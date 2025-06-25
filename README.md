# Pokémon Opponent Advisor

A desktop application that helps you find the best Pokémon to use against a specific opponent by analyzing type matchups.

![Screenshot of the app](https://i.imgur.com/your-screenshot.png) <!-- It's a good idea to add a screenshot of your app here! -->

## Features

- **Matchup Analysis:** Select your Pokémon and an opponent to see a detailed breakdown of offensive and defensive type advantages.
- **Extensive Pokémon Database:** Includes Pokémon from multiple generations.
- **Battle Theme Music:** Plays classic Pokémon battle music during analysis (requires `pygame`).
- **User-Friendly Interface:** Built with Tkinter for a simple and intuitive experience.
- **Modular Architecture:** Clean, maintainable code structure with separated concerns.

## Project Structure

```
pokemon_advisor/
├── main.py                 # Main application entry point
├── app.py                  # Original monolithic file (legacy)
├── requirements.txt        # Python dependencies
├── README.md              # This file
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

### 2. Install Dependencies

This project uses `pygame` for music playback. Install it using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> **Note:** The application also requires `tkinter`, which is included in most standard Python installations. If you get an error about `tkinter` not being found, you may need to install it separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).

### 3. Add the Music File (Optional)

For the "Play Battle Theme" button to work, you need to add a music file named `pokemon_battle_theme.mp3` to the main project folder.

### 4. Run the Application

Once the dependencies are installed, you can run the app with the following command:

```bash
python3 main.py
```

Now you can select your Pokémon and an opponent to get an instant matchup analysis!

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

## Contributing

Feel free to contribute to this project by:
- Adding more Pokémon to the database
- Improving the type effectiveness calculations
- Enhancing the user interface
- Adding new features like move recommendations
- Writing tests for the modular components