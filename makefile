# Define variables
ENV_NAME := myenv
DEFAULT_ROUNDS := 100

clean:
	rm -f *.txt
env:
	python -m venv $(ENV_NAME)
build:
	source ./$(ENV_NAME)/bin/activate
deactivate:
	deactivate
random:
	python random_game.py rounds=$(or $(rounds),$(DEFAULT_ROUNDS))
evaluate:
    python evaluate.py player1=$(player1) player2=$(player2)

