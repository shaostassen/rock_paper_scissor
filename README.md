# Rock-Paper-Scissors Game

Welcome to the Rock-Paper-Scissors game project! This repository contains Python scripts that simulate a classic game of Rock-Paper-Scissors between two players(one simply randomized player, the other with a complex ML algorithm).

## Context

This project is designed to showcase the implementation of a simple game using Python

### Setup

To run the rock-paper-scissors game, follow these steps:

1. **Create Virtual Environment:**
   
   ```bash
   make env

2. **Activate the Environment:**
   
   ```bash
   make build

3. **Clean up previous player.txt:**
   
   ```bash
   make clean
4. **Run random_game.py:**
   
   ```bash
   make random (optional) rounds=#
5. **Clean up previous player.txt:**
   
   ```bash
   make evaluate (optional) player1=player#.txt player2=player#.txt

### Push to Remote
Make to run:
    ```bash
   make clean
Before you add files through git

### Code Explanation:

- **Summary of Python Files**: Describes the purpose and functionality of each Python script (`model.py`, `randomgame.py`, `evaluate.py`) involved in the project:

  - **`model.py`**: Using a [specify] algorithm to implement a strategy to defeat any player in rock paper scissors

  
  - **`randomgame.py`**: Generates random moves ("rock", "paper", "scissors") for a specified number of rounds, writes them to new `player#.txt` files
    •	make_choice(): Randomly selects a move (“rock”, “paper”, or “scissors”).
	•	get_round(prompt, default_value): Prompts user to enter number of rounds or defaults to 100 if no input.
	•	get_next_player_number(directory='.'): Determines next available player number based on existing player files.
	•	main(): Executes process of generating random moves and writing them to a new player file
