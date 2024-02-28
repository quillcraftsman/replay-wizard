test:
	pytest

coverage:
	DISPLAY=":0" python -m pytest -s --cov --cov-report html --cov-fail-under 100

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