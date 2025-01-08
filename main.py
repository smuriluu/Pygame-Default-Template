import pygame
from scripts.screen import Screen
from scripts.settings import Settings
from scripts.menu import Menu

class Main():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = Screen(self.settings)
        self.running = True
        # Set initial game state to 'menu'.
        self.game_state = 'menu'
        # Create an instance of the Menu class, passing the current Game instance as an argument.
        self.menu = Menu(self)
    
    def run(self):
        while self.running:
            # Calculate the time elapsed since the last frame (delta time).
            self.screen.delta_time()
            # Handle user input and update the game state.
            self.controller()
            # Update the screen.
            self.screen.screen_update()
        pygame.quit()
    
    # Define a method to handle user input and update the game state.
    def controller(self):
        # If the current game state is 'menu', run the menu.
        if self.game_state == 'menu':
            self.menu.run()

if __name__ == '__main__':
    Main().run()
