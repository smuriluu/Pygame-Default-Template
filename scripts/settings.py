import json
import os

class Settings():
    # Manages Settings stored in a JSON file.
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), '..')
        self.file_path = os.path.join(self.path, 'config', 'settings.json')
        self.settings = self.load_settings()
        self.game_settings()
    
    def load_settings(self):
        # Loads settings from the JSON file and returns a dictionary.
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def game_settings(self):
        # Initializes game settings from the aloaded settings.
        self.video_settings = self.get_settings('video')
        self.audio_settings = self.get_settings('audio')
        self.language = self.get_settings('language')
        self.language_set = self.language['language_set']
        self.game_texts = self.language[self.language_set]
        self.game_data = self.get_settings('game_data')
        self.controls = self.get_settings('keys')
    
    def update_settings(self):
        # Updates the JSON file with the new settings stored in the settings dictionary.
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4, ensure_ascii=False)
        self.game_settings()

    def get_settings(self, key):
        # Returns the value of the setting specified by the key.
        return self.settings.get(key)
    
    def set_settings(self, option, key, value):
        # Sets the value of the setting specified by the key and updates the JSON file.
        self.settings[option][key] = value
        self.update_settings()
