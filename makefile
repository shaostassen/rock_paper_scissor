clean:
	rm -f *.txt
build:
	python3 -m venv myenv
	source ./myenv/bin/activate
deactivate:
	deactivate

