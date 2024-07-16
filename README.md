# Rock-Paper-Scissors Game

## Environment Setup and Code Execution

### Setup

To run the rock-paper-scissors game, follow these steps:

1. **Create Virtual Environment:**
   
   ```bash
   make env

### Explanation:

- **Title (`# Rock-Paper-Scissors Game`)**: Introduces the project and sets the context.

- **Environment Setup and Code Execution**: Provides clear instructions on how to prepare the environment and execute the game using Makefile commands.

- **Setup**: Outlines the steps to create a virtual environment (`make env`) and provides an overview of the available Makefile targets (`clean`, `build`, `run`) for managing the environment and running the game.

- **Summary of Python Files**: Describes the purpose and functionality of each Python script (`model.py`, `randomgame.py`, `evaluate.py`) involved in the project:

  - **`model.py`**: Handles file operations and data manipulation using pandas for reading, comparing, and calculating scores based on moves stored in `player1.txt` and `player2.txt`.
  
  - **`randomgame.py`**: Generates random moves ("rock", "paper", "scissors") for a specified number of rounds, writes them to new `player#.txt` files, and determines the next available player number dynamically.
  
  - **`evaluate.py`**: Reads moves from `player1.txt` and `player2.txt`, compares them based on predefined game rules to calculate scores for Player 1, Player 2, and ties.

This structured format ensures clarity in understanding how to use and interact with the rock-paper-scissors game project, making it easier for users to get started and utilize the provided functionality. Adjust the markdown formatting as needed when adding it to your `README.md` file.