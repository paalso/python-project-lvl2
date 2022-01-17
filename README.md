## Level 2 project on [Hexlet](https://ru.hexlet.io/), program [Python developer](https://ru.hexlet.io/programs/python).
### [Вычислитель отличий (Diffs generator)](https://ru.hexlet.io/programs/python/projects/50)

#### Computes the AST difference between two JSON/YAML files and outputs in specifiied format


### Hexlet tests and linter status:
[![Actions Status](https://github.com/paalso/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/paalso/python-project-lvl2/actions)

### Pytests and flake8 linter status:
[![lint&test](https://github.com/paalso/python-project-lvl2/actions/workflows/lint-test.yml/badge.svg)](https://github.com/paalso/python-project-lvl2/actions/workflows/lint-test.yml)

### Code Climate maintainability status
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)


## Installation:

```sh
pip install --user git+https://github.com/paalso/python-project-lvl2.git
```
[![asciicast](https://asciinema.org/a/ItFSylslQyWNMzLuA2bWbbxPa.svg)](https://asciinema.org/a/ItFSylslQyWNMzLuA2bWbbxPa)

## The package usage

### Usage as a library
[![asciicast](https://asciinema.org/a/LYyuvTzLuAttGJ4EHlBeJCgED.svg)](https://asciinema.org/a/LYyuvTzLuAttGJ4EHlBeJCgED)

### Usage as a cli utility
```
gendiff [-h] [-f [--format] FORMAT] first_file second_file
```
Supported file formats: JSON, YAML

'stylish' format:
```
gendiff --format stylish first_file second_file
```

'plain' format
```
gendiff --format plain first_file second_file
```

inner json representation of diff AST: 
```
gendiff --format json first_file second_file
```
[![asciicast](https://asciinema.org/a/T7yXHbloR2BMpnDqHcVNXOyIc.svg)](https://asciinema.org/a/T7yXHbloR2BMpnDqHcVNXOyIc)

