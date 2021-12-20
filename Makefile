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
	poetry run flake8 tests

test:
	poetry run pytest -s -vv
