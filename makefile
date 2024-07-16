clean:
	rm -f *.txt
build:
	python -m venv myenv
	source ./myenv/bin/activate
deactivate:
	deactivate

