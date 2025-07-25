"""
Pokémon data and type effectiveness information.
This module contains all the static data used by the application.
"""

# All standard Pokémon types
ALL_TYPES = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon",
    "Steel", "Dark", "Fairy"
]

# Pokémon Data: Maps Pokémon names to their primary and (optional) secondary types.
POKEMON_DATA = {
    "Select Pokémon": [], # Placeholder for initial dropdown state
    "Bulbasaur": ["Grass", "Poison"],
    "Charmander": ["Fire"],
    "Squirtle": ["Water"],
    "Pikachu": ["Electric"],
    "Jigglypuff": ["Normal", "Fairy"],
    "Machamp": ["Fighting"],
    "Gengar": ["Ghost", "Poison"],
    "Onix": ["Rock", "Ground"],
    "Eevee": ["Normal"],
    "Snorlax": ["Normal"],
    "Dragonite": ["Dragon", "Flying"],
    "Lucario": ["Fighting", "Steel"],
    "Gardevoir": ["Psychic", "Fairy"],
    "Tyranitar": ["Rock", "Dark"],
    "Metagross": ["Steel", "Psychic"],
    "Togekiss": ["Fairy", "Flying"],
    "Mimikyu": ["Ghost", "Fairy"],
    "Charizard": ["Fire", "Flying"],
    "Blastoise": ["Water"],
    "Venusaur": ["Grass", "Poison"],
    "Alakazam": ["Psychic"],
    "Arcanine": ["Fire"],
    "Gyarados": ["Water", "Flying"],
    "Jolteon": ["Electric"],
    "Vaporeon": ["Water"],
    "Flareon": ["Fire"],
    "Rhydon": ["Ground", "Rock"],
    "Lapras": ["Water", "Ice"],
    "Articuno": ["Ice", "Flying"],
    "Zapdos": ["Electric", "Flying"],
    "Moltres": ["Fire", "Flying"],
    "Mewtwo": ["Psychic"],
    "Mew": ["Psychic"],
    "Typhlosion": ["Fire"],
    "Feraligatr": ["Water"],
    "Meganium": ["Grass"],
    "Ampharos": ["Electric"],
    "Scizor": ["Bug", "Steel"],
    "Heracross": ["Bug", "Fighting"],
    "Umbreon": ["Dark"],
    "Espeon": ["Psychic"],
    "Donphan": ["Ground"],
    "Sceptile": ["Grass"],
    "Blaziken": ["Fire", "Fighting"],
    "Swampert": ["Water", "Ground"],
    "Salamence": ["Dragon", "Flying"],
    "Groudon": ["Ground"],
    "Kyogre": ["Water"],
    "Rayquaza": ["Dragon", "Flying"],
    "Staraptor": ["Normal", "Flying"],
    "Luxray": ["Electric"],
    "Garchomp": ["Dragon", "Ground"],
    "Weavile": ["Dark", "Ice"],
    "Porygon-Z": ["Normal"],
    "Heatran": ["Fire", "Steel"],
    "Giratina": ["Ghost", "Dragon"],
    "Dialga": ["Steel", "Dragon"],
    "Palkia": ["Water", "Dragon"],
    "Darkrai": ["Dark"],
    "Shaymin": ["Grass"],
    "Arceus": ["Normal"], # Can change type with plates, but default is Normal
    "Zoroark": ["Dark"],
    "Chandelure": ["Ghost", "Fire"],
    "Haxorus": ["Dragon"],
    "Hydreigon": ["Dark", "Dragon"],
    "Volcarona": ["Bug", "Fire"],
    "Reshiram": ["Dragon", "Fire"],
    "Zekrom": ["Dragon", "Electric"],
    "Kyurem": ["Dragon", "Ice"],
    "Greninja": ["Water", "Dark"],
    "Talonflame": ["Fire", "Flying"],
    "Aegislash": ["Steel", "Ghost"],
    "Sylveon": ["Fairy"],
    "Hawlucha": ["Fighting", "Flying"],
    "Goodra": ["Dragon"],
    "Decidueye": ["Grass", "Ghost"],
    "Incineroar": ["Fire", "Dark"],
    "Primarina": ["Water", "Fairy"],
    "Lycanroc": ["Rock"],
    "Kommo-o": ["Dragon", "Fighting"],
    "Necrozma": ["Psychic"],
    "Corviknight": ["Flying", "Steel"],
    "Cinderace": ["Fire"],
    "Inteleon": ["Water"],
    "Rillaboom": ["Grass"],
    "Dragapult": ["Dragon", "Ghost"],
    "Toxtricity": ["Electric", "Poison"],
    "Urshifu": ["Fighting", "Water"], # Single Strike & Rapid Strike have different types
    "Zacian": ["Fairy", "Steel"],
    "Zamazenta": ["Fighting", "Steel"],
    "Calyrex": ["Psychic", "Grass"],
    "Flutter Mane": ["Ghost", "Fairy"],
    "Iron Hands": ["Fighting", "Electric"],
    "Gholdengo": ["Steel", "Ghost"],
    "Skeledirge": ["Fire", "Ghost"],
    "Quaquaval": ["Water", "Fighting"],
    "Meowscarada": ["Grass", "Dark"],
    # Expanded list based on common Pokémon and type combinations
    "Abra": ["Psychic"],
    "Kadabra": ["Psychic"],
    "Diglett": ["Ground"],
    "Dugtrio": ["Ground"],
    "Meowth": ["Normal"],
    "Persian": ["Normal"],
    "Poliwag": ["Water"],
    "Poliwhirl": ["Water"],
    "Poliwrath": ["Water", "Fighting"],
    "Machop": ["Fighting"],
    "Machoke": ["Fighting"],
    "Bellsprout": ["Grass", "Poison"],
    "Weepinbell": ["Grass", "Poison"],
    "Victreebel": ["Grass", "Poison"],
    "Tentacool": ["Water", "Poison"],
    "Tentacruel": ["Water", "Poison"],
    "Geodude": ["Rock", "Ground"],
    "Graveler": ["Rock", "Ground"],
    "Golem": ["Rock", "Ground"],
    "Ponyta": ["Fire"],
    "Rapidash": ["Fire"],
    "Slowpoke": ["Water", "Psychic"],
    "Slowbro": ["Water", "Psychic"],
    "Magnemite": ["Electric", "Steel"],
    "Magneton": ["Electric", "Steel"],
    "Farfetch'd": ["Normal", "Flying"],
    "Doduo": ["Normal", "Flying"],
    "Dodrio": ["Normal", "Flying"],
    "Seel": ["Water"],
    "Dewgong": ["Water", "Ice"],
    "Grimer": ["Poison"],
    "Muk": ["Poison"],
    "Shellder": ["Water"],
    "Cloyster": ["Water", "Ice"],
    "Gastly": ["Ghost", "Poison"],
    "Haunter": ["Ghost", "Poison"],
    "Drowzee": ["Psychic"],
    "Hypno": ["Psychic"],
    "Krabby": ["Water"],
    "Kingler": ["Water"],
    "Voltorb": ["Electric"],
    "Electrode": ["Electric"],
    "Exeggcute": ["Grass", "Psychic"],
    "Exeggutor": ["Grass", "Psychic"],
    "Cubone": ["Ground"],
    "Marowak": ["Ground"],
    "Hitmonlee": ["Fighting"],
    "Hitmonchan": ["Fighting"],
    "Lickitung": ["Normal"],
    "Koffing": ["Poison"],
    "Weezing": ["Poison"],
    "Rhyhorn": ["Ground", "Rock"],
    "Chansey": ["Normal"],
    "Tangela": ["Grass"],
    "Kangaskhan": ["Normal"],
    "Horsea": ["Water"],
    "Seadra": ["Water"],
    "Goldeen": ["Water"],
    "Seaking": ["Water"],
    "Staryu": ["Water"],
    "Starmie": ["Water", "Psychic"],
    "Mr. Mime": ["Psychic", "Fairy"],
    "Scyther": ["Bug", "Flying"],
    "Jynx": ["Ice", "Psychic"],
    "Electabuzz": ["Electric"],
    "Magmar": ["Fire"],
    "Pinsir": ["Bug"],
    "Tauros": ["Normal"],
    "Magikarp": ["Water"],
    "Ditto": ["Normal"],
    "Porygon": ["Normal"],
    "Omanyte": ["Rock", "Water"],
    "Omastar": ["Rock", "Water"],
    "Kabuto": ["Rock", "Water"],
    "Kabutops": ["Rock", "Water"],
    "Aerodactyl": ["Rock", "Flying"],
    "Dratini": ["Dragon"],
    "Dragonair": ["Dragon"],
    # Generation 2
    "Chikorita": ["Grass"],
    "Bayleef": ["Grass"],
    "Cyndaquil": ["Fire"],
    "Quilava": ["Fire"],
    "Totodile": ["Water"],
    "Croconaw": ["Water"],
    "Sentret": ["Normal"],
    "Furret": ["Normal"],
    "Hoothoot": ["Normal", "Flying"],
    "Noctowl": ["Normal", "Flying"],
    "Ledyba": ["Bug", "Flying"],
    "Ledian": ["Bug", "Flying"],
    "Spinarak": ["Bug", "Poison"],
    "Ariados": ["Bug", "Poison"],
    "Crobat": ["Poison", "Flying"],
    "Chinchou": ["Water", "Electric"],
    "Lanturn": ["Water", "Electric"],
    "Pichu": ["Electric"],
    "Cleffa": ["Fairy"],
    "Igglybuff": ["Normal", "Fairy"],
    "Togepi": ["Fairy"],
    "Togetic": ["Fairy", "Flying"],
    "Natu": ["Psychic", "Flying"],
    "Xatu": ["Psychic", "Flying"],
    "Mareep": ["Electric"],
    "Flaaffy": ["Electric"],
    "Sudowoodo": ["Rock"],
    "Politoed": ["Water"],
    "Hoppip": ["Grass", "Flying"],
    "Skiploom": ["Grass", "Flying"],
    "Jumpluff": ["Grass", "Flying"],
    "Aipom": ["Normal"],
    "Sunkern": ["Grass"],
    "Sunflora": ["Grass"],
    "Yanma": ["Bug", "Flying"],
    "Wooper": ["Water", "Ground"],
    "Quagsire": ["Water", "Ground"],
    "Murkrow": ["Dark", "Flying"],
    "Slowking": ["Water", "Psychic"],
    "Misdreavus": ["Ghost"],
    "Unown": ["Psychic"],
    "Wobbuffet": ["Psychic"],
    "Girafarig": ["Normal", "Psychic"],
    "Pineco": ["Bug"],
    "Forretress": ["Bug", "Steel"],
    "Dunsparce": ["Normal"],
    "Gligar": ["Ground", "Flying"],
    "Steelix": ["Steel", "Ground"],
    "Snubbull": ["Fairy"],
    "Granbull": ["Fairy"],
    "Qwilfish": ["Water", "Poison"],
    "Shuckle": ["Bug", "Rock"],
    "Sneasel": ["Dark", "Ice"],
    "Teddiursa": ["Normal"],
    "Ursaring": ["Normal"],
    "Slugma": ["Fire"],
    "Magcargo": ["Fire", "Rock"],
    "Swinub": ["Ice", "Ground"],
    "Piloswine": ["Ice", "Ground"],
    "Corsola": ["Water", "Rock"],
    "Remoraid": ["Water"],
    "Octillery": ["Water"],
    "Delibird": ["Ice", "Flying"],
    "Mantine": ["Water", "Flying"],
    "Skarmory": ["Steel", "Flying"],
    "Houndour": ["Dark", "Fire"],
    "Houndoom": ["Dark", "Fire"],
    "Kingdra": ["Water", "Dragon"],
    "Phanpy": ["Ground"],
    "Porygon2": ["Normal"],
    "Stantler": ["Normal"],
    "Smeargle": ["Normal"],
    "Tyrogue": ["Fighting"],
    "Hitmontop": ["Fighting"],
    "Smoochum": ["Ice", "Psychic"],
    "Elekid": ["Electric"],
    "Magby": ["Fire"],
    "Miltank": ["Normal"],
    "Blissey": ["Normal"],
    "Raikou": ["Electric"],
    "Entei": ["Fire"],
    "Suicune": ["Water"],
    "Larvitar": ["Rock", "Ground"],
    "Pupitar": ["Rock", "Ground"],
    "Lugia": ["Psychic", "Flying"],
    "Ho-Oh": ["Fire", "Flying"],
    "Celebi": ["Psychic", "Grass"],
    "Drapion": ["Poison", "Dark"],
    "Scorbunny": ["Fire"],
    "Grookey": ["Grass"],
    "Sobble": ["Water"],
    "Cramorant": ["Flying", "Water"],
    "Appletun": ["Grass", "Dragon"],
    "Flapple": ["Grass", "Dragon"],
    "Coalossal": ["Rock", "Fire"],
    "Urshifu (Single Strike)": ["Fighting", "Dark"],
    "Urshifu (Rapid Strike)": ["Fighting", "Water"],
    "Zarude": ["Dark", "Grass"],
    "Regieleki": ["Electric"],
    "Regidrago": ["Dragon"],
    "Glastrier": ["Ice"],
    "Spectrier": ["Ghost"],
    "Iron Bundle": ["Ice", "Water"],
    "Iron Moth": ["Fire", "Poison"],
    "Iron Thorns": ["Rock", "Electric"],
    "Iron Valiant": ["Fairy", "Fighting"],
    "Iron Treads": ["Ground", "Steel"],
    "Iron Jugulis": ["Dark", "Flying"],
    "Walking Wake": ["Water", "Dragon"],
    "Slither Wing": ["Bug", "Fighting"],
    "Sandy Shocks": ["Electric", "Ground"],
    "Great Tusk": ["Ground", "Fighting"],
    "Brute Bonnet": ["Grass", "Dark"],
    "Scream Tail": ["Fairy", "Psychic"],
    "Roaring Moon": ["Dragon", "Dark"],
    "Iron Leaves": ["Grass", "Psychic"],
    "Dudunsparce": ["Normal"], # Expanded form of Dunsparce
    "Maushold": ["Normal"], # Evolution of Tandemaus
    "Palafin": ["Water"], # Evolution of Finizen, has a stronger form
    "Tatsugiri": ["Dragon", "Water"],
    "Cyclizar": ["Dragon", "Normal"],
    "Pawmot": ["Electric", "Fighting"],
    "Clodsire": ["Poison", "Ground"],
    "Dondozo": ["Water"],
    "Kingambit": ["Dark", "Steel"],
    "Annihilape": ["Fighting", "Ghost"],
    "Farigiraf": ["Normal", "Psychic"],
    "Dachsbun": ["Fairy"],
    "Koraidon": ["Fighting", "Dragon"], # Legendaries
    "Miraidon": ["Electric", "Dragon"], # Legendaries
}

# Type Effectiveness Chart (Attacking Type -> Defending Type -> Multiplier)
# 2.0 = Super Effective (2x damage)
# 1.0 = Normal Effectiveness (1x damage)
# 0.5 = Not Very Effective (0.5x damage)
# 0.0 = No Effect (0x damage)
TYPE_CHART = {
    "Normal": {
        "Rock": 0.5, "Ghost": 0.0, "Steel": 0.5,
    },
    "Fire": {
        "Grass": 2.0, "Ice": 2.0, "Bug": 2.0, "Steel": 2.0,
        "Fire": 0.5, "Water": 0.5, "Dragon": 0.5, "Rock": 0.5,
    },
    "Water": {
        "Fire": 2.0, "Ground": 2.0, "Rock": 2.0,
        "Water": 0.5, "Grass": 0.5, "Dragon": 0.5,
    },
    "Electric": {
        "Water": 2.0, "Flying": 2.0,
        "Electric": 0.5, "Grass": 0.5, "Dragon": 0.5, "Ground": 0.0,
    },
    "Grass": {
        "Water": 2.0, "Ground": 2.0, "Rock": 2.0,
        "Fire": 0.5, "Grass": 0.5, "Poison": 0.5, "Flying": 0.5, "Bug": 0.5, "Dragon": 0.5, "Steel": 0.5,
    },
    "Ice": {
        "Grass": 2.0, "Ground": 2.0, "Flying": 2.0, "Dragon": 2.0,
        "Fire": 0.5, "Water": 0.5, "Ice": 0.5, "Steel": 0.5,
    },
    "Fighting": {
        "Normal": 2.0, "Ice": 2.0, "Rock": 2.0, "Dark": 2.0, "Steel": 2.0,
        "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Fairy": 0.5, "Ghost": 0.0,
    },
    "Poison": {
        "Grass": 2.0, "Fairy": 2.0,
        "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0.0,
    },
    "Ground": {
        "Fire": 2.0, "Electric": 2.0, "Poison": 2.0, "Rock": 2.0, "Steel": 2.0,
        "Grass": 0.5, "Bug": 0.5, "Flying": 0.0,
    },
    "Flying": {
        "Grass": 2.0, "Fighting": 2.0, "Bug": 2.0,
        "Electric": 0.5, "Rock": 0.5, "Steel": 0.5,
    },
    "Psychic": {
        "Fighting": 2.0, "Poison": 2.0,
        "Psychic": 0.5, "Steel": 0.5, "Dark": 0.0,
    },
    "Bug": {
        "Grass": 2.0, "Psychic": 2.0, "Dark": 2.0,
        "Fire": 0.5, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Ghost": 0.5, "Steel": 0.5, "Fairy": 0.5,
    },
    "Rock": {
        "Fire": 2.0, "Ice": 2.0, "Flying": 2.0, "Bug": 2.0,
        "Fighting": 0.5, "Ground": 0.5, "Steel": 0.5,
    },
    "Ghost": {
        "Psychic": 2.0, "Ghost": 2.0,
        "Normal": 0.0, "Dark": 0.5, "Steel": 0.5,
    },
    "Dragon": {
        "Dragon": 2.0,
        "Steel": 0.5, "Fairy": 0.0,
    },
    "Steel": {
        "Ice": 2.0, "Rock": 2.0, "Fairy": 2.0,
        "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Steel": 0.5,
    },
    "Dark": {
        "Psychic": 2.0, "Ghost": 2.0,
        "Fighting": 0.5, "Dark": 0.5, "Fairy": 0.5,
    },
    "Fairy": {
        "Fighting": 2.0, "Dragon": 2.0, "Dark": 2.0,
        "Fire": 0.5, "Poison": 0.5, "Steel": 0.5,
    }
}

# Fill in default 1.0 for types not explicitly listed (normal effectiveness)
for attacking_type in ALL_TYPES:
    for defending_type in ALL_TYPES:
        if defending_type not in TYPE_CHART.get(attacking_type, {}):
            if attacking_type not in TYPE_CHART:
                TYPE_CHART[attacking_type] = {} # Initialize if not exists
            TYPE_CHART[attacking_type][defending_type] = 1.0 