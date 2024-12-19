from game.manager import GameManager
from game.controller import GameController
from game.ui import GameUI


class GameComponentFactory:
    """
    A factory class for creating game components.

    This class provides static methods to create and initialize
    instances of the main game components, including:

    - GameManager: Manages the overall game state and logic.
    - GameController: Handles game interactions and connects to the manager.
    - GameUI: Manages the game's user interface.
    """

    @staticmethod
    def create_manager():
        """Creates and returns an instance of GameManager."""
        return GameManager()

    @staticmethod
    def create_controller(manager: GameManager):
        """Creates and returns an instance
          of GameController, assigning the provided game manager."""
        return GameController(manager)

    @staticmethod
    def create_ui(controller: GameController):
        """Creates and returns an instance
          of GameUI, assigning the provided game controller."""
        return GameUI(controller)
