"""
Music management utilities.
This module handles pygame music functionality for the application.
"""

import os

# Try to import pygame, but don't fail if it's not available
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


class MusicManager:
    """Manages music playback using pygame."""
    
    def __init__(self, music_file="pokemon_battle_theme.mp3"):
        """
        Initialize the music manager.
        
        Args:
            music_file (str): Path to the music file
        """
        self.music_file = music_file
        self.is_available = self._check_pygame_availability()
        self.is_loaded = False
        
        if self.is_available:
            self._load_music()
    
    def _check_pygame_availability(self):
        """Check if pygame is available and initialize mixer."""
        if not PYGAME_AVAILABLE:
            return False
            
        try:
            pygame.mixer.init()
            return True
        except Exception:
            return False
    
    def _load_music(self):
        """Load the music file if it exists."""
        if not self.is_available:
            return False
            
        if not os.path.exists(self.music_file):
            return False
            
        try:
            pygame.mixer.music.load(self.music_file)
            self.is_loaded = True
            return True
        except pygame.error:
            return False
    
    def play_music(self, duration=5):
        """
        Play music for a specified duration.
        
        Args:
            duration (int): Duration in seconds to play music
        """
        if not self.is_available or not self.is_loaded:
            return False
            
        try:
            # Stop music first if already playing
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            
            pygame.mixer.music.play(-1)  # Loop indefinitely
            return True
        except pygame.error:
            return False
    
    def stop_music(self):
        """Stop the currently playing music."""
        if self.is_available and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            return True
        return False
    
    def is_playing(self):
        """Check if music is currently playing."""
        return self.is_available and pygame.mixer.music.get_busy()
    
    def get_status(self):
        """Get the current status of the music manager."""
        if not self.is_available:
            return "Pygame not found. Music disabled."
        elif not self.is_loaded:
            return f"Music file '{self.music_file}' not found."
        elif self.is_playing():
            return "Battle theme playing 🎶"
        else:
            return "Music ready to play." 