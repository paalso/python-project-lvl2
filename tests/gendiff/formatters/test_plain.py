from gendiff.formatters.plain import _stringify
from gendiff.formatters.plain import _upd_path
from tests.fixtures.expected_dicts import NESTED_DICT_1


def test_stringify_primitive_values():
    assert _stringify('Hexlet') == "'Hexlet'"
    assert _stringify('') == "''"
    assert _stringify(50) == '50'
    assert _stringify(1.0) == '1.0'
    assert _stringify(1e0) == '1.0'
    assert _stringify(0.1e1) == '1.0'
    assert _stringify(True) == 'true'
    assert _stringify(False) == 'false'
    assert _stringify(None) == 'null'


def test_stringify_dicts():
    data = {"hello": "world", "is": True, "nested": {"count": 5}}
    assert _stringify(data) == '[complex value]'
    assert _stringify(NESTED_DICT_1) == '[complex value]'


def test_upd_path():
    assert _upd_path('', 'key1') == 'key1'
    assert _upd_path('key1', 'key2') == 'key1.key2'
    assert _upd_path('key1.key2', 'key3') == 'key1.key2.key3'
