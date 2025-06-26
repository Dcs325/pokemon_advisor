# Pokémon Opponent Advisor

A desktop application that helps you find the best Pokémon to use against a specific opponent by analyzing type matchups.

![Screenshot of the app](https://i.imgur.com/your-screenshot.png) <!-- It's a good idea to add a screenshot of your app here! -->

## Features

- **Matchup Analysis:** Select your Pokémon and an opponent to see a detailed breakdown of offensive and defensive type advantages.
- **Extensive Pokémon Database:** Includes Pokémon from multiple generations.
- **Battle Sound Effects:** Plays classic Pokémon battle music during analysis (requires `pygame` and music file).
- **User-Friendly Interface:** Built with Tkinter for a simple and intuitive experience.
- **Modular Architecture:** Clean, maintainable code structure with separated concerns.

## Project Structure

```
pokemon_advisor/
├── main.py                 # Main application entry point
├── app.py                  # Original monolithic file (legacy)
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── pokemon_battle_theme.mp3 # Battle music file (optional)
└── src/                   # Source code directory
    ├── __init__.py
    ├── data/              # Data layer
    │   ├── __init__.py
    │   └── pokemon_data.py # Pokémon and type data
    ├── utils/             # Utility functions
    │   ├── __init__.py
    │   ├── type_calculator.py # Type effectiveness calculations
    │   └── music_manager.py   # Music playback management
    └── gui/               # User interface
        ├── __init__.py
        └── app_window.py  # Main GUI window
```

## How to Run This Project

To run this application on your local machine, you'll need Python 3 installed.

### 1. Clone the Repository

First, clone this repository to your computer:

```bash
git clone https://github.com/Dcs325/pokemon_advisor.git
cd pokemon_advisor
```

### 2. Set Up Virtual Environment (Recommended)

Due to system package management restrictions, it's recommended to use a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

This project uses `pygame` for battle sound effects. Install it using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> **Note:** The application also requires `tkinter`, which is included in most standard Python installations. If you get an error about `tkinter` not being found, you may need to install it separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).

### 4. Add the Music File (Optional)

For the battle sound effects to work, you need to add a music file named `pokemon_battle_theme.mp3` to the main project folder.

**If you don't have the music file:**
- The application will still work perfectly without it
- You'll just miss the battle sound effects during analysis

### 5. Run the Application

Once the dependencies are installed, you can run the app with the following command:

```bash
python3 main.py
```

Now you can select your Pokémon and an opponent to get an instant matchup analysis with battle sounds! 🎵

## Battle Sound Features

- **Automatic Playback:** Battle music starts automatically when you click "Analyze Matchup"
- **5-Second Duration:** Music plays for exactly 5 seconds then stops automatically
- **No Manual Controls:** Seamless integration with the analysis workflow
- **Graceful Fallback:** App works perfectly even without the music file

## Development

### Running the Legacy Version

If you want to run the original monolithic version, use:

```bash
python3 app.py
```

### Code Organization

The application has been refactored into a modular structure:

- **`src/data/`**: Contains all Pokémon and type effectiveness data
- **`src/utils/`**: Contains utility functions for calculations and music management
- **`src/gui/`**: Contains the Tkinter GUI implementation
- **`main.py`**: The new entry point that orchestrates all components

This modular structure makes the code:
- **Maintainable**: Each module has a single responsibility
- **Testable**: Individual components can be tested in isolation
- **Extensible**: New features can be added without modifying existing code
- **Readable**: Clear separation of concerns makes the code easier to understand

### Troubleshooting

**No Battle Sounds:**
- Make sure `pokemon_battle_theme.mp3` is in the project root folder
- Ensure pygame is installed: `pip install pygame`
- Check that your system volume is not muted

**Pygame Installation Issues:**
- Use a virtual environment to avoid system package conflicts
- On macOS, you might need to use `brew install pygame` as an alternative

## Contributing

Feel free to contribute to this project by:
- Adding more Pokémon to the database
- Improving the type effectiveness calculations
- Enhancing the user interface
- Adding new features like move recommendations
- Writing tests for the modular components
- Suggesting new battle sound effects