### Задача 1.1
#### Склонируйте созданный репозиторий проекта локально

https://github.com/paalso/python-project-lvl2.git

#### и инициализируйте ваш пакет внутри корневой директории проекта, используя команду poetry init. При инициализации задайте имя пакета - hexlet-code.

```bash
poetry init
...
```

Получаем pyproject.toml
```
[tool.poetry]
name = "hexlet-code"
version = "0.1.0"
description = "Difference calculator utility"
authors = ["paalso <40a.pvl@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"
[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```
  
Т.к. инициализировали пакет с помощью команды **poetry init**, а не **poetry new**,  структуру придется задавать вручную
```bash
mkdir -p gen_diff/scripts
touch gen_diff/__init__.py gen_diff/scripts/__init__.py
```
### Задача 1.2

#### Создайте скрипт (точку входа) gendiff,..

```bash
touch gen_diff/scripts/gendiff.py
```
  
Получили такую структуру:

```bash
.
├── README.md
├── gen_diff
│ ├── __init__.py
│ └── scripts
│ ├── __init__.py
│ └── gendiff.py
└── pyproject.toml
```  

#### ...который при запуске с флагом -h, выводит справку, как указано выше.

Создаем файл
```bash
touch gen_diff/scripts/gendiff.py
```
пишем код, не забываем, что имя пакета называется не так, как называется корневой Python package ("hexlet-code" и "gendiff"),
поэтому в **pyproject.toml** в секцию **[tool.poetry]** нужно добавить параметр **packages**:

```
packages = [
  { include = "gen_diff" },
]
```
и раздел

```
[tool.poetry.scripts]
brain-games = "brain_games.scripts.brain_games:main"
```
Скопируем из рекомендованной шаблонной директории **boilerplate-python-package** (см. [https://github.com/hexlet-boilerplates/python-package](https://github.com/hexlet-boilerplates/python-package)) файлы **.gitignore**, **setup.cfg** (настройки для линтера flake8), **Makefile**, последний отредактируем:

```
install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 hexlet-code
....
```

### Задача 2.1
#### Модифицируйте скрипт (точку входа) gendiff так, чтобы при запуске с флагом -h выводилась справка, как указано выше.
........

### Задача 2.2
#### Выполните сборку пакета.

```bash
poetry build
```
