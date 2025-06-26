"""
Move recommendation system for Pokémon battles.
This module provides intelligent move suggestions based on type effectiveness.
"""

from ..data.pokemon_data import TYPE_CHART
from ..data.move_data import get_moves_for_pokemon, get_move_info, MOVE_DATA


def recommend_moves(attacking_pokemon, defending_pokemon, pokemon_data):
    """
    Recommend the best moves for a Pokémon to use against an opponent.
    
    Args:
        attacking_pokemon (str): Name of the attacking Pokémon
        defending_pokemon (str): Name of the defending Pokémon
        pokemon_data (dict): Dictionary containing Pokémon type data
        
    Returns:
        dict: Dictionary containing move recommendations and analysis
    """
    attacking_types = pokemon_data.get(attacking_pokemon, [])
    defending_types = pokemon_data.get(defending_pokemon, [])
    
    if not attacking_types or not defending_types:
        return None
    
    # Get available moves for the attacking Pokémon
    available_moves = get_moves_for_pokemon(attacking_pokemon)
    
    if not available_moves:
        return {
            'pokemon': attacking_pokemon,
            'opponent': defending_pokemon,
            'recommendations': [],
            'message': f"No move data available for {attacking_pokemon}"
        }
    
    # Analyze each move
    move_analysis = []
    for move_name in available_moves:
        move_info = get_move_info(move_name)
        if move_info:
            move_type, power, accuracy, pp, category, description = move_info
            effectiveness = calculate_move_effectiveness(move_type, defending_types)
            
            # Calculate move score (effectiveness * power * accuracy)
            move_score = effectiveness * power * (accuracy / 100)
            
            move_analysis.append({
                'name': move_name,
                'type': move_type,
                'power': power,
                'accuracy': accuracy,
                'category': category,
                'description': description,
                'effectiveness': effectiveness,
                'score': move_score,
                'recommendation': get_move_recommendation(effectiveness, move_type, defending_pokemon)
            })
    
    # Sort moves by score (best first)
    move_analysis.sort(key=lambda x: x['score'], reverse=True)
    
    # Get top recommendations
    top_moves = move_analysis[:4]  # Top 4 moves
    
    # Generate strategy tips
    strategy_tips = generate_strategy_tips(move_analysis, attacking_pokemon, defending_pokemon)
    
    return {
        'pokemon': attacking_pokemon,
        'opponent': defending_pokemon,
        'recommendations': top_moves,
        'all_moves': move_analysis,
        'strategy_tips': strategy_tips,
        'best_move': top_moves[0] if top_moves else None
    }


def calculate_move_effectiveness(move_type, defending_types):
    """Calculate the effectiveness of a move against defending types."""
    effectiveness = 1.0
    for defending_type in defending_types:
        effectiveness *= TYPE_CHART.get(move_type, {}).get(defending_type, 1.0)
    return effectiveness


def get_move_recommendation(effectiveness, move_type, defending_pokemon):
    """Generate a recommendation message for a move."""
    if effectiveness == 0.0:
        return f"❌ AVOID: {move_type} moves have NO EFFECT against {defending_pokemon}!"
    elif effectiveness < 1.0:
        return f"⚠️ WEAK: {move_type} moves are NOT VERY EFFECTIVE against {defending_pokemon}"
    elif effectiveness > 1.0:
        return f"✅ EXCELLENT: {move_type} moves are SUPER EFFECTIVE against {defending_pokemon}!"
    else:
        return f"🟡 NEUTRAL: {move_type} moves have normal effectiveness against {defending_pokemon}"


def generate_strategy_tips(move_analysis, attacking_pokemon, defending_pokemon):
    """Generate strategic advice for the matchup."""
    tips = []
    
    # Find best and worst moves
    best_moves = [move for move in move_analysis if move['effectiveness'] > 1.0]
    weak_moves = [move for move in move_analysis if move['effectiveness'] < 1.0]
    useless_moves = [move for move in move_analysis if move['effectiveness'] == 0.0]
    
    if best_moves:
        best_move = best_moves[0]
        tips.append(f"🎯 BEST CHOICE: Use {best_move['name']} ({best_move['type']}) - "
                   f"{best_move['power']} power, {best_move['accuracy']}% accuracy")
    
    if len(best_moves) > 1:
        tips.append(f"💪 BACKUP OPTIONS: You have {len(best_moves)} super-effective moves available")
    
    if weak_moves:
        tips.append(f"⚠️ AVOID: {len(weak_moves)} moves are not very effective")
    
    if useless_moves:
        tips.append(f"❌ USELESS: {len(useless_moves)} moves have no effect - don't use them!")
    
    # Type coverage advice
    move_types = set(move['type'] for move in move_analysis)
    if len(move_types) >= 3:
        tips.append(f"🌈 GOOD COVERAGE: Your {attacking_pokemon} has {len(move_types)} different move types")
    
    # Accuracy vs Power trade-off
    high_power_low_acc = [move for move in move_analysis if move['power'] >= 100 and move['accuracy'] < 85]
    if high_power_low_acc:
        tips.append("🎲 HIGH RISK: Consider accuracy vs power trade-offs for maximum damage moves")
    
    return tips


def get_counter_moves(defending_pokemon, pokemon_data):
    """
    Find moves that are effective against a specific Pokémon.
    
    Args:
        defending_pokemon (str): Name of the defending Pokémon
        pokemon_data (dict): Dictionary containing Pokémon type data
        
    Returns:
        list: List of move types that are effective against the defending Pokémon
    """
    defending_types = pokemon_data.get(defending_pokemon, [])
    if not defending_types:
        return []
    
    effective_moves = []
    for move_type in TYPE_CHART.keys():
        effectiveness = calculate_move_effectiveness(move_type, defending_types)
        if effectiveness > 1.0:
            effective_moves.append({
                'type': move_type,
                'effectiveness': effectiveness,
                'description': f"{move_type} moves are {effectiveness:.1f}x effective"
            })
    
    # Sort by effectiveness
    effective_moves.sort(key=lambda x: x['effectiveness'], reverse=True)
    return effective_moves


def analyze_move_coverage(pokemon_name, pokemon_data):
    """
    Analyze the type coverage of a Pokémon's moves.
    
    Args:
        pokemon_name (str): Name of the Pokémon
        pokemon_data (dict): Dictionary containing Pokémon type data
        
    Returns:
        dict: Analysis of the Pokémon's move coverage
    """
    available_moves = get_moves_for_pokemon(pokemon_name)
    if not available_moves:
        return {'coverage': 'No move data available'}
    
    move_types = set()
    physical_moves = 0
    special_moves = 0
    status_moves = 0
    
    for move_name in available_moves:
        move_info = get_move_info(move_name)
        if move_info:
            move_type, power, accuracy, pp, category, description = move_info
            move_types.add(move_type)
            
            if category == "Physical":
                physical_moves += 1
            elif category == "Special":
                special_moves += 1
            elif category == "Status":
                status_moves += 1
    
    coverage_score = len(move_types)
    coverage_quality = "Excellent" if coverage_score >= 4 else "Good" if coverage_score >= 3 else "Limited"
    
    return {
        'pokemon': pokemon_name,
        'total_moves': len(available_moves),
        'unique_types': len(move_types),
        'move_types': list(move_types),
        'physical_moves': physical_moves,
        'special_moves': special_moves,
        'status_moves': status_moves,
        'coverage_score': coverage_score,
        'coverage_quality': coverage_quality,
        'recommendation': get_coverage_recommendation(coverage_score, physical_moves, special_moves)
    }


def get_coverage_recommendation(coverage_score, physical_moves, special_moves):
    """Generate recommendations based on move coverage analysis."""
    recommendations = []
    
    if coverage_score < 3:
        recommendations.append("Consider adding more diverse move types for better coverage")
    
    if physical_moves == 0:
        recommendations.append("No physical moves - consider adding some for mixed attacking")
    elif special_moves == 0:
        recommendations.append("No special moves - consider adding some for mixed attacking")
    
    if physical_moves >= 3 and special_moves >= 3:
        recommendations.append("Good mix of physical and special moves - versatile attacker")
    
    return recommendations 