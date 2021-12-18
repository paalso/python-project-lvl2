install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report xml

build:
	python3 -m pip3 install .
