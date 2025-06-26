"""
Team Builder Window for the Pokémon Advisor.
This module provides a GUI for building and analyzing teams.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import tkinter.font as tkfont

from ..data.pokemon_data import POKEMON_DATA
from ..utils.team_builder import TeamBuilder


class TeamBuilderWindow:
    """Team Builder window for creating and analyzing Pokémon teams."""
    
    def __init__(self, parent):
        """
        Initialize the Team Builder window.
        
        Args:
            parent: The parent window
        """
        self.parent = parent
        self.team_builder = TeamBuilder()
        
        # Create the window
        self.window = tk.Toplevel(parent)
        self.window.title("Team Builder - Pokémon Advisor")
        self.window.geometry("1000x800")
        self.window.resizable(True, True)
        self.window.configure(bg="#2a4d69")
        
        # Center the window
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.window.geometry(f'+{x}+{y}')
        
        self._setup_fonts()
        self._create_widgets()
        self._update_team_display()
    
    def _setup_fonts(self):
        """Setup custom fonts for the window."""
        try:
            self.title_font = tkfont.Font(family="Arial", size=20, weight="bold")
            self.header_font = tkfont.Font(family="Arial", size=14, weight="bold")
            self.label_font = tkfont.Font(family="Arial", size=11)
            self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")
            self.text_font = tkfont.Font(family="Courier New", size=10)
        except Exception:
            self.title_font = ("TkDefaultFont", 20, "bold")
            self.header_font = ("TkDefaultFont", 14, "bold")
            self.label_font = ("TkDefaultFont", 11)
            self.button_font = ("TkDefaultFont", 12, "bold")
            self.text_font = ("TkFixedFont", 10)
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Title
        title_label = tk.Label(
            self.window,
            text="Team Builder",
            font=self.title_font,
            fg="#ffc107",
            bg="#2a4d69"
        )
        title_label.pack(pady=10)
        
        # Main container
        main_frame = tk.Frame(self.window, bg="#2a4d69")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Team Management
        self._create_team_management_panel(main_frame)
        
        # Right panel - Analysis
        self._create_analysis_panel(main_frame)
    
    def _create_team_management_panel(self, parent):
        """Create the team management panel."""
        team_frame = tk.LabelFrame(
            parent,
            text="Team Management",
            font=self.header_font,
            fg="black",
            bg="#396c8d",
            bd=3,
            relief=tk.RAISED
        )
        team_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Pokémon selection
        selection_frame = tk.Frame(team_frame, bg="#396c8d")
        selection_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            selection_frame,
            text="Add Pokémon:",
            font=self.label_font,
            bg="#396c8d",
            fg="black"
        ).pack(anchor=tk.W)
        
        # Pokémon dropdown
        pokemon_names = sorted(list(POKEMON_DATA.keys()))
        self.pokemon_var = tk.StringVar()
        self.pokemon_var.set(pokemon_names[0])
        
        self.pokemon_dropdown = ttk.Combobox(
            selection_frame,
            textvariable=self.pokemon_var,
            values=pokemon_names,
            font=self.label_font,
            state="readonly"
        )
        self.pokemon_dropdown.pack(fill=tk.X, pady=5)
        
        # Add button
        add_button = tk.Button(
            selection_frame,
            text="Add to Team",
            command=self._add_pokemon,
            font=self.button_font,
            bg="#28a745",
            fg="black",
            relief=tk.RAISED,
            bd=2
        )
        add_button.pack(pady=5)
        
        # Team display
        team_display_frame = tk.Frame(team_frame, bg="#396c8d")
        team_display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(
            team_display_frame,
            text="Current Team:",
            font=self.header_font,
            bg="#396c8d",
            fg="black"
        ).pack(anchor=tk.W)
        
        # Team listbox
        self.team_listbox = tk.Listbox(
            team_display_frame,
            font=self.text_font,
            bg="white",
            fg="black",
            selectmode=tk.SINGLE,
            height=8
        )
        self.team_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Team control buttons
        button_frame = tk.Frame(team_display_frame, bg="#396c8d")
        button_frame.pack(fill=tk.X, pady=5)
        
        remove_button = tk.Button(
            button_frame,
            text="Remove Selected",
            command=self._remove_pokemon,
            font=self.button_font,
            bg="#dc3545",
            fg="black",
            relief=tk.RAISED,
            bd=2
        )
        remove_button.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_button = tk.Button(
            button_frame,
            text="Clear Team",
            command=self._clear_team,
            font=self.button_font,
            bg="#6c757d",
            fg="black",
            relief=tk.RAISED,
            bd=2
        )
        clear_button.pack(side=tk.LEFT)
        
        # Suggestions
        suggestions_frame = tk.Frame(team_frame, bg="#396c8d")
        suggestions_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            suggestions_frame,
            text="Suggestions:",
            font=self.header_font,
            bg="#396c8d",
            fg="black"
        ).pack(anchor=tk.W)
        
        self.suggestions_text = scrolledtext.ScrolledText(
            suggestions_frame,
            font=self.text_font,
            bg="white",
            fg="black",
            height=4,
            wrap=tk.WORD
        )
        self.suggestions_text.pack(fill=tk.X, pady=5)
        
        suggest_button = tk.Button(
            suggestions_frame,
            text="Get Suggestions",
            command=self._get_suggestions,
            font=self.button_font,
            bg="#17a2b8",
            fg="black",
            relief=tk.RAISED,
            bd=2
        )
        suggest_button.pack(pady=5)
    
    def _create_analysis_panel(self, parent):
        """Create the team analysis panel."""
        analysis_frame = tk.LabelFrame(
            parent,
            text="Team Analysis",
            font=self.header_font,
            fg="black",
            bg="#396c8d",
            bd=3,
            relief=tk.RAISED
        )
        analysis_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Analysis button
        analyze_button = tk.Button(
            analysis_frame,
            text="Analyze Team",
            command=self._analyze_team,
            font=self.button_font,
            bg="#ffc107",
            fg="black",
            relief=tk.RAISED,
            bd=2
        )
        analyze_button.pack(pady=10)
        
        # Analysis display
        self.analysis_text = scrolledtext.ScrolledText(
            analysis_frame,
            font=self.text_font,
            bg="white",
            fg="black",
            wrap=tk.WORD
        )
        self.analysis_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def _add_pokemon(self):
        """Add a Pokémon to the team."""
        pokemon_name = self.pokemon_var.get()
        success, message = self.team_builder.add_pokemon(pokemon_name)
        
        if success:
            self._update_team_display()
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
    
    def _remove_pokemon(self):
        """Remove the selected Pokémon from the team."""
        selection = self.team_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a Pokémon to remove.")
            return
        
        index = selection[0]
        team = self.team_builder.get_team()
        if index < len(team):
            pokemon_name = team[index]['name']
            success, message = self.team_builder.remove_pokemon(pokemon_name)
            if success:
                self._update_team_display()
                messagebox.showinfo("Success", message)
    
    def _clear_team(self):
        """Clear the entire team."""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the entire team?"):
            success, message = self.team_builder.clear_team()
            if success:
                self._update_team_display()
                messagebox.showinfo("Success", message)
    
    def _update_team_display(self):
        """Update the team display."""
        self.team_listbox.delete(0, tk.END)
        team = self.team_builder.get_team()
        
        for i, pokemon in enumerate(team, 1):
            types_str = " / ".join(pokemon['types'])
            self.team_listbox.insert(tk.END, f"{i}. {pokemon['name']} ({types_str})")
        
        # Update team size indicator
        team_size = len(team)
        if team_size == 6:
            self.team_listbox.insert(tk.END, "\n✅ Team Complete!")
        else:
            self.team_listbox.insert(tk.END, f"\n📝 {6 - team_size} Pokémon needed")
    
    def _get_suggestions(self):
        """Get suggestions for the current team."""
        suggestions = self.team_builder.suggest_pokemon()
        
        if not suggestions:
            self.suggestions_text.delete(1.0, tk.END)
            self.suggestions_text.insert(tk.END, "No suggestions available.")
            return
        
        self.suggestions_text.delete(1.0, tk.END)
        self.suggestions_text.insert(tk.END, "Suggested Pokémon to add:\n\n")
        
        for i, suggestion in enumerate(suggestions, 1):
            types = POKEMON_DATA.get(suggestion, [])
            types_str = " / ".join(types)
            self.suggestions_text.insert(tk.END, f"{i}. {suggestion} ({types_str})\n")
    
    def _analyze_team(self):
        """Analyze the current team."""
        analysis = self.team_builder.analyze_team()
        
        if analysis.get('status') == 'empty':
            messagebox.showwarning("Warning", "No Pokémon in team to analyze.")
            return
        
        self.analysis_text.delete(1.0, tk.END)
        output = self._format_team_analysis(analysis)
        self.analysis_text.insert(tk.END, output)
    
    def _format_team_analysis(self, analysis):
        """Format the team analysis for display."""
        output = f"=== TEAM ANALYSIS ===\n\n"
        output += f"Team Size: {analysis['team_size']}/6 Pokémon\n"
        output += f"Team Members: {', '.join(analysis['pokemon_list'])}\n\n"
        
        # Type Analysis
        type_analysis = analysis['type_analysis']
        output += f"=== TYPE ANALYSIS ===\n"
        output += f"Diversity Rating: {type_analysis['diversity_rating']}\n"
        output += f"Unique Types: {type_analysis['unique_types']}/18\n"
        output += f"Diversity Score: {type_analysis['diversity_score']:.2f}\n\n"
        
        output += "Type Distribution:\n"
        for pokemon_type, count in type_analysis['type_distribution'].items():
            output += f"  {pokemon_type}: {count}\n"
        output += "\n"
        
        output += "Type Combinations:\n"
        for combo in type_analysis['type_combinations']:
            output += f"  {combo}\n"
        output += "\n"
        
        # Coverage Analysis
        coverage_analysis = analysis['coverage_analysis']
        output += f"=== COVERAGE ANALYSIS ===\n"
        output += f"Coverage Score: {coverage_analysis['coverage_score']:.2f}\n"
        output += f"Excellent Coverage: {len(coverage_analysis['excellent_coverage'])} types\n"
        
        if coverage_analysis['excellent_coverage']:
            output += f"  Types: {', '.join(coverage_analysis['excellent_coverage'])}\n"
        
        if coverage_analysis['coverage_gaps']:
            output += f"Coverage Gaps: {len(coverage_analysis['coverage_gaps'])} types\n"
            output += f"  Types: {', '.join(coverage_analysis['coverage_gaps'][:5])}\n"
        output += "\n"
        
        # Weakness Analysis
        weakness_analysis = analysis['weakness_analysis']
        output += f"=== WEAKNESS ANALYSIS ===\n"
        output += f"Weakness Score: {weakness_analysis['weakness_score']:.2f}\n"
        
        if weakness_analysis['critical_weaknesses']:
            output += f"Critical Weaknesses:\n"
            for weak_type, pokemon in weakness_analysis['critical_weaknesses'].items():
                output += f"  {weak_type}: {', '.join(pokemon)}\n"
        
        if weakness_analysis['defensive_gaps']:
            output += f"Defensive Gaps: {', '.join(weakness_analysis['defensive_gaps'][:5])}\n"
        output += "\n"
        
        # Synergy Analysis
        synergy_analysis = analysis['synergy_analysis']
        output += f"=== SYNERGY ANALYSIS ===\n"
        output += f"Overall Synergy: {synergy_analysis['overall_synergy']}\n\n"
        
        if synergy_analysis['synergy_pairs']:
            output += f"Strong Synergy Pairs:\n"
            for pair in synergy_analysis['synergy_pairs'][:3]:
                output += f"  {pair['pokemon1']} + {pair['pokemon2']} (Score: {pair['score']:.2f})\n"
                output += f"    Reason: {pair['reason']}\n"
        
        if synergy_analysis['anti_synergy_pairs']:
            output += f"\nWeak Synergy Pairs:\n"
            for pair in synergy_analysis['anti_synergy_pairs'][:3]:
                output += f"  {pair['pokemon1']} + {pair['pokemon2']} (Score: {pair['score']:.2f})\n"
                output += f"    Reason: {pair['reason']}\n"
        output += "\n"
        
        # Recommendations
        output += f"=== RECOMMENDATIONS ===\n"
        for i, rec in enumerate(analysis['recommendations'], 1):
            output += f"{i}. {rec}\n"
        
        return output
    
    def show(self):
        """Show the team builder window."""
        self.window.deiconify()
        self.window.focus_force()
    
    def hide(self):
        """Hide the team builder window."""
        self.window.withdraw() 