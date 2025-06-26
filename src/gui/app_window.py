"""
Main application window for the Pokémon Opponent Advisor.
This module contains the Tkinter GUI implementation.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import tkinter.font as tkfont

from ..data.pokemon_data import POKEMON_DATA
from ..utils.type_calculator import analyze_matchup
from ..utils.music_manager import MusicManager


class PokemonOpponentApp:
    """Main application window for the Pokémon Opponent Advisor."""
    
    def __init__(self, master):
        """
        Initialize the application window.
        
        Args:
            master: The root Tkinter window
        """
        self.master = master
        self.music_manager = MusicManager()
        
        self._setup_window()
        self._setup_fonts()
        self._create_widgets()
    
    def _setup_window(self):
        """Configure the main application window."""
        self.master.title("Pokémon Opponent Recommender")
        self.master.geometry("750x780")
        self.master.resizable(True, True)
        self.master.configure(bg="#2a4d69")
        
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
        self.master.rowconfigure(0, weight=0)  # Title
        self.master.rowconfigure(1, weight=0)  # Controls
        self.master.rowconfigure(2, weight=1)  # Results area
    
    def _setup_fonts(self):
        """Configure custom fonts for the application."""
        try:
            self.title_font = tkfont.Font(family="Arial", size=26, weight="bold")
            self.header_font = tkfont.Font(family="Arial", size=16, weight="bold")
            self.label_font = tkfont.Font(family="Arial", size=12)
            self.button_font = tkfont.Font(family="Arial", size=14, weight="bold")
            self.text_area_font = tkfont.Font(family="Courier New", size=12)
        except Exception:
            self.title_font = ("TkDefaultFont", 26, "bold")
            self.header_font = ("TkDefaultFont", 16, "bold")
            self.label_font = ("TkDefaultFont", 12)
            self.button_font = ("TkDefaultFont", 14, "bold")
            self.text_area_font = ("TkFixedFont", 12)
    
    def _create_widgets(self):
        """Create and place all GUI widgets."""
        # Title
        title_label = tk.Label(
            self.master, 
            text="Pokémon Opponent Advisor",
            font=self.title_font, 
            fg="#ffc107", 
            bg="#2a4d69"
        )
        title_label.grid(row=0, column=0, pady=20, sticky="n")
        
        # Control Frame
        self._create_control_frame()
        
        # Results Frame
        self._create_results_frame()
    
    def _create_control_frame(self):
        """Create the control frame with user inputs."""
        control_frame = tk.Frame(
            self.master, 
            bg="#396c8d", 
            bd=4, 
            relief=tk.RAISED, 
            padx=20, 
            pady=20
        )
        control_frame.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        control_frame.columnconfigure(0, weight=1)
        control_frame.columnconfigure(1, weight=1)
        
        # Your Pokémon Selection
        tk.Label(
            control_frame, 
            text="Select Your Pokémon:", 
            font=self.label_font, 
            bg="#396c8d", 
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.your_pokemon_var = tk.StringVar(self.master)
        pokemon_names_sorted = sorted(list(POKEMON_DATA.keys()))
        self.your_pokemon_var.set(pokemon_names_sorted[0])
        
        your_pokemon_menu = tk.OptionMenu(
            control_frame, 
            self.your_pokemon_var, 
            *pokemon_names_sorted
        )
        your_pokemon_menu.config(
            font=self.label_font, 
            bg="#f8f9fa", 
            fg="#343a40", 
            relief=tk.GROOVE, 
            bd=2
        )
        your_pokemon_menu["menu"].config(
            font=self.label_font, 
            bg="#f8f9fa", 
            fg="#343a40"
        )
        your_pokemon_menu.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Target Opponent Selection
        tk.Label(
            control_frame, 
            text="Select Target Opponent:", 
            font=self.label_font, 
            bg="#396c8d", 
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.opponent_pokemon_var = tk.StringVar(self.master)
        self.opponent_pokemon_var.set(pokemon_names_sorted[0])
        
        opponent_pokemon_menu = tk.OptionMenu(
            control_frame, 
            self.opponent_pokemon_var, 
            *pokemon_names_sorted
        )
        opponent_pokemon_menu.config(
            font=self.label_font, 
            bg="#f8ffa0", 
            fg="#343a40", 
            relief=tk.GROOVE, 
            bd=2
        )
        opponent_pokemon_menu["menu"].config(
            font=self.label_font, 
            bg="#f8fa90", 
            fg="#343a40"
        )
        opponent_pokemon_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Analyze Button
        find_button = tk.Button(
            control_frame, 
            text="Analyze Matchup", 
            command=self._analyze_matchup,
            font=self.button_font, 
            bg="#00a8e8", 
            fg="black",
            relief=tk.RAISED, 
            bd=3, 
            padx=20, 
            pady=10
        )
        find_button.grid(row=2, column=0, columnspan=2, pady=15)
    
    def _create_results_frame(self):
        """Create the results display frame."""
        results_frame = tk.Frame(
            self.master, 
            bg="#f8f9fa", 
            bd=4, 
            relief=tk.SUNKEN, 
            padx=20, 
            pady=15
        )
        results_frame.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)
        
        tk.Label(
            results_frame, 
            text="Matchup Analysis:", 
            font=self.header_font, 
            fg="#2a4d69", 
            bg="#f8f9fa"
        ).grid(row=0, column=0, pady=(5, 10))
        
        self.results_text_area = scrolledtext.ScrolledText(
            results_frame, 
            wrap=tk.WORD, 
            width=60, 
            height=15,
            font=self.text_area_font, 
            bg="white", 
            fg="#343a40",
            relief=tk.FLAT, 
            bd=0, 
            padx=10, 
            pady=10
        )
        self.results_text_area.grid(row=1, column=0, sticky="nsew")
        self.results_text_area.config(state=tk.DISABLED)
    
    def _analyze_matchup(self):
        """Analyze the matchup between selected Pokémon."""
        self.results_text_area.config(state=tk.NORMAL)
        self.results_text_area.delete(1.0, tk.END)
        
        your_pokemon_name = self.your_pokemon_var.get()
        opponent_pokemon_name = self.opponent_pokemon_var.get()
        
        # Validate inputs
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
        
        # Analyze matchup
        analysis = analyze_matchup(your_pokemon_name, opponent_pokemon_name, POKEMON_DATA)
        
        if analysis is None:
            messagebox.showerror("Data Error", "Could not find type data for selected Pokémon. Please try again.")
            self.results_text_area.config(state=tk.DISABLED)
            return
        
        # Play battle sound during analysis
        self._play_battle_sound()
        
        # Generate output
        output_text = self._format_analysis_output(analysis)
        
        self.results_text_area.insert(tk.END, output_text)
        self.results_text_area.config(state=tk.DISABLED)
    
    def _format_analysis_output(self, analysis):
        """Format the analysis results for display."""
        your_pokemon = analysis['your_pokemon']
        opponent_pokemon = analysis['opponent_pokemon']
        
        output_text = f"--- Matchup Analysis: {your_pokemon['name']} vs. {opponent_pokemon['name']} ---\n\n"
        output_text += f"Your Pokémon: {your_pokemon['name']} ({' / '.join(your_pokemon['types'])})\n"
        output_text += f"Opponent Pokémon: {opponent_pokemon['name']} ({' / '.join(opponent_pokemon['types'])})\n\n"
        
        # Your Pokémon's Offensive Analysis
        output_text += f"--- 📊 {your_pokemon['name']}'s Offensive Analysis ---\n"
        for detail in your_pokemon['offensive_details']:
            output_text += f"  • If {your_pokemon['name']} uses a {detail['type']}-type attack: {detail['description']}\n"
        output_text += f"\nOverall, {your_pokemon['name']} will deal {your_pokemon['offensive_multiplier']:.1f}x damage (best case).\n\n"
        
        # Opponent Pokémon's Offensive Threat
        output_text += f"--- 🚨 {opponent_pokemon['name']}'s Offensive Threat (to {your_pokemon['name']}) ---\n"
        for detail in opponent_pokemon['offensive_details']:
            output_text += f"  • If {opponent_pokemon['name']} uses a {detail['type']}-type attack: {detail['description']}\n"
        output_text += f"\nOverall, {your_pokemon['name']} will take {opponent_pokemon['offensive_multiplier']:.1f}x damage (worst case).\n\n"
        
        # Overall Matchup Summary
        output_text += "--- ⭐ Overall Matchup Summary ⭐ ---\n"
        output_text += f"{analysis['matchup_summary']}\n"
        
        return output_text
    
    def _play_battle_sound(self):
        """Play a battle sound during the analysis."""
        if self.music_manager.play_music():
            # Schedule the music to stop after 5 seconds
            self.master.after(5000, self._stop_battle_sound)
    
    def _stop_battle_sound(self):
        """Stop the battle sound."""
        self.music_manager.stop_music() 