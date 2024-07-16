clean:
	rm -f *.txt
env:
	python -m venv myenv
build:
	source ./myenv/bin/activate
deactivate:
	deactivate
run:
	python random_game.py

