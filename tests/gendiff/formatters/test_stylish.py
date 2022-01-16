from gendiff.formatters.stylish import _stringify
from tests.fixtures.expected_strings import STRINGIFIED_DICT_1
from tests.fixtures.expected_strings import STRINGIFIED_DICT_2
from tests.fixtures.expected_strings import STRINGIFIED_DICT_3
from tests.fixtures.expected_strings import STRINGIFIED_DICT_INDENTED_1
from tests.fixtures.expected_strings import STRINGIFIED_DICT_INDENTED_2
from tests.fixtures.expected_strings import STRINGIFIED_DICT_INDENTED_3


def test_stringify_primitive_values():
    assert _stringify('Hexlet') == 'Hexlet'
    assert _stringify(50) == '50'
    assert _stringify(1.0) == '1.0'
    assert _stringify(1e0) == '1.0'
    assert _stringify(0.1e1) == '1.0'
    assert _stringify(True) == 'true'
    assert _stringify(False) == 'false'
    assert _stringify(None) == 'null'


def test_stringify_dicts():
    data = {"hello": "world", "is": True, "nested": {"count": 5}}
    assert _stringify(data, spaces_count=1) == STRINGIFIED_DICT_1
    assert _stringify(data) == STRINGIFIED_DICT_2
    assert _stringify(data, replacer='|-', spaces_count=2) == \
        STRINGIFIED_DICT_3
    assert _stringify(data, spaces_count=4, indent_size=4) == \
        STRINGIFIED_DICT_INDENTED_1
    assert _stringify(data, spaces_count=4, indent_size=2) == \
        STRINGIFIED_DICT_INDENTED_2
    assert _stringify(data, spaces_count=4, indent_size=8) == \
        STRINGIFIED_DICT_INDENTED_3
