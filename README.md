# US-States-game-gajanan
## README: U.S. States Game

### Overview

The U.S. States Game is an interactive Python application where you test your knowledge by naming all 50 U.S. states. Each correct answer is written on a blank map in its proper location, helping you learn state geography in a fun and visual way!

### How to Play

1. **Run `main.py`**  
   The game uses the Turtle graphics library to display a blank map (`blank_states_img.jpg`) on your screen.

2. **Guess States**  
   - You will be prompted to enter the name of a U.S. state.
   - Each correct answer:
     - Is marked on the map at its geographical location.
     - Increases your score.
   - States are matched case-insensitively.
   - Type `exit` at any time to quit the game.

3. **Game Completion**
   - The game ends when you either name all 50 states or exit.
   - When finished, a list of missed states is saved to `missed_states.csv` (shows state names and coordinates).

### File Descriptions

- **main.py** — Main game logic, handles user input, updates the map, and tracks progress.
- **50_states.csv** — Contains all U.S. state names and their x/y coordinates for map placement.
- **missed_states.csv** — Generated after playing, lists any states you didn’t guess.
- **blank_states_img.jpg** — The background map displayed in the game.

### Requirements

- Python 3.x
- `turtle` graphics library (included with standard Python)
- `pandas` library

### Quick Start Instructions

1. Ensure all files (`main.py`, `50_states.csv`, `blank_states_img.jpg`) are in the same folder.
2. Install pandas if needed (`pip install pandas`).
3. Run `main.py`.
4. Try to name all 50 states before you exit!

### Educational Value

This game is great for memorizing U.S. geography, mastering state spellings, and having fun with friends or in the classroom.

***

**Enjoy testing your U.S. state knowledge—can you name them all?**
