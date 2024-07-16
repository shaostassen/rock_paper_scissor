import random
import os
import re

def make_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_round(prompt, default_value):
    user_input = input(prompt)
    if not user_input:
        return default_value
    return user_input

def get_next_player_number(directory = '.'):
    # Regular expression pattern to match filenames like "player#.txt"
    pattern = re.compile(r'player(\d+)\.txt')
    
    # Get a list of all files in the specified directory
    files = os.listdir(directory)
    
    # Extract numbers from filenames that match the pattern
    player_numbers = [int(pattern.match(file).group(1)) for file in files if pattern.match(file)]
    
    # Determine the next player number
    if player_numbers:
        next_player_number = max(player_numbers) + 1
    else:
        next_player_number = 1
    
    return next_player_number


def main():
    # Define the number of rounds
    rounds = int(get_round("Enter the number of rounds: ", 100))
    # Define the iter
    next_number = get_next_player_number()
    # Define the file name
    file_name = "player" + str(next_number) + ".txt"

    # Open the file in write mode (this will create the file if it doesn't exist)
    with open(file_name, "w") as file:
        for i in range(rounds):
            # Write some values to the file
            file.write(make_choice()+"\n")
    # The file is automatically closed when the with block is exited
    file.close()

if __name__ == "__main__":
    main()