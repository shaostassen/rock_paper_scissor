# This is a placeholder for the model code that will be used to make a robust rock paper scissors machine

import pandas as pd

# Read the contents of player1.txt into a list
with open('player1.txt', 'r') as file:
    moves = file.read().splitlines()

# Create a pandas DataFrame
df = pd.DataFrame(moves, columns=['Move'])

# Display the DataFrame
print(df)