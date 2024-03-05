test:
	pytest

coverage:
	pytest -s --cov --cov-report html --cov-fail-under 100

yamllint:
	yamllint -d relaxed .

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall replay-wizard -y
	rm -rf dist
	rm -rf replay_wizard.egg-info

reinstall:
	make uninstall
	make install

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint

sphinx-help:
	make help -f Sphinxfile

package_docs:
	sphinx-apidoc -o docs/package replay_wizard/

capture:
	python main.py capture debug

time_capture:
	python main.py capture debug -t true

replay:
	python main.py replay debug -d 5

time_replay:
	python main.py replay debug -t true -d 5

monitor_replay:
	python main.py replay debug -t true -d 5 -m true

capture_mouse:
	python main.py capture debug -k false -mo true -t true

capture_all:
	python main.py capture debug -mo true -t true