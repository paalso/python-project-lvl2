import json
import yaml
from gendiff.input_parser import get_file_extension
from gendiff.input_parser import get_file_reader
from gendiff.input_parser import get_dict_from_datafile


plain1 = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
    'float': 1.0,
    'married': None,
}

plain2 = {
    'timeout': 20,
    'married': None,
    'float': 0.1e1,
    'verbose': True,
    'host': 'hexlet.io',
}


def test_stringify_value():
    assert get_file_extension('file') == ''
    assert get_file_extension('file.txt') == '.txt'
    assert get_file_extension('/home/user/Projects/script.py') == '.py'
    assert get_file_extension(r'C:\python3\file.tar.gz') == '.gz'


def test_get_file_reader():
    assert get_file_reader('/home/user/Projects/script.py') is None
    assert get_file_reader(r'C:\python3\data.json') == json.load
    assert get_file_reader('file.yml') == yaml.safe_load
    assert get_file_reader('/home/user/data/info.yaml') == yaml.safe_load


def test_get_dict_from_datafile():
    assert get_dict_from_datafile('./tests/fixtures/plain1.json') == plain1
    assert get_dict_from_datafile('./tests/fixtures/plain2.json') == plain2
    assert get_dict_from_datafile('./tests/fixtures/plain1.yaml') == plain1
    assert get_dict_from_datafile('./tests/fixtures/plain2.yaml') == plain2
    assert get_dict_from_datafile('./tests/fixtures/plain1.yml') == plain1
    assert get_dict_from_datafile('./tests/fixtures/plain2.yml') == plain2
