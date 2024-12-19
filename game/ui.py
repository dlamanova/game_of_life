from game.controller import GameController
from game.constants import COLORS, GRID_SIZE, WINDOW_SIZE
import pygame


class GameUI:
    """
    The GameUI class handles the graphical user interface (GUI) of the game using the Pygame library.

    This class is responsible for rendering the game grid, game cells, buttons, and notifications,
    as well as managing user inputs like button clicks and window events.

    Attributes:
        width (int): Width of the game window.
        height (int): Height of the game window.
        n_cells_x (int): Number of cells along the x-axis (horizontal).
        n_cells_y (int): Number of cells along the y-axis (vertical).
        cell_width (int): Width of an individual cell.
        cell_height (int): Height of an individual cell.
        screen (Surface): The Pygame window surface where the game is drawn.
        colors (dict): Dictionary of color mappings used in the UI (defined in constants.py).
        notification (str): Current notification message to be displayed.
        notification_timer (int): Timer controlling how long the notification is displayed (in frames).
        notification_font (Font): Font used for rendering notification messages.
        controller (GameController): The game controller object managing game state and interactions.
        buttons (dict): Dictionary containing button coordinates and labels.
    """
    def __init__(self, controller: GameController):
        pygame.init()
        self.width, self.height = WINDOW_SIZE
        self.n_cells_x, self.n_cells_y = GRID_SIZE
        self.cell_width = self.width // self.n_cells_x
        self.cell_height = self.height // self.n_cells_y
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.colors = COLORS  # Use COLORS from constants.py
        self.notification = ""
        self.notification_timer = 0
        self.notification_font = pygame.font.Font(None, 24)
        self.controller = controller

        # Define button properties
        button_width, button_height = 100, 25
        start_button_x, start_button_y = (self.width - button_width) // 4, self.height - button_height - 10
        pause_button_x, pause_button_y = start_button_x + button_width + 10, self.height - button_height - 10
        save_button_x, save_button_y = pause_button_x + button_width + 10, self.height - button_height - 10
        load_button_x, load_button_y = save_button_x + button_width + 10, self.height - button_height - 10

        self.buttons = {
            "start": (start_button_x, start_button_y),
            "pause": (pause_button_x, pause_button_y),
            "save": (save_button_x, save_button_y),
            "load": (load_button_x, load_button_y),
        }

    def draw_grid(self):
        for y in range(0, self.height, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, self.colors["gray"], cell, 1)

    def draw_cells(self):
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if self.controller.manager.game_state[x, y] == 1:
                    pygame.draw.rect(self.screen, self.colors["black"], cell)

    def draw_buttons(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for label, (x, y) in self.buttons.items():
            is_hovered = x <= mouse_x <= x + 100 and y <= mouse_y <= y + 25
            if label == "pause":
                color = self.colors["dark_red"] if is_hovered else self.colors["red"]
            else:
                color = self.colors["dark_green"] if is_hovered else self.colors["green"]

            pygame.draw.rect(self.screen, color, (x, y, 100, 25))
            font = pygame.font.Font(None, 36)
            text_color = self.colors["white"] if is_hovered else self.colors["black"]
            text = font.render(label.capitalize(), True, text_color)
            text_rect = text.get_rect(center=(x + 50, y + 12))
            self.screen.blit(text, text_rect)

    def draw_notification(self):
        if self.notification and self.notification_timer > 0:
            text_render = self.notification_font.render(self.notification, True, self.colors["black"])
            text_rect = text_render.get_rect(center=(self.width // 2, self.height - 50))

            bg_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)
            pygame.draw.rect(self.screen, self.colors["white"], bg_rect)
            pygame.draw.rect(self.screen, self.colors["black"], bg_rect, 2)

            self.screen.blit(text_render, text_rect)
            self.notification_timer -= 1
        elif self.notification_timer == 0:
            self.notification = ""

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.manager.stop()
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for label, (btn_x, btn_y) in self.buttons.items():
                    if btn_x <= x <= btn_x + 100 and btn_y <= y <= btn_y + 25:
                        self.notification = self.controller.handle_button_click(label)
                        self.notification_timer = 120 if self.notification else 0

        return True

    def run(self):
        running = True
        while running:
            self.screen.fill(self.colors["white"])
            self.draw_grid()
            self.draw_cells()
            self.draw_buttons()
            self.draw_notification()
            pygame.display.flip()
            running = self.handle_events()
        pygame.quit()
