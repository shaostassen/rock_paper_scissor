import random

def make_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_round(prompt, default_value):
    user_input = input(prompt)
    if not user_input:
        return default_value
    return user_input


def main():
    # Define the number of rounds
    rounds = int(get_round("Enter the number of rounds: ", 100))
    # Define the file name
    file_name = "result.txt"

    # Open the file in write mode (this will create the file if it doesn't exist)
    with open(file_name, "w") as file:
        for i in range(rounds):
            # Write some values to the file
            file.write(make_choice()+"\n")
    # The file is automatically closed when the with block is exited
    file.close()

if __name__ == "__main__":
    main()