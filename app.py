import random # Not directly used for logic, but often useful in games
import os
import sys
import threading # For potential background tasks, though Pygame handles music well
import time

# Suppress the Tk deprecation warning on macOS
# This should be set BEFORE tkinter is imported for it to take effect
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# --- Module Availability Checks ---
try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
    import tkinter.font as tkfont
    _tkinter_available = True
except ImportError:
    _tkinter_available = False
    print("Error: tkinter is not available. Please install tkinter or ensure your Python includes Tcl/Tk.")
    print("If you are on Linux, try: sudo apt-get install python3-tk") # Or for Homebrew: python3 -m pip install tk
    sys.exit(1) # Exit if Tkinter is not available, as GUI is required.

try:
    import pygame
    pygame.mixer.init() # Initialize the mixer specifically for music
    _pygame_available = True
except ImportError:
    _pygame_available = False
    print("Warning: pygame is not available. Music functionality will be disabled.")
    print("To install pygame: pip install pygame")

# --- Configuration & Data ---

MUSIC_FILE = "pokemon_battle_theme.mp3" # !!! IMPORTANT: Replace with your actual music file path (.mp3, .wav, .ogg)

# All standard Pokémon types
ALL_TYPES = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon",
    "Steel", "Dark", "Fairy"
]

# Pokémon Data: Maps Pokémon names to their primary and (optional) secondary types.
# You can expand this dictionary with many more Pokémon!
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
    "Metagross": ["Steel", "Psychic"],
    "Groudon": ["Ground"],
    "Kyogre": ["Water"],
    "Rayquaza": ["Dragon", "Flying"],
    "Staraptor": ["Normal", "Flying"],
    "Luxray": ["Electric"],
    "Garchomp": ["Dragon", "Ground"],
    "Lucario": ["Fighting", "Steel"],
    "Weavile": ["Dark", "Ice"],
    "Togekiss": ["Fairy", "Flying"],
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
    "Mimikyu": ["Ghost", "Fairy"],
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
    "Alakazam": ["Psychic"],
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
    "Onix": ["Rock", "Ground"], # Already there, but keeping consistent for expansion logic
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
    "Rhydon": ["Ground", "Rock"], # Already there
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
    "Gyarados": ["Water", "Flying"], # Already there
    "Lapras": ["Water", "Ice"], # Already there
    "Ditto": ["Normal"],
    "Eevee": ["Normal"], # Already there
    "Vaporeon": ["Water"], # Already there
    "Jolteon": ["Electric"], # Already there
    "Flareon": ["Fire"], # Already there
    "Porygon": ["Normal"],
    "Omanyte": ["Rock", "Water"],
    "Omastar": ["Rock", "Water"],
    "Kabuto": ["Rock", "Water"],
    "Kabutops": ["Rock", "Water"],
    "Aerodactyl": ["Rock", "Flying"],
    "Snorlax": ["Normal"], # Already there
    "Articuno": ["Ice", "Flying"], # Already there
    "Zapdos": ["Electric", "Flying"], # Already there
    "Moltres": ["Fire", "Flying"], # Already there
    "Dratini": ["Dragon"],
    "Dragonair": ["Dragon"],
    "Dragonite": ["Dragon", "Flying"], # Already there
    "Mewtwo": ["Psychic"], # Already there
    "Mew": ["Psychic"], # Already there
    # Generation 2
    "Chikorita": ["Grass"],
    "Bayleef": ["Grass"],
    "Meganium": ["Grass"], # Already there
    "Cyndaquil": ["Fire"],
    "Quilava": ["Fire"],
    "Typhlosion": ["Fire"], # Already there
    "Totodile": ["Water"],
    "Croconaw": ["Water"],
    "Feraligatr": ["Water"], # Already there
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
    "Ampharos": ["Electric"], # Already there
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
    "Scizor": ["Bug", "Steel"], # Already there
    "Shuckle": ["Bug", "Rock"],
    "Heracross": ["Bug", "Fighting"], # Already there
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
    "Donphan": ["Ground"], # Already there
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
    "Tyranitar": ["Rock", "Dark"], # Already there
    "Lugia": ["Psychic", "Flying"],
    "Ho-Oh": ["Fire", "Flying"],
    "Celebi": ["Psychic", "Grass"],
    # Adding some more from later generations for variety
    "Swampert": ["Water", "Ground"],
    "Sceptile": ["Grass"],
    "Blaziken": ["Fire", "Fighting"],
    "Gardevoir": ["Psychic", "Fairy"],
    "Salamence": ["Dragon", "Flying"],
    "Metagross": ["Steel", "Psychic"],
    "Groudon": ["Ground"],
    "Kyogre": ["Water"],
    "Rayquaza": ["Dragon", "Flying"],
    "Luxray": ["Electric"],
    "Garchomp": ["Dragon", "Ground"],
    "Lucario": ["Fighting", "Steel"],
    "Weavile": ["Dark", "Ice"],
    "Porygon-Z": ["Normal"],
    "Heatran": ["Fire", "Steel"],
    "Giratina": ["Ghost", "Dragon"],
    "Dialga": ["Steel", "Dragon"],
    "Palkia": ["Water", "Dragon"],
    "Darkrai": ["Dark"],
    "Shaymin": ["Grass"],
    "Arceus": ["Normal"],
    "Zoroark": ["Dark"],
    "Chandelure": ["Ghost", "Fire"],
    "Haxorus": ["Dragon"],
    "Hydreigon": ["Dark", "Dragon"],
    "Volcarona": ["Bug", "Fire"],
    "Greninja": ["Water", "Dark"],
    "Aegislash": ["Steel", "Ghost"],
    "Sylveon": ["Fairy"],
    "Corviknight": ["Flying", "Steel"],
    "Dragapult": ["Dragon", "Ghost"],
    "Gholdengo": ["Steel", "Ghost"],
    "Skeledirge": ["Fire", "Ghost"],
    "Quaquaval": ["Water", "Fighting"],
    "Meowscarada": ["Grass", "Dark"],
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

# --- Tkinter GUI Application ---

class PokemonOpponentApp:
    def __init__(self, master):
        self.master = master
        self._setup_window()
        self._setup_fonts()
        self._create_widgets()
        self._load_music()

    def _setup_window(self):
        """Configures the main application window."""
        self.master.title("Pokémon Opponent Recommender")
        self.master.geometry("750x780") # Adjusted height for more text
        self.master.resizable(True, True) # Allow resizing
        self.master.configure(bg="#2a4d69") # Dark blue-gray background

        # Center the window
        self.master.update_idletasks()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f'+{x}+{y}')

        # Configure grid weights for responsiveness
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=0) # Title
        self.master.rowconfigure(1, weight=0) # Controls
        self.master.rowconfigure(2, weight=1) # Results area

    def _setup_fonts(self):
        """Configures custom fonts for the application."""
        try:
            self.title_font = tkfont.Font(family="Arial", size=26, weight="bold")
            self.header_font = tkfont.Font(family="Arial", size=16, weight="bold")
            self.label_font = tkfont.Font(family="Arial", size=12)
            self.button_font = tkfont.Font(family="Arial", size=14, weight="bold")
            self.text_area_font = tkfont.Font(family="Courier New", size=12) # Monospaced for output
        except Exception:
            self.title_font = ("TkDefaultFont", 26, "bold")
            self.header_font = ("TkDefaultFont", 16, "bold")
            self.label_font = ("TkDefaultFont", 12)
            self.button_font = ("TkDefaultFont", 14, "bold")
            self.text_area_font = ("TkFixedFont", 12) # Fallback to system monospaced

    def _create_widgets(self):
        """Creates and places all GUI widgets."""
        # --- Title ---
        title_label = tk.Label(self.master, text="Pokémon Opponent Advisor",
                               font=self.title_font, fg="#ffc107", bg="#2a4d69") # Gold-ish text
        title_label.grid(row=0, column=0, pady=20, sticky="n")

        # --- Control Frame (User Inputs) ---
        control_frame = tk.Frame(self.master, bg="#396c8d", bd=4, relief=tk.RAISED, padx=20, pady=20)
        control_frame.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        control_frame.columnconfigure(0, weight=1)
        control_frame.columnconfigure(1, weight=1)

        # Your Pokémon Name Selection
        tk.Label(control_frame, text="Select Your Pokémon:", font=self.label_font, bg="#396c8d", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.your_pokemon_var = tk.StringVar(self.master)
        pokemon_names_sorted = sorted(list(POKEMON_DATA.keys()))
        self.your_pokemon_var.set(pokemon_names_sorted[0]) # Set default to "Select Pokémon"
        your_pokemon_menu = tk.OptionMenu(control_frame, self.your_pokemon_var, *pokemon_names_sorted)
        your_pokemon_menu.config(font=self.label_font, bg="#f8f9fa", fg="#343a40", relief=tk.GROOVE, bd=2)
        your_pokemon_menu["menu"].config(font=self.label_font, bg="#f8f9fa", fg="#343a40")
        your_pokemon_menu.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Target Opponent Pokémon Selection
        tk.Label(control_frame, text="Select Target Opponent:", font=self.label_font, bg="#396c8d", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.opponent_pokemon_var = tk.StringVar(self.master)
        # Populate with the same list, but default to "Select Pokémon" for clarity
        self.opponent_pokemon_var.set(pokemon_names_sorted[0])
        opponent_pokemon_menu = tk.OptionMenu(control_frame, self.opponent_pokemon_var, *pokemon_names_sorted)
        opponent_pokemon_menu.config(font=self.label_font, bg="#f8ffa0", fg="#343a40", relief=tk.GROOVE, bd=2) # Slightly different background for opponent dropdown
        opponent_pokemon_menu["menu"].config(font=self.label_font, bg="#f8fa90", fg="#343a40")
        opponent_pokemon_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")


        # Find Opponents Button
        find_button = tk.Button(control_frame, text="Analyze Matchup", command=self._analyze_matchup,
                                font=self.button_font, bg="#00a8e8", fg="white",
                                relief=tk.RAISED, bd=3, padx=20, pady=10)
        find_button.grid(row=2, column=0, columnspan=2, pady=15) # Row changed for new dropdown

        # Music Controls (Row changed to 3)
        music_frame = tk.Frame(control_frame, bg="#396c8d")
        music_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        self.play_music_button = tk.Button(music_frame, text="▶ Play Battle Theme", command=self._play_music,
                                           font=self.label_font, bg="#f5cd2d", fg="#333",
                                           relief=tk.RAISED, bd=2, padx=10, pady=5,
                                           state=tk.NORMAL if _pygame_available else tk.DISABLED)
        self.play_music_button.pack(side=tk.LEFT, padx=5)

        self.stop_music_button = tk.Button(music_frame, text="■ Stop Battle Theme", command=self._stop_music,
                                          font=self.label_font, bg="#e84a4a", fg="white",
                                          relief=tk.RAISED, bd=2, padx=10, pady=5,
                                          state=tk.DISABLED)
        self.stop_music_button.pack(side=tk.LEFT, padx=5)

        # --- Results Frame ---
        results_frame = tk.Frame(self.master, bg="#f8f9fa", bd=4, relief=tk.SUNKEN, padx=20, pady=15)
        results_frame.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1) # ScrolledText area expands

        tk.Label(results_frame, text="Matchup Analysis:", font=self.header_font, fg="#2a4d69", bg="#f8f9fa").grid(row=0, column=0, pady=(5, 10))

        self.results_text_area = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, width=60, height=15,
                                                           font=self.text_area_font, bg="white", fg="#343a40",
                                                           relief=tk.FLAT, bd=0, padx=10, pady=10)
        self.results_text_area.grid(row=1, column=0, sticky="nsew")
        self.results_text_area.config(state=tk.DISABLED) # Make read-only by default

        # Clear Button
        clear_button = tk.Button(results_frame, text="Clear Results", command=self._clear_results,
                                font=self.button_font, bg="#6c757d", fg="white",
                                relief=tk.RAISED, bd=3, padx=15, pady=8)
        clear_button.grid(row=2, column=0, pady=15)

    def _load_music(self):
        """Loads the music file if pygame is available."""
        # The status label needs to be created before it's used here.
        # Let's add it to the main window grid, or ensure it's created consistently.
        self.status_label = tk.Label(self.master, text="",
                                        font=self.label_font, fg="#90ee90", bg="#2a4d69")
        self.status_label.grid(row=3, column=0, pady=(5,0), sticky="s") # Placed at grid row 3

        if not _pygame_available:
            self.status_label.config(text="Pygame not found. Music disabled.", fg="red")
            return

        if not os.path.exists(MUSIC_FILE):
            self.status_label.config(text=f"Music file '{MUSIC_FILE}' not found. Please add it to the same folder.", fg="red")
            self.play_music_button.config(state=tk.DISABLED)
            return

        try:
            pygame.mixer.music.load(MUSIC_FILE)
            self.status_label.config(text=f"Music '{MUSIC_FILE}' loaded.")
        except pygame.error as e:
            self.status_label.config(text=f"Error loading music: {e}. Check file format.", fg="red")
            self.play_music_button.config(state=tk.DISABLED)

    def _play_music(self):
        """Plays the loaded music."""
        if not _pygame_available:
            return

        # Stop music first if already playing, to reset the timer for the 5-second play
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        try:
            pygame.mixer.music.play(-1) # -1 means loop indefinitely
            self.play_music_button.config(state=tk.DISABLED)
            self.stop_music_button.config(state=tk.NORMAL)
            self.status_label.config(text="Battle theme playing 🎶", fg="#90ee90")
        except pygame.error as e:
            self.status_label.config(text=f"Error playing music: {e}.", fg="red")
            self.play_music_button.config(state=tk.NORMAL)
            self.stop_music_button.config(state=tk.DISABLED)
        # Schedule the music to stop after 5 seconds
        self.master.after(5000, self._stop_music)

    def _stop_music(self):
        """Stops the currently playing music."""
        if _pygame_available and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.play_music_button.config(state=tk.NORMAL)
            self.stop_music_button.config(state=tk.DISABLED)
            self.status_label.config(text="Battle theme stopped.", fg="gray")

    def _calculate_type_effectiveness(self, attacking_type, defending_types):
        """
        Calculates the combined effectiveness of a single attacking type against
        one or two defending types.
        """
        multiplier = 1.0
        for d_type in defending_types:
            multiplier *= TYPE_CHART.get(attacking_type, {}).get(d_type, 1.0)
        return multiplier

    def _analyze_matchup(self):
        """
        Analyzes the specific matchup between the selected 'Your Pokémon'
        and 'Target Opponent Pokémon' with more detailed explanations.
        """
        self.results_text_area.config(state=tk.NORMAL) # Enable editing
        self.results_text_area.delete(1.0, tk.END) # Clear previous results

        your_pokemon_name = self.your_pokemon_var.get()
        opponent_pokemon_name = self.opponent_pokemon_var.get()

        if your_pokemon_name == "Select Pokémon":
            messagebox.showwarning("Input Error", "Please select Your Pokémon!")
            self.results_text_area.config(state=tk.DISABLED)
            return
        if opponent_pokemon_name == "Select Pokémon":
            messagebox.showwarning("Input Error", "Please select a Target Opponent Pokémon!")
            self.results_text_area.config(state=tk.DISABLED)
            return
        if your_pokemon_name == opponent_pokemon_name:
            messagebox.showwarning("Input Error", "Your Pokémon and the Target Opponent cannot be the same!")
            self.results_text_area.config(state=tk.DISABLED)
            return

        your_pokemon_types = POKEMON_DATA.get(your_pokemon_name, [])
        opponent_pokemon_types = POKEMON_DATA.get(opponent_pokemon_name, [])

        if not your_pokemon_types or not opponent_pokemon_types:
            messagebox.showerror("Data Error", "Could not find type data for selected Pokémon. Please try again.")
            self.results_text_area.config(state=tk.DISABLED)
            return

        # Start music when analysis begins, and schedule its stop
        self._play_music() # This method now includes the 5-second timer

        output_text = f"--- Matchup Analysis: {your_pokemon_name} vs. {opponent_pokemon_name} ---\n\n"
        output_text += f"Your Pokémon: {your_pokemon_name} ({' / '.join(your_pokemon_types)})\n"
        output_text += f"Opponent Pokémon: {opponent_pokemon_name} ({' / '.join(opponent_pokemon_types)})\n\n"

        # --- Your Pokémon's Offensive Capability ---
        output_text += f"--- 📊 {your_pokemon_name}'s Offensive Analysis ---\n"
        overall_your_offensive_multiplier = 0.0 # Will store the max effectiveness
        your_offensive_details = []

        for your_atk_type in your_pokemon_types:
            effectiveness_against_opponent = self._calculate_type_effectiveness(your_atk_type, opponent_pokemon_types)
            overall_your_offensive_multiplier = max(overall_your_offensive_multiplier, effectiveness_against_opponent)

            detail_line = f"  • If {your_pokemon_name} uses a {your_atk_type}-type attack:"
            if effectiveness_against_opponent == 0.0:
                detail_line += f" NO EFFECT! ({opponent_pokemon_name} is immune to {your_atk_type})."
            elif effectiveness_against_opponent < 1.0:
                detail_line += f" NOT VERY EFFECTIVE ({effectiveness_against_opponent:.1f}x damage)."
            elif effectiveness_against_opponent > 1.0:
                detail_line += f" SUPER EFFECTIVE ({effectiveness_against_opponent:.1f}x damage)!"
            else:
                detail_line += f" Normal Effectiveness ({effectiveness_against_opponent:.1f}x damage)."
            your_offensive_details.append(detail_line)

        output_text += "\n".join(your_offensive_details) + "\n\n"
        output_text += f"Overall, {your_pokemon_name} will deal {overall_your_offensive_multiplier:.1f}x damage (best case).\n\n"

        # --- Opponent Pokémon's Offensive Capability (Threat to You) ---
        output_text += f"--- 🚨 {opponent_pokemon_name}'s Offensive Threat (to {your_pokemon_name}) ---\n"
        overall_opponent_offensive_multiplier = 0.0 # Will store the max effectiveness
        opponent_offensive_details = []

        for opp_atk_type in opponent_pokemon_types:
            effectiveness_against_you = self._calculate_type_effectiveness(opp_atk_type, your_pokemon_types)
            overall_opponent_offensive_multiplier = max(overall_opponent_offensive_multiplier, effectiveness_against_you)

            detail_line = f"  • If {opponent_pokemon_name} uses a {opp_atk_type}-type attack:"
            if effectiveness_against_you == 0.0:
                detail_line += f" You are IMMUNE! ({your_pokemon_name} takes 0x from {opp_atk_type})."
            elif effectiveness_against_you < 1.0:
                detail_line += f" You RESIST ({effectiveness_against_you:.1f}x damage taken)."
            elif effectiveness_against_you > 1.0:
                detail_line += f" You are VULNERABLE ({effectiveness_against_you:.1f}x damage taken)!"
            else:
                detail_line += f" Normal damage taken ({effectiveness_against_you:.1f}x damage taken)."
            opponent_offensive_details.append(detail_line)

        output_text += "\n".join(opponent_offensive_details) + "\n\n"
        output_text += f"Overall, {your_pokemon_name} will take {overall_opponent_offensive_multiplier:.1f}x damage (worst case).\n\n"


        # --- Overall Matchup Summary ---
        output_text += "--- ⭐ Overall Matchup Summary ⭐ ---\n"
        if overall_your_offensive_multiplier >= 2.0 and overall_opponent_offensive_multiplier <= 0.5:
            output_text += "🌟 This is a VERY FAVORABLE matchup for you! You hit hard, they hit weakly.\n"
        elif overall_your_offensive_multiplier >= 2.0 and overall_opponent_offensive_multiplier >= 2.0:
            output_text += "🔥 This is a highly OFFENSIVE matchup. You hit hard, but they hit hard too! Be careful!\n"
        elif overall_your_offensive_multiplier <= 0.5 and overall_opponent_offensive_multiplier >= 2.0:
            output_text += "🚨 This is a VERY UNFAVORABLE matchup for you! You hit weakly, and they hit hard. Consider switching!\n"
        elif overall_your_offensive_multiplier == 0.0:
            output_text += "🚫 You cannot damage them at all. This is a bad matchup offensively, retreat!\n"
        elif overall_opponent_offensive_multiplier == 0.0:
            output_text += "✨ You are immune to their attacks, giving you a huge advantage!\n"
        else:
            output_text += "🤝 This matchup is relatively balanced, or presents moderate advantages/disadvantages. Strategy is key!\n"


        self.results_text_area.insert(tk.END, output_text)
        self.results_text_area.config(state=tk.DISABLED) # Make read-only again

    def _clear_results(self):
        """Clears the results text area and resets type selections."""
        self.results_text_area.config(state=tk.NORMAL)
        self.results_text_area.delete(1.0, tk.END)
        self.results_text_area.config(state=tk.DISABLED)
        self.your_pokemon_var.set("Select Pokémon") # Reset to default Pokémon
        self.opponent_pokemon_var.set("Select Pokémon") # Reset opponent dropdown
        if _pygame_available and pygame.mixer.music.get_busy():
            self._stop_music() # Stop music if playing when clearing

# --- Main Application Execution ---

def main():
    """Initializes and runs the Tkinter Pokémon Opponent App."""
    if not _tkinter_available:
        print("tkinter is not available. Please install it to run this GUI application.")
        sys.exit(1) # Exit if Tkinter is missing

    root = tk.Tk()
    app = PokemonOpponentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()