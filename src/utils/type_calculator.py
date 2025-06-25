"""
Type effectiveness calculation utilities.
This module contains functions for calculating Pokémon type matchups.
"""

from ..data.pokemon_data import TYPE_CHART


def calculate_type_effectiveness(attacking_type, defending_types):
    """
    Calculates the combined effectiveness of a single attacking type against
    one or two defending types.
    
    Args:
        attacking_type (str): The type of the attacking move
        defending_types (list): List of defending Pokémon's types
        
    Returns:
        float: The effectiveness multiplier (0.0, 0.5, 1.0, or 2.0)
    """
    multiplier = 1.0
    for d_type in defending_types:
        multiplier *= TYPE_CHART.get(attacking_type, {}).get(d_type, 1.0)
    return multiplier


def analyze_matchup(your_pokemon_name, opponent_pokemon_name, pokemon_data):
    """
    Analyzes the matchup between two Pokémon and returns detailed analysis.
    
    Args:
        your_pokemon_name (str): Name of your Pokémon
        opponent_pokemon_name (str): Name of the opponent Pokémon
        pokemon_data (dict): Dictionary containing Pokémon type data
        
    Returns:
        dict: Dictionary containing analysis results
    """
    your_pokemon_types = pokemon_data.get(your_pokemon_name, [])
    opponent_pokemon_types = pokemon_data.get(opponent_pokemon_name, [])
    
    if not your_pokemon_types or not opponent_pokemon_types:
        return None
    
    # Your Pokémon's offensive capability
    your_offensive_multiplier = 0.0
    your_offensive_details = []
    
    for your_atk_type in your_pokemon_types:
        effectiveness = calculate_type_effectiveness(your_atk_type, opponent_pokemon_types)
        your_offensive_multiplier = max(your_offensive_multiplier, effectiveness)
        
        detail = {
            'type': your_atk_type,
            'effectiveness': effectiveness,
            'description': _get_effectiveness_description(effectiveness, your_atk_type, opponent_pokemon_name)
        }
        your_offensive_details.append(detail)
    
    # Opponent Pokémon's offensive capability
    opponent_offensive_multiplier = 0.0
    opponent_offensive_details = []
    
    for opp_atk_type in opponent_pokemon_types:
        effectiveness = calculate_type_effectiveness(opp_atk_type, your_pokemon_types)
        opponent_offensive_multiplier = max(opponent_offensive_multiplier, effectiveness)
        
        detail = {
            'type': opp_atk_type,
            'effectiveness': effectiveness,
            'description': _get_defensive_description(effectiveness, opp_atk_type, your_pokemon_name)
        }
        opponent_offensive_details.append(detail)
    
    # Overall matchup summary
    matchup_summary = _get_matchup_summary(your_offensive_multiplier, opponent_offensive_multiplier)
    
    return {
        'your_pokemon': {
            'name': your_pokemon_name,
            'types': your_pokemon_types,
            'offensive_multiplier': your_offensive_multiplier,
            'offensive_details': your_offensive_details
        },
        'opponent_pokemon': {
            'name': opponent_pokemon_name,
            'types': opponent_pokemon_types,
            'offensive_multiplier': opponent_offensive_multiplier,
            'offensive_details': opponent_offensive_details
        },
        'matchup_summary': matchup_summary
    }


def _get_effectiveness_description(effectiveness, attacking_type, defending_name):
    """Generate description for offensive effectiveness."""
    if effectiveness == 0.0:
        return f"NO EFFECT! ({defending_name} is immune to {attacking_type})."
    elif effectiveness < 1.0:
        return f"NOT VERY EFFECTIVE ({effectiveness:.1f}x damage)."
    elif effectiveness > 1.0:
        return f"SUPER EFFECTIVE ({effectiveness:.1f}x damage)!"
    else:
        return f"Normal Effectiveness ({effectiveness:.1f}x damage)."


def _get_defensive_description(effectiveness, attacking_type, defending_name):
    """Generate description for defensive effectiveness."""
    if effectiveness == 0.0:
        return f"You are IMMUNE! ({defending_name} takes 0x from {attacking_type})."
    elif effectiveness < 1.0:
        return f"You RESIST ({effectiveness:.1f}x damage taken)."
    elif effectiveness > 1.0:
        return f"You are VULNERABLE ({effectiveness:.1f}x damage taken)!"
    else:
        return f"Normal damage taken ({effectiveness:.1f}x damage taken)."


def _get_matchup_summary(your_offensive, opponent_offensive):
    """Generate overall matchup summary."""
    if your_offensive >= 2.0 and opponent_offensive <= 0.5:
        return "🌟 This is a VERY FAVORABLE matchup for you! You hit hard, they hit weakly."
    elif your_offensive >= 2.0 and opponent_offensive >= 2.0:
        return "🔥 This is a highly OFFENSIVE matchup. You hit hard, but they hit hard too! Be careful!"
    elif your_offensive <= 0.5 and opponent_offensive >= 2.0:
        return "🚨 This is a VERY UNFAVORABLE matchup for you! You hit weakly, and they hit hard. Consider switching!"
    elif your_offensive == 0.0:
        return "🚫 You cannot damage them at all. This is a bad matchup offensively, retreat!"
    elif opponent_offensive == 0.0:
        return "✨ You are immune to their attacks, giving you a huge advantage!"
    else:
        return "🤝 This matchup is relatively balanced, or presents moderate advantages/disadvantages. Strategy is key!" 