# Game of Life

A Python implementation of Conway's Game of Life with a graphical user interface using Pygame.  
This project simulates cellular automata and allows users to control the state of the grid through various UI buttons.

---

## Features

- Rendering of the Game of Life grid using Pygame.
- **Buttons** for controlling the game:
    - Start
    - Pause
    - Save
    - Load
- Notifications to inform the user about game events.
- Easy-to-read and modularized codebase for further extensions.

---

## Requirements

To run this project, you need the following:

- Python 3.12 or higher
- Installed dependencies in `requirements.txt` (see installation steps below)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dlamanova/game_of_life.git
   cd your_project
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## How to Play

1. **Start**: Press the "Start" button to begin/resume the simulation.
2. **Pause**: Press the "Pause" button to stop the simulation temporarily.
3. **Save**: Save the current state of the grid.
4. **Load**: Load a previously saved grid state.

You can also interact directly with the grid cells in some implementations, depending on the controller's behavior.

---

## Folder Structure

- `main.py`: Entry point of the application.
- `game/`: Contains the main logic, including grid management and game state.
- `ui.py`: Contains the user interface (buttons, notifications, and rendering code).
- `constants.py`: Stores game configuration, colors, and screen settings.

---

## Demo

![Game Demo](assets/demo.gif)