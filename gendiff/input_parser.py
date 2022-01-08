import pathlib
import json
from types import MethodType
import yaml


def get_file_extension(file_path: str) -> str:
    return pathlib.Path(file_path).suffix


def get_file_reader(file_path: str) -> MethodType:
    return {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(get_file_extension(file_path))


def get_dict_from_datafile(file_path: str) -> dict:
    reader = get_file_reader(file_path)
    if reader:
        with open(file_path) as f:
            return reader(f)
