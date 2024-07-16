
def read_moves(filename):
    with open(filename, 'r') as file:
        moves = file.read().splitlines()
    return moves

def compare_moves(move1, move2):
    if move1 == move2:
        return 0, 0, 1 # Tie, no points
    elif (move1 == 'rock' and move2 == 'scissors') or \
         (move1 == 'scissors' and move2 == 'paper') or \
         (move1 == 'paper' and move2 == 'rock'):
        return 1, 0, 0  # Player 1 wins
    else:
        return 0, 1, 0  # Player 2 wins

def calculate_scores(moves1, moves2):
    score1, score2, tie = 0, 0, 0
    for move1, move2 in zip(moves1, moves2):
        result1, result2, result3 = compare_moves(move1, move2)
        score1 += result1
        score2 += result2
        tie += result3
    return score1, score2, tie

def main():
    player1_moves = read_moves('player1.txt')
    player2_moves = read_moves('player2.txt')

    score1, score2, tie = calculate_scores(player1_moves, player2_moves)

    print(f"Player 1 Score: {score1}")
    print(f"Player 2 Score: {score2}")
    print(f"Number of ties: {tie}")


if __name__ == "__main__":
    main()