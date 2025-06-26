"""
Team Builder system for Pokémon teams.
This module provides team analysis, coverage checking, weakness identification, and synergy suggestions.
"""

from ..data.pokemon_data import POKEMON_DATA, TYPE_CHART, ALL_TYPES
from ..data.move_data import get_moves_for_pokemon, get_move_info
from ..utils.move_recommender import analyze_move_coverage
from collections import defaultdict, Counter


class TeamBuilder:
    """Team building and analysis system."""
    
    def __init__(self):
        self.team = []
        self.team_analysis = {}
    
    def add_pokemon(self, pokemon_name):
        """Add a Pokémon to the team."""
        if pokemon_name not in POKEMON_DATA:
            return False, f"Pokémon '{pokemon_name}' not found in database."
        
        if len(self.team) >= 6:
            return False, "Team is already full (6 Pokémon maximum)."
        
        if pokemon_name in [p['name'] for p in self.team]:
            return False, f"{pokemon_name} is already in your team."
        
        pokemon_types = POKEMON_DATA[pokemon_name]
        pokemon_data = {
            'name': pokemon_name,
            'types': pokemon_types,
            'move_coverage': analyze_move_coverage(pokemon_name, POKEMON_DATA)
        }
        
        self.team.append(pokemon_data)
        return True, f"{pokemon_name} added to team."
    
    def remove_pokemon(self, pokemon_name):
        """Remove a Pokémon from the team."""
        for i, pokemon in enumerate(self.team):
            if pokemon['name'] == pokemon_name:
                removed = self.team.pop(i)
                return True, f"{removed['name']} removed from team."
        return False, f"{pokemon_name} not found in team."
    
    def clear_team(self):
        """Clear the entire team."""
        self.team.clear()
        return True, "Team cleared."
    
    def get_team(self):
        """Get the current team."""
        return self.team.copy()
    
    def analyze_team(self):
        """Perform comprehensive team analysis."""
        if not self.team:
            return {
                'status': 'empty',
                'message': 'No Pokémon in team to analyze.'
            }
        
        analysis = {
            'team_size': len(self.team),
            'pokemon_list': [p['name'] for p in self.team],
            'type_analysis': self._analyze_team_types(),
            'coverage_analysis': self._analyze_team_coverage(),
            'weakness_analysis': self._analyze_team_weaknesses(),
            'synergy_analysis': self._analyze_team_synergy(),
            'recommendations': self._generate_team_recommendations()
        }
        
        self.team_analysis = analysis
        return analysis
    
    def _analyze_team_types(self):
        """Analyze the type distribution in the team."""
        type_counts = Counter()
        type_combinations = []
        
        for pokemon in self.team:
            types = pokemon['types']
            type_counts.update(types)
            type_combinations.append(f"{pokemon['name']}: {'/'.join(types)}")
        
        # Find most and least common types
        most_common = type_counts.most_common(3)
        least_common = [(t, c) for t, c in type_counts.items() if c == 1]
        
        # Check for type diversity
        unique_types = len(type_counts)
        diversity_score = unique_types / 18  # Out of 18 total types
        
        return {
            'type_distribution': dict(type_counts),
            'type_combinations': type_combinations,
            'most_common_types': most_common,
            'least_common_types': least_common,
            'unique_types': unique_types,
            'diversity_score': diversity_score,
            'diversity_rating': self._get_diversity_rating(diversity_score)
        }
    
    def _analyze_team_coverage(self):
        """Analyze the offensive coverage of the team."""
        team_moves = defaultdict(list)
        coverage_by_type = defaultdict(list)
        
        for pokemon in self.team:
            pokemon_name = pokemon['name']
            available_moves = get_moves_for_pokemon(pokemon_name)
            
            for move_name in available_moves:
                move_info = get_move_info(move_name)
                if move_info:
                    move_type = move_info[0]
                    team_moves[move_type].append(f"{pokemon_name}: {move_name}")
                    coverage_by_type[move_type].append(pokemon_name)
        
        # Calculate coverage effectiveness against each type
        coverage_effectiveness = {}
        for defending_type in ALL_TYPES:
            effectiveness = 0
            best_attackers = []
            
            for attacking_type, attackers in coverage_by_type.items():
                if attacking_type in TYPE_CHART and defending_type in TYPE_CHART[attacking_type]:
                    type_effectiveness = TYPE_CHART[attacking_type][defending_type]
                    if type_effectiveness > effectiveness:
                        effectiveness = type_effectiveness
                        best_attackers = attackers
                    elif type_effectiveness == effectiveness:
                        best_attackers.extend(attackers)
            
            coverage_effectiveness[defending_type] = {
                'effectiveness': effectiveness,
                'attackers': list(set(best_attackers))
            }
        
        # Find coverage gaps
        coverage_gaps = [t for t, data in coverage_effectiveness.items() if data['effectiveness'] < 1.0]
        excellent_coverage = [t for t, data in coverage_effectiveness.items() if data['effectiveness'] >= 2.0]
        
        return {
            'team_moves': dict(team_moves),
            'coverage_by_type': dict(coverage_by_type),
            'coverage_effectiveness': coverage_effectiveness,
            'coverage_gaps': coverage_gaps,
            'excellent_coverage': excellent_coverage,
            'coverage_score': len(excellent_coverage) / 18
        }
    
    def _analyze_team_weaknesses(self):
        """Analyze defensive weaknesses in the team."""
        team_weaknesses = defaultdict(list)
        team_resistances = defaultdict(list)
        team_immunities = defaultdict(list)
        
        for pokemon in self.team:
            pokemon_name = pokemon['name']
            pokemon_types = pokemon['types']
            
            for attacking_type in ALL_TYPES:
                effectiveness = 1.0
                for defending_type in pokemon_types:
                    if attacking_type in TYPE_CHART and defending_type in TYPE_CHART[attacking_type]:
                        effectiveness *= TYPE_CHART[attacking_type][defending_type]
                
                if effectiveness > 1.0:
                    team_weaknesses[attacking_type].append(pokemon_name)
                elif effectiveness < 1.0:
                    team_resistances[attacking_type].append(pokemon_name)
                if effectiveness == 0.0:
                    team_immunities[attacking_type].append(pokemon_name)
        
        # Find critical weaknesses (affecting multiple team members)
        critical_weaknesses = {t: pokemon for t, pokemon in team_weaknesses.items() if len(pokemon) >= 2}
        
        # Find defensive gaps (no resistance to certain types)
        defensive_gaps = [t for t in ALL_TYPES if t not in team_resistances and t not in team_immunities]
        
        return {
            'team_weaknesses': dict(team_weaknesses),
            'team_resistances': dict(team_resistances),
            'team_immunities': dict(team_immunities),
            'critical_weaknesses': critical_weaknesses,
            'defensive_gaps': defensive_gaps,
            'weakness_score': len(critical_weaknesses) / 18
        }
    
    def _analyze_team_synergy(self):
        """Analyze how well team members work together."""
        synergy_pairs = []
        anti_synergy_pairs = []
        
        for i, pokemon1 in enumerate(self.team):
            for j, pokemon2 in enumerate(self.team[i+1:], i+1):
                synergy_score = self._calculate_pair_synergy(pokemon1, pokemon2)
                
                if synergy_score > 0.7:
                    synergy_pairs.append({
                        'pokemon1': pokemon1['name'],
                        'pokemon2': pokemon2['name'],
                        'score': synergy_score,
                        'reason': self._get_synergy_reason(pokemon1, pokemon2)
                    })
                elif synergy_score < 0.3:
                    anti_synergy_pairs.append({
                        'pokemon1': pokemon1['name'],
                        'pokemon2': pokemon2['name'],
                        'score': synergy_score,
                        'reason': self._get_anti_synergy_reason(pokemon1, pokemon2)
                    })
        
        # Sort by synergy score
        synergy_pairs.sort(key=lambda x: x['score'], reverse=True)
        anti_synergy_pairs.sort(key=lambda x: x['score'])
        
        return {
            'synergy_pairs': synergy_pairs,
            'anti_synergy_pairs': anti_synergy_pairs,
            'overall_synergy': len(synergy_pairs) - len(anti_synergy_pairs)
        }
    
    def _calculate_pair_synergy(self, pokemon1, pokemon2):
        """Calculate synergy score between two Pokémon."""
        score = 0.0
        
        # Type synergy (resistances and immunities)
        types1 = set(pokemon1['types'])
        types2 = set(pokemon2['types'])
        
        # Check if they cover each other's weaknesses
        for type1 in types1:
            for type2 in types2:
                if type1 in TYPE_CHART and type2 in TYPE_CHART[type1]:
                    if TYPE_CHART[type1][type2] < 1.0:  # Resistance
                        score += 0.2
                    elif TYPE_CHART[type1][type2] == 0.0:  # Immunity
                        score += 0.4
        
        # Move coverage synergy
        moves1 = get_moves_for_pokemon(pokemon1['name'])
        moves2 = get_moves_for_pokemon(pokemon2['name'])
        
        move_types1 = set()
        move_types2 = set()
        
        for move in moves1:
            move_info = get_move_info(move)
            if move_info:
                move_types1.add(move_info[0])
        
        for move in moves2:
            move_info = get_move_info(move)
            if move_info:
                move_types2.add(move_info[0])
        
        # Different move types = better coverage
        unique_types = len(move_types1.union(move_types2))
        score += unique_types * 0.1
        
        return min(score, 1.0)
    
    def _get_synergy_reason(self, pokemon1, pokemon2):
        """Get reason for good synergy between two Pokémon."""
        types1 = pokemon1['types']
        types2 = pokemon2['types']
        
        reasons = []
        
        # Check for type resistances
        for type1 in types1:
            for type2 in types2:
                if type1 in TYPE_CHART and type2 in TYPE_CHART[type1]:
                    if TYPE_CHART[type1][type2] < 1.0:
                        reasons.append(f"{pokemon2['name']} resists {type1}")
                    elif TYPE_CHART[type1][type2] == 0.0:
                        reasons.append(f"{pokemon2['name']} is immune to {type1}")
        
        if not reasons:
            reasons.append("Good move coverage diversity")
        
        return "; ".join(reasons)
    
    def _get_anti_synergy_reason(self, pokemon1, pokemon2):
        """Get reason for poor synergy between two Pokémon."""
        types1 = pokemon1['types']
        types2 = pokemon2['types']
        
        reasons = []
        
        # Check for shared weaknesses
        for type1 in types1:
            for type2 in types2:
                if type1 in TYPE_CHART and type2 in TYPE_CHART[type1]:
                    if TYPE_CHART[type1][type2] > 1.0:
                        reasons.append(f"Both weak to {type1}")
        
        if not reasons:
            reasons.append("Limited move coverage diversity")
        
        return "; ".join(reasons)
    
    def _generate_team_recommendations(self):
        """Generate recommendations for improving the team."""
        recommendations = []
        
        if len(self.team) < 6:
            recommendations.append(f"Add {6 - len(self.team)} more Pokémon to complete your team.")
        
        # Coverage recommendations
        coverage_analysis = self._analyze_team_coverage()
        if coverage_analysis['coverage_gaps']:
            recommendations.append(f"Add moves to cover: {', '.join(coverage_analysis['coverage_gaps'][:3])}")
        
        # Weakness recommendations
        weakness_analysis = self._analyze_team_weaknesses()
        if weakness_analysis['critical_weaknesses']:
            weak_types = list(weakness_analysis['critical_weaknesses'].keys())[:3]
            recommendations.append(f"Add resistance to: {', '.join(weak_types)}")
        
        # Type diversity recommendations
        type_analysis = self._analyze_team_types()
        if type_analysis['diversity_score'] < 0.5:
            recommendations.append("Consider adding more diverse Pokémon types for better coverage.")
        
        return recommendations
    
    def _get_diversity_rating(self, diversity_score):
        """Get a rating for type diversity."""
        if diversity_score >= 0.8:
            return "Excellent"
        elif diversity_score >= 0.6:
            return "Good"
        elif diversity_score >= 0.4:
            return "Fair"
        else:
            return "Poor"
    
    def suggest_pokemon(self, criteria=None):
        """Suggest Pokémon to add to the team based on current analysis."""
        if not self.team:
            return self._suggest_balanced_starters()
        
        analysis = self.analyze_team()
        suggestions = []
        
        # Suggest based on coverage gaps
        coverage_gaps = analysis['coverage_analysis']['coverage_gaps']
        if coverage_gaps:
            for gap_type in coverage_gaps[:2]:
                suggestions.extend(self._find_pokemon_with_type(gap_type))
        
        # Suggest based on weaknesses
        critical_weaknesses = analysis['weakness_analysis']['critical_weaknesses']
        if critical_weaknesses:
            for weak_type in list(critical_weaknesses.keys())[:2]:
                suggestions.extend(self._find_pokemon_resistant_to(weak_type))
        
        # Remove duplicates and already in team
        unique_suggestions = []
        team_names = [p['name'] for p in self.team]
        
        for suggestion in suggestions:
            if suggestion not in unique_suggestions and suggestion not in team_names:
                unique_suggestions.append(suggestion)
        
        return unique_suggestions[:5]  # Return top 5 suggestions
    
    def _suggest_balanced_starters(self):
        """Suggest a balanced starter team."""
        return [
            "Charizard",  # Fire/Flying
            "Blastoise",  # Water
            "Venusaur",   # Grass/Poison
            "Pikachu",    # Electric
            "Machamp",    # Fighting
            "Gengar"      # Ghost/Poison
        ]
    
    def _find_pokemon_with_type(self, target_type):
        """Find Pokémon that have a specific type."""
        pokemon_with_type = []
        for pokemon_name, types in POKEMON_DATA.items():
            if target_type in types:
                pokemon_with_type.append(pokemon_name)
        return pokemon_with_type[:3]  # Return top 3
    
    def _find_pokemon_resistant_to(self, target_type):
        """Find Pokémon that resist a specific type."""
        resistant_pokemon = []
        for pokemon_name, types in POKEMON_DATA.items():
            effectiveness = 1.0
            for defending_type in types:
                if target_type in TYPE_CHART and defending_type in TYPE_CHART[target_type]:
                    effectiveness *= TYPE_CHART[target_type][defending_type]
            
            if effectiveness < 1.0:
                resistant_pokemon.append(pokemon_name)
        
        return resistant_pokemon[:3]  # Return top 3


def analyze_team_from_list(pokemon_list):
    """Convenience function to analyze a team from a list of Pokémon names."""
    builder = TeamBuilder()
    for pokemon_name in pokemon_list:
        if pokemon_name in POKEMON_DATA:
            builder.add_pokemon(pokemon_name)
    
    return builder.analyze_team()


def get_team_suggestions(current_team):
    """Get suggestions for improving a team."""
    builder = TeamBuilder()
    for pokemon_name in current_team:
        if pokemon_name in POKEMON_DATA:
            builder.add_pokemon(pokemon_name)
    
    return builder.suggest_pokemon() 