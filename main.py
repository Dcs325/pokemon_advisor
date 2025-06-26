#!/usr/bin/env python3
"""
Pokémon Opponent Advisor - Main Application Entry Point

A desktop application that helps you find the best Pokémon to use against 
a specific opponent by analyzing type matchups.

This is the main entry point for the modular Pokémon Advisor application.
"""

import os
import sys

# Suppress the Tk deprecation warning on macOS
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Module availability checks
try:
    import tkinter as tk
    _tkinter_available = True
except ImportError:
    _tkinter_available = False
    print("Error: tkinter is not available. Please install tkinter or ensure your Python includes Tcl/Tk.")
    print("If you are on Linux, try: sudo apt-get install python3-tk")
    sys.exit(1)

# Import our modular components
try:
    from src.gui.app_window import PokemonOpponentApp
except ImportError as e:
    print(f"Error importing application modules: {e}")
    print("Make sure you're running this from the project root directory.")
    sys.exit(1)


def main():
    """
    Initialize and run the Pokémon Opponent Advisor application.
    
    This function sets up the main Tkinter window and starts the application.
    """
    if not _tkinter_available:
        print("tkinter is not available. Please install it to run this GUI application.")
        sys.exit(1)
    
    # Create the main window
    root = tk.Tk()
    
    # Initialize the application
    app = PokemonOpponentApp(root)
    
    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main() 