# 🎮 Pygame Default Template

## A modular, scalable starting point for building Pygame games.

Created for my personal use, this template may also serve as a helpful foundation—especially for beginners—when organizing a Pygame project.

---

## 📂 Project Structure
```plaintext
Pygame-Default-Template/
├── canvas/
│   └── menu.py            # Game states (menu, options, gameplay, etc.)
│
├── config/
│   └── settings.json      # Persistent settings (audio, video, language, game data, controls)
│
├── scripts/
│   ├── basics/
│   │   ├── assets.py      # Sprite loading, sprite groups, and animation helpers
│   │   ├── screen.py      # Window management: resizing, delta time, FPS handling
│   │   ├── settings.py    # Reading and updating `settings.json`
│   │   └── gui.py         # GUI components: Label, Button, Slider, TextBox, etc.
│   │
│   └── objects/
│       └── map.py         # `.tmx` map loading (via pytmx) and collision sprites
│
└── main.py                # Game entry point: main loop and state management
```

---

## ⚙️ Features

- Game States: Each screen (menu, options, gameplay) is a separate module in canvas/.

- JSON-based Settings: Store and persist video, audio, language, game data, and key mappings in config/settings.json.

- Dynamic Window Resizing: Change resolution, VSync, and fullscreen at runtime.

- Reusable GUI Components: Buttons, sliders, text boxes, and basic UI helpers.

- Asset Management: Load static and animated sprites via scripts/basics/assets.py.

- TMX Map Integration: Import tile maps with pytmx and generate sprite layers.

---

## 🛠️ Dependencies:

Make sure you have Pygame Community Edition and pytmx installed.
Install it using the following command:

```bash
pip install pygame-ce pytmx
```

---

## 🖥️ How to Run

- Clone this repository:

```bash
git clone https://github.com/your-username/pygame-default-template.git
cd pygame-default-template
```

- Install the required dependencies:

- Start the game:

```bash
python3 main.py
```

---

## 🔧 Customization

- Add a New Screen: Create a script in canvas/ with a run() method, then instantiate it in Main().

- New Assets: Place image files in an images/ folder and use Assets.load_sprite() or Assets.animated_sprites().

- Adjust Settings: Edit config/settings.json, or call Settings.set_settings() at runtime to update and persist values.

---

## 📄 License

Free to use for educational and commercial purposes. Provided without any warranty.

---

This template was created for my personal workflow but may be useful for organizing your Pygame projects.
