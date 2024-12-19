import numpy as np
import json
from threading import Timer

class GameManager:
    """
    The GameManager class is responsible for handling the main game logic
    and managing the game's state.

    This class uses the Singleton pattern to ensure only one instance
    exists throughout the application. It manages the game state, controls
    the game's flow (e.g., start, pause, resume, stop), and updates the game grid.

    Attributes:
        running (bool): Indicates whether the game is currently running.
        paused (bool): Indicates whether the game is currently paused.
        game_state (np.ndarray): The current state of the game grid, represented
            as a 2D numpy array (0: dead cell, 1: alive cell).
        tick_interval (float): The interval in seconds between game state updates.
        timer (Timer): A Timer object used for scheduling game ticks.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.running = False
        self.paused = True
        self.game_state = np.random.choice([0, 1], size=(40, 30), p=[0.8, 0.2])
        self.tick_interval = 0.5
        self.timer = None

    def start(self):
        self.running = True
        self.paused = False
        self.schedule_tick()

    def pause(self):
        self.paused = True
        if self.timer:
            self.timer.cancel()

    def resume(self):
        self.paused = False
        self.schedule_tick()

    def stop(self):
        self.running = False
        if self.timer:
            self.timer.cancel()

    def schedule_tick(self):
        if not self.paused:
            self.timer = Timer(self.tick_interval, self.tick)
            self.timer.start()

    def tick(self):
        self.update_grid()
        self.schedule_tick()

    def update_grid(self):
        # Logika aktualizacji siatki
        new_state = np.copy(self.game_state)
        n_cells_x, n_cells_y = self.game_state.shape

        for y in range(n_cells_y):
            for x in range(n_cells_x):
                n_neighbors = (
                        self.game_state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] +
                        self.game_state[(x) % n_cells_x, (y - 1) % n_cells_y] +
                        self.game_state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] +
                        self.game_state[(x - 1) % n_cells_x, (y) % n_cells_y] +
                        self.game_state[(x + 1) % n_cells_x, (y) % n_cells_y] +
                        self.game_state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] +
                        self.game_state[(x) % n_cells_x, (y + 1) % n_cells_y] +
                        self.game_state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]
                )

                if self.game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.game_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.game_state = new_state

    def save_state(self, file_name: str):
        with open(file_name, "w") as file:
            data = {
                "game_state": self.game_state.tolist(),
                "tick_interval": self.tick_interval
            }
            json.dump(data, file)

    def load_state(self, file_name: str):
        with open(file_name, "r") as file:
            data = json.load(file)
            self.game_state = np.array(data["game_state"], dtype=int)
            self.tick_interval = data["tick_interval"]

