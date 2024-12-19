from game.manager import GameManager

class GameController:
    """
    The GameController class manages the logic, state,
    and interactions of the game.

    Responsibilities:
    - Handles user inputs and game events.
    - Manages the game's state and updates as required.
    - Interacts with other components such as the display
      and game objects.
    """
    def __init__(self, manager: GameManager):
        self.manager = manager

    def handle_button_click(self, label):
        if label == "start":
            self.manager.resume()
        elif label == "pause":
            self.manager.pause()
        elif label == "save":
            self.manager.save_state("game_state.json")
            return "Game state saved successfully!"
        elif label == "load":
            self.manager.load_state("game_state.json")
            return "Game state loaded successfully!"
        return ""