# 🎮 Pygame Default Template

This repository contains a default template for projects developed with Pygame. The goal of this template is to provide a solid and modular base for game development, allowing you to focus on the specific mechanics of the game without needing to redo essential logic, such as screen resizing, game state management, and data persistence.

---

## 🚀 Key Features

### 🛠️ Modularity
- **Flexible Components**: Easily replace or modify individual parts like the menu system, sprite management, and settings control.

### 💾 Data Persistence
- **Player Preferences**: Automatically save and load settings such as screen resolution, audio volume, language, and player data (e.g., playtime, high scores) in a JSON file.

### 🎮 Game State Management
- **Smooth Navigation**: A prebuilt structure to handle different game states such as menus, levels, and pauses.

### 🖥️ Screen Resizing
- **Dynamic Adjustments**: Integrated logic to adjust resolution and aspect ratio based on player preferences.

### 🌍 Multilingual Support
- **Global Reach**: Easily add new translations to the game by updating the JSON settings file.

---

## 📂 Project Structure

```plaintext
Pygame-Default-Template/
│
├── config/
│ └── settings.json # Game settings file (resolution, audio, language, etc.)
│
├── images/ # Directory to store sprites and other graphics
│
├── scripts/
│ └── menu.py # Main menu implementation
│ └── screen.py # Screen management and resizing
│ └── settings.py # Loading and saving settings
│ └── sprites.py # Sprite loading
│ └── text.py # Text management
└── main.py # Main script to start the game
```

---

## ⚙️ Settings

Game settings are stored in the config/settings.json file.
This file allows customization of various options, such as:

- Screen Resolution
- Language
- Audio Volume
- Key Mappings

Example settings.json file:

```json
{
    "video": {
        "width": 1280,
        "height": 720,
        "fps": 0,
        "vsync": 0,
        "show_fps": true
    },
    "audio": {
        "main_volume": 0
    },
    "game_data": {
        "times_played": 0,
        "high_score": 0,
        "max_enemies_defeated": 0
    }
}
```

---

## 🛠️ Requirements

Make sure you have Pygame Community Edition installed.
Install it using the following command:

```bash
pip install pygame-ce
```

---

## 🖥️ How to Run the Project

- Clone this repository:

```bash
git clone https://github.com/your-username/pygame-default-template.git
cd pygame-default-template
```

- Install the required dependencies:

```bash
pip install pygame-ce
```

- Run the game:

```bash
python main.py
```