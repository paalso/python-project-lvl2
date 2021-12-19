install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

local-build:
	python3 -m pip install 

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report xml
