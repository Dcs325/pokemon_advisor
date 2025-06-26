"""
Move data and move recommendation system.
This module contains move information and logic for suggesting optimal moves.
"""

# Move Database: Maps move names to their properties
# Format: "Move Name": [type, power, accuracy, pp, category, description]
MOVE_DATA = {
    # Fire Moves
    "Fire Blast": ["Fire", 110, 85, 5, "Special", "A powerful fire attack that may burn the target."],
    "Flamethrower": ["Fire", 90, 100, 15, "Special", "A powerful fire attack that may burn the target."],
    "Fire Punch": ["Fire", 75, 100, 15, "Physical", "A fiery punch that may burn the target."],
    "Ember": ["Fire", 40, 100, 25, "Special", "A weak fire attack that may burn the target."],
    "Inferno": ["Fire", 100, 50, 5, "Special", "An intense fire attack that always burns the target."],
    "Flare Blitz": ["Fire", 120, 100, 15, "Physical", "A powerful fire attack that damages the user."],
    "Pyro Ball": ["Fire", 120, 90, 5, "Physical", "A powerful fire attack that may burn."],
    "Torch Song": ["Fire", 80, 100, 10, "Special", "A fire attack that raises Special Attack."],
    
    # Water Moves
    "Hydro Pump": ["Water", 110, 80, 5, "Special", "A powerful water attack."],
    "Surf": ["Water", 90, 100, 15, "Special", "A powerful water attack that hits all adjacent foes."],
    "Aqua Jet": ["Water", 40, 100, 20, "Physical", "A fast water attack that always goes first."],
    "Water Gun": ["Water", 40, 100, 25, "Special", "A weak water attack."],
    "Liquidation": ["Water", 85, 100, 10, "Physical", "A powerful water attack that may lower Defense."],
    "Waterfall": ["Water", 80, 100, 15, "Physical", "A powerful water attack that may cause flinching."],
    "Aqua Step": ["Water", 80, 100, 10, "Physical", "A water attack that raises Speed."],
    "Surging Strikes": ["Water", 25, 100, 5, "Physical", "Always hits 3 times with critical hits."],
    
    # Electric Moves
    "Thunderbolt": ["Electric", 90, 100, 15, "Special", "A powerful electric attack that may paralyze."],
    "Thunder": ["Electric", 110, 70, 10, "Special", "A powerful electric attack that may paralyze."],
    "Thunder Punch": ["Electric", 75, 100, 15, "Physical", "An electric punch that may paralyze."],
    "Thunder Shock": ["Electric", 40, 100, 30, "Special", "A weak electric attack that may paralyze."],
    "Volt Tackle": ["Electric", 120, 100, 15, "Physical", "A powerful electric attack that damages the user."],
    "Overdrive": ["Electric", 80, 100, 10, "Special", "An electric attack that may paralyze."],
    "Volt Switch": ["Electric", 70, 100, 20, "Special", "An electric attack that switches the user out."],
    
    # Grass Moves
    "Solar Beam": ["Grass", 120, 100, 10, "Special", "A powerful grass attack that takes time to charge."],
    "Leaf Blade": ["Grass", 90, 100, 15, "Physical", "A sharp leaf attack with high critical hit ratio."],
    "Giga Drain": ["Grass", 75, 100, 10, "Special", "A grass attack that heals the user."],
    "Vine Whip": ["Grass", 45, 100, 25, "Physical", "A weak grass attack using vines."],
    "Energy Ball": ["Grass", 90, 100, 10, "Special", "A grass attack that may lower Special Defense."],
    "Wood Hammer": ["Grass", 120, 100, 15, "Physical", "A powerful grass attack that damages the user."],
    "Flower Trick": ["Grass", 70, 100, 10, "Physical", "A grass attack that always hits and crits."],
    "Drum Beating": ["Grass", 80, 100, 10, "Physical", "A grass attack that lowers Speed."],
    
    # Ice Moves
    "Ice Beam": ["Ice", 90, 100, 10, "Special", "A powerful ice attack that may freeze."],
    "Blizzard": ["Ice", 110, 70, 5, "Special", "A powerful ice attack that may freeze."],
    "Ice Punch": ["Ice", 75, 100, 15, "Physical", "An ice punch that may freeze."],
    "Avalanche": ["Ice", 60, 100, 10, "Physical", "An ice attack that's stronger if hit first."],
    "Freeze-Dry": ["Ice", 70, 100, 20, "Special", "An ice attack that's super effective against Water."],
    "Ice Fang": ["Ice", 65, 95, 15, "Physical", "An ice attack that may freeze or cause flinching."],
    
    # Fighting Moves
    "Close Combat": ["Fighting", 120, 100, 5, "Physical", "A powerful fighting attack that lowers defenses."],
    "Dynamic Punch": ["Fighting", 100, 50, 5, "Physical", "A powerful fighting attack that confuses."],
    "Mach Punch": ["Fighting", 40, 100, 30, "Physical", "A fast fighting attack that always goes first."],
    "Brick Break": ["Fighting", 75, 100, 15, "Physical", "A fighting attack that breaks barriers."],
    "Aura Sphere": ["Fighting", 80, 100, 20, "Special", "A fighting attack that never misses."],
    "High Jump Kick": ["Fighting", 130, 90, 10, "Physical", "A powerful fighting attack that damages the user if it misses."],
    "Drain Punch": ["Fighting", 75, 100, 10, "Physical", "A fighting attack that heals the user."],
    
    # Poison Moves
    "Sludge Bomb": ["Poison", 90, 100, 10, "Special", "A poison attack that may poison."],
    "Poison Jab": ["Poison", 80, 100, 20, "Physical", "A poison attack that may poison."],
    "Toxic": ["Poison", 0, 90, 10, "Status", "Badly poisons the target."],
    "Venoshock": ["Poison", 65, 100, 10, "Special", "Stronger if target is poisoned."],
    "Gunk Shot": ["Poison", 120, 80, 5, "Physical", "A powerful poison attack."],
    
    # Ground Moves
    "Earthquake": ["Ground", 100, 100, 10, "Physical", "A powerful ground attack that hits all adjacent foes."],
    "Dig": ["Ground", 80, 100, 10, "Physical", "A ground attack that takes time to charge."],
    "Earth Power": ["Ground", 90, 100, 10, "Special", "A ground attack that may lower Special Defense."],
    "Mud Shot": ["Ground", 55, 95, 15, "Special", "A ground attack that may lower Speed."],
    "High Horsepower": ["Ground", 95, 95, 10, "Physical", "A powerful ground attack."],
    
    # Flying Moves
    "Brave Bird": ["Flying", 120, 100, 15, "Physical", "A powerful flying attack that damages the user."],
    "Air Slash": ["Flying", 75, 95, 15, "Special", "A flying attack that may cause flinching."],
    "Hurricane": ["Flying", 110, 70, 10, "Special", "A powerful flying attack that may confuse."],
    "Aerial Ace": ["Flying", 60, 100, 20, "Physical", "A flying attack that never misses."],
    "Drill Peck": ["Flying", 80, 100, 20, "Physical", "A powerful flying attack."],
    "Bounce": ["Flying", 85, 85, 5, "Physical", "A flying attack that takes time to charge."],
    
    # Psychic Moves
    "Psychic": ["Psychic", 90, 100, 10, "Special", "A psychic attack that may lower Special Defense."],
    "Psyshock": ["Psychic", 80, 100, 10, "Special", "A psychic attack that targets Defense."],
    "Zen Headbutt": ["Psychic", 80, 90, 15, "Physical", "A psychic attack that may cause flinching."],
    "Confusion": ["Psychic", 50, 100, 25, "Special", "A weak psychic attack that may confuse."],
    "Future Sight": ["Psychic", 120, 100, 10, "Special", "An attack that hits on the next turn."],
    "Extrasensory": ["Psychic", 80, 100, 20, "Special", "A psychic attack that may cause flinching."],
    
    # Bug Moves
    "Megahorn": ["Bug", 120, 85, 10, "Physical", "A powerful bug attack."],
    "X-Scissor": ["Bug", 80, 100, 15, "Physical", "A bug attack using crossed scythes."],
    "Bug Buzz": ["Bug", 90, 100, 10, "Special", "A bug attack that may lower Special Defense."],
    "U-turn": ["Bug", 70, 100, 20, "Physical", "A bug attack that switches the user out."],
    "Signal Beam": ["Bug", 75, 100, 15, "Special", "A bug attack that may confuse."],
    "Leech Life": ["Bug", 80, 100, 10, "Physical", "A bug attack that heals the user."],
    
    # Rock Moves
    "Stone Edge": ["Rock", 100, 80, 5, "Physical", "A powerful rock attack with high critical hit ratio."],
    "Rock Slide": ["Rock", 75, 90, 10, "Physical", "A rock attack that may cause flinching."],
    "Power Gem": ["Rock", 80, 100, 20, "Special", "A rock attack using light energy."],
    "Rock Throw": ["Rock", 50, 90, 15, "Physical", "A weak rock attack."],
    "Ancient Power": ["Rock", 60, 100, 5, "Special", "A rock attack that may raise all stats."],
    
    # Ghost Moves
    "Shadow Ball": ["Ghost", 80, 100, 15, "Special", "A ghost attack that may lower Special Defense."],
    "Shadow Claw": ["Ghost", 70, 100, 15, "Physical", "A ghost attack with high critical hit ratio."],
    "Hex": ["Ghost", 65, 100, 10, "Special", "Stronger if target has a status condition."],
    "Phantom Force": ["Ghost", 90, 100, 10, "Physical", "A ghost attack that takes time to charge."],
    "Shadow Sneak": ["Ghost", 40, 100, 30, "Physical", "A ghost attack that always goes first."],
    "Spirit Shackle": ["Ghost", 80, 100, 10, "Physical", "A ghost attack that prevents switching."],
    "Astral Barrage": ["Ghost", 120, 100, 5, "Special", "A powerful ghost attack."],
    
    # Dragon Moves
    "Outrage": ["Dragon", 120, 100, 10, "Physical", "A powerful dragon attack that confuses the user."],
    "Dragon Claw": ["Dragon", 80, 100, 15, "Physical", "A dragon attack using sharp claws."],
    "Dragon Pulse": ["Dragon", 85, 100, 10, "Special", "A dragon attack using energy waves."],
    "Dragon Rage": ["Dragon", 0, 100, 10, "Special", "Always deals 40 HP of damage."],
    "Draco Meteor": ["Dragon", 130, 90, 5, "Special", "A powerful dragon attack that lowers Special Attack."],
    "Clanging Scales": ["Dragon", 110, 100, 5, "Special", "A dragon attack that lowers Defense."],
    
    # Steel Moves
    "Iron Head": ["Steel", 80, 100, 15, "Physical", "A steel attack that may cause flinching."],
    "Flash Cannon": ["Steel", 80, 100, 10, "Special", "A steel attack that may lower Special Defense."],
    "Meteor Mash": ["Steel", 90, 90, 10, "Physical", "A steel attack that may raise Attack."],
    "Steel Wing": ["Steel", 70, 90, 25, "Physical", "A steel attack that may raise Defense."],
    "Gyro Ball": ["Steel", 0, 100, 5, "Physical", "Stronger the slower the user is."],
    "Behemoth Blade": ["Steel", 100, 100, 5, "Physical", "A powerful steel attack."],
    "Behemoth Bash": ["Steel", 100, 100, 5, "Physical", "A powerful steel attack."],
    "Make It Rain": ["Steel", 120, 100, 5, "Special", "A steel attack that lowers Special Attack."],
    
    # Dark Moves
    "Crunch": ["Dark", 80, 100, 15, "Physical", "A dark attack that may lower Defense."],
    "Dark Pulse": ["Dark", 80, 100, 15, "Special", "A dark attack that may cause flinching."],
    "Sucker Punch": ["Dark", 70, 100, 5, "Physical", "A dark attack that always goes first."],
    "Night Slash": ["Dark", 70, 100, 15, "Physical", "A dark attack with high critical hit ratio."],
    "Foul Play": ["Dark", 95, 100, 15, "Physical", "Uses the target's Attack stat."],
    "Darkest Lariat": ["Dark", 85, 100, 10, "Physical", "A dark attack that ignores stat changes."],
    "Knock Off": ["Dark", 65, 100, 20, "Physical", "A dark attack that removes held items."],
    
    # Fairy Moves
    "Moonblast": ["Fairy", 95, 100, 15, "Special", "A fairy attack that may lower Special Attack."],
    "Play Rough": ["Fairy", 90, 90, 10, "Physical", "A fairy attack that may lower Attack."],
    "Dazzling Gleam": ["Fairy", 80, 100, 10, "Special", "A fairy attack using light energy."],
    "Fairy Wind": ["Fairy", 40, 100, 30, "Special", "A weak fairy attack."],
    "Spirit Break": ["Fairy", 75, 100, 15, "Physical", "A fairy attack that lowers Special Attack."],
    
    # Normal Moves
    "Hyper Beam": ["Normal", 150, 90, 5, "Special", "A powerful normal attack that requires rest."],
    "Return": ["Normal", 0, 100, 20, "Physical", "Stronger the more the user likes its trainer."],
    "Body Slam": ["Normal", 85, 100, 15, "Physical", "A normal attack that may paralyze."],
    "Quick Attack": ["Normal", 40, 100, 30, "Physical", "A fast normal attack that always goes first."],
    "Tackle": ["Normal", 40, 100, 35, "Physical", "A weak normal attack."],
    "Extreme Speed": ["Normal", 80, 100, 5, "Physical", "A normal attack that always goes first."],
    "Boomburst": ["Normal", 140, 100, 10, "Special", "A powerful normal attack that hits all adjacent foes."],
    
    # Status Moves
    "Focus Blast": ["Fighting", 120, 70, 5, "Special", "A powerful fighting attack that may lower Special Defense."],
    "Thunder Wave": ["Electric", 0, 90, 20, "Status", "Paralyzes the target."],
    "Sleep Powder": ["Grass", 0, 75, 15, "Status", "Puts the target to sleep."],
    "Leech Seed": ["Grass", 0, 90, 10, "Status", "Drains HP from the target each turn."],
    "Dragon Dance": ["Dragon", 0, 100, 20, "Status", "Raises Attack and Speed."],
    "Swords Dance": ["Normal", 0, 100, 20, "Status", "Sharply raises Attack."],
    "Calm Mind": ["Psychic", 0, 100, 20, "Status", "Raises Special Attack and Special Defense."],
    "Will-O-Wisp": ["Fire", 0, 85, 15, "Status", "Burns the target."],
    "Roost": ["Flying", 0, 100, 10, "Status", "Restores HP and removes Flying type temporarily."],
    "Bulk Up": ["Fighting", 0, 100, 20, "Status", "Raises Attack and Defense."],
    "Nasty Plot": ["Dark", 0, 100, 20, "Status", "Sharply raises Special Attack."],
    "Recover": ["Normal", 0, 100, 10, "Status", "Restores HP."],
    "Slack Off": ["Normal", 0, 100, 10, "Status", "Restores HP."],
    "Spiky Shield": ["Grass", 0, 100, 10, "Status", "Protects and damages attackers."],
    "King's Shield": ["Steel", 0, 100, 10, "Status", "Protects and lowers Attack of attackers."],
    "Sacred Sword": ["Fighting", 90, 100, 15, "Physical", "A fighting attack that ignores stat changes."],
    "Howl": ["Normal", 0, 100, 40, "Status", "Raises Attack."],
    "Quiver Dance": ["Bug", 0, 100, 20, "Status", "Raises Special Attack, Special Defense, and Speed."],
    "Fiery Dance": ["Fire", 80, 100, 10, "Special", "A fire attack that may raise Special Attack."],
    "Court Change": ["Normal", 0, 100, 10, "Status", "Switches field effects with the opponent."],
    "Snipe Shot": ["Water", 80, 100, 15, "Special", "A water attack that ignores abilities."],
    "Self-Destruct": ["Normal", 200, 100, 5, "Physical", "A powerful attack that faints the user."],
    "Iron Tail": ["Steel", 100, 75, 15, "Physical", "A steel attack that may lower Defense."],
    "Fire Fang": ["Fire", 65, 95, 15, "Physical", "A fire attack that may burn or cause flinching."],
    "Thunder Fang": ["Electric", 65, 95, 15, "Physical", "An electric attack that may paralyze or cause flinching."],
    "Ice Fang": ["Ice", 65, 95, 15, "Physical", "An ice attack that may freeze or cause flinching."],
}

# Pokémon Move Sets: Maps Pokémon names to their available moves
# This is a simplified version - in a full implementation, you'd have complete move sets
POKEMON_MOVES = {
    "Charizard": ["Fire Blast", "Flamethrower", "Air Slash", "Dragon Claw", "Earthquake", "Solar Beam"],
    "Blastoise": ["Hydro Pump", "Surf", "Ice Beam", "Earthquake", "Flash Cannon", "Focus Blast"],
    "Venusaur": ["Solar Beam", "Giga Drain", "Sludge Bomb", "Earthquake", "Sleep Powder", "Leech Seed"],
    "Pikachu": ["Thunderbolt", "Thunder", "Quick Attack", "Iron Tail", "Brick Break", "Volt Tackle"],
    "Gengar": ["Shadow Ball", "Sludge Bomb", "Thunderbolt", "Focus Blast", "Psychic", "Dark Pulse"],
    "Machamp": ["Close Combat", "Dynamic Punch", "Stone Edge", "Earthquake", "Ice Punch", "Thunder Punch"],
    "Alakazam": ["Psychic", "Shadow Ball", "Focus Blast", "Energy Ball", "Dazzling Gleam", "Thunder Wave"],
    "Gyarados": ["Waterfall", "Earthquake", "Stone Edge", "Ice Fang", "Dragon Dance", "Bounce"],
    "Dragonite": ["Outrage", "Dragon Claw", "Fire Punch", "Thunder Punch", "Earthquake", "Extreme Speed"],
    "Snorlax": ["Body Slam", "Earthquake", "Fire Punch", "Thunder Punch", "Ice Punch", "Self-Destruct"],
    "Lucario": ["Aura Sphere", "Close Combat", "Flash Cannon", "Dark Pulse", "Earthquake", "Extreme Speed"],
    "Gardevoir": ["Psychic", "Moonblast", "Shadow Ball", "Focus Blast", "Thunderbolt", "Calm Mind"],
    "Tyranitar": ["Stone Edge", "Crunch", "Earthquake", "Fire Punch", "Ice Punch", "Thunder Punch"],
    "Metagross": ["Meteor Mash", "Psychic", "Earthquake", "Thunder Punch", "Ice Punch", "Zen Headbutt"],
    "Garchomp": ["Outrage", "Earthquake", "Stone Edge", "Fire Fang", "Dragon Claw", "Swords Dance"],
    "Salamence": ["Outrage", "Dragon Claw", "Fire Blast", "Earthquake", "Stone Edge", "Dragon Dance"],
    "Garchomp": ["Outrage", "Earthquake", "Stone Edge", "Fire Fang", "Dragon Claw", "Swords Dance"],
    "Hydreigon": ["Draco Meteor", "Dark Pulse", "Fire Blast", "Earth Power", "Focus Blast", "U-turn"],
    "Volcarona": ["Fire Blast", "Bug Buzz", "Hurricane", "Giga Drain", "Quiver Dance", "Fiery Dance"],
    "Greninja": ["Hydro Pump", "Dark Pulse", "Ice Beam", "U-turn", "Extrasensory", "Gunk Shot"],
    "Aegislash": ["Shadow Ball", "Iron Head", "Sacred Sword", "Shadow Sneak", "King's Shield", "Swords Dance"],
    "Talonflame": ["Brave Bird", "Flare Blitz", "U-turn", "Roost", "Swords Dance", "Will-O-Wisp"],
    "Goodra": ["Draco Meteor", "Fire Blast", "Thunderbolt", "Ice Beam", "Sludge Bomb", "Focus Blast"],
    "Decidueye": ["Leaf Blade", "Spirit Shackle", "Brave Bird", "Sucker Punch", "Swords Dance", "Roost"],
    "Incineroar": ["Flare Blitz", "Darkest Lariat", "Close Combat", "U-turn", "Swords Dance", "Will-O-Wisp"],
    "Primarina": ["Moonblast", "Hydro Pump", "Energy Ball", "Psychic", "Ice Beam", "Calm Mind"],
    "Lycanroc": ["Stone Edge", "Crunch", "Fire Fang", "Thunder Fang", "Ice Fang", "Swords Dance"],
    "Mimikyu": ["Play Rough", "Shadow Claw", "Shadow Sneak", "Swords Dance", "Wood Hammer", "Leech Life"],
    "Kommo-o": ["Close Combat", "Dragon Claw", "Poison Jab", "Earthquake", "Dragon Dance", "Clanging Scales"],
    "Corviknight": ["Brave Bird", "Iron Head", "Body Press", "U-turn", "Bulk Up", "Roost"],
    "Cinderace": ["Pyro Ball", "High Jump Kick", "U-turn", "Gunk Shot", "Bulk Up", "Court Change"],
    "Inteleon": ["Hydro Pump", "Snipe Shot", "Ice Beam", "U-turn", "Air Slash", "Dark Pulse"],
    "Rillaboom": ["Wood Hammer", "High Horsepower", "U-turn", "Knock Off", "Swords Dance", "Drum Beating"],
    "Dragapult": ["Draco Meteor", "Shadow Ball", "Fire Blast", "Thunderbolt", "U-turn", "Dragon Dance"],
    "Toxtricity": ["Overdrive", "Sludge Bomb", "Boomburst", "Volt Switch", "Fire Punch", "Thunder Punch"],
    "Urshifu": ["Close Combat", "Surging Strikes", "U-turn", "Ice Punch", "Thunder Punch", "Bulk Up"],
    "Zacian": ["Behemoth Blade", "Play Rough", "Close Combat", "Iron Head", "Swords Dance", "Sacred Sword"],
    "Zamazenta": ["Behemoth Bash", "Close Combat", "Crunch", "Iron Head", "Howl", "Sacred Sword"],
    "Calyrex": ["Astral Barrage", "Giga Drain", "Psychic", "Earth Power", "Nasty Plot", "Leech Seed"],
    "Flutter Mane": ["Moonblast", "Shadow Ball", "Mystical Fire", "Thunderbolt", "Calm Mind", "Dazzling Gleam"],
    "Iron Hands": ["Close Combat", "Thunder Punch", "Ice Punch", "Fire Punch", "Bulk Up", "Drain Punch"],
    "Gholdengo": ["Make It Rain", "Shadow Ball", "Focus Blast", "Thunderbolt", "Nasty Plot", "Recover"],
    "Skeledirge": ["Torch Song", "Shadow Ball", "Earth Power", "Will-O-Wisp", "Nasty Plot", "Slack Off"],
    "Quaquaval": ["Aqua Step", "Close Combat", "Ice Punch", "U-turn", "Swords Dance", "Roost"],
    "Meowscarada": ["Flower Trick", "Knock Off", "U-turn", "Play Rough", "Swords Dance", "Spiky Shield"],
}

def get_moves_for_pokemon(pokemon_name):
    """Get the available moves for a specific Pokémon."""
    return POKEMON_MOVES.get(pokemon_name, [])

def get_move_info(move_name):
    """Get detailed information about a specific move."""
    return MOVE_DATA.get(move_name, None)

def get_moves_by_type(move_type):
    """Get all moves of a specific type."""
    return [move for move, data in MOVE_DATA.items() if data[0] == move_type]

def get_physical_moves():
    """Get all physical moves."""
    return [move for move, data in MOVE_DATA.items() if data[4] == "Physical"]

def get_special_moves():
    """Get all special moves."""
    return [move for move, data in MOVE_DATA.items() if data[4] == "Special"]

def get_status_moves():
    """Get all status moves."""
    return [move for move, data in MOVE_DATA.items() if data[4] == "Status"] 