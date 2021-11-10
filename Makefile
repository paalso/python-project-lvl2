install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 hexlet-code

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
