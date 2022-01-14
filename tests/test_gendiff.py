from gendiff.gendiff import generate_diff
from gendiff.gendiff import stringify_simple_value
from gendiff.gendiff import stringify
from tests.fixtures.expected_strings import *   # noqa: F403,F405


def test_stringify_simple_value():
    assert stringify_simple_value('Hexlet') == 'Hexlet'
    assert stringify_simple_value(50) == '50'
    assert stringify_simple_value(1.0) == '1.0'
    assert stringify_simple_value(1e0) == '1.0'
    assert stringify_simple_value(0.1e1) == '1.0'
    assert stringify_simple_value(True) == 'true'
    assert stringify_simple_value(False) == 'false'
    assert stringify_simple_value(None) == 'null'


def test_stringify_value():
    data = {"hello": "world", "is": True, "nested": {"count": 5}}
    assert stringify(data, spaces_count=1) == STRINGIFIED_DICT_1    # noqa: F405
    assert stringify(data) == STRINGIFIED_DICT_2    # noqa: F405
    assert stringify(data, replacer='|-', spaces_count=2) == \
        STRINGIFIED_DICT_3  # noqa: F405
    assert stringify(data, spaces_count=4, indent_size=4) == \
        STRINGIFIED_DICT_INDENTED_1     # noqa: F405
    assert stringify(data, spaces_count=4, indent_size=2) == \
        STRINGIFIED_DICT_INDENTED_2     # noqa: F405
    assert stringify(data, spaces_count=4, indent_size=8) == \
        STRINGIFIED_DICT_INDENTED_3     # noqa: F405


def test_gendiff_plain():
    # Test jsons
    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.json'
    ) == PLAIN_DIFF_STR_12  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.json'
    ) == PLAIN_DIFF_STR_21  # noqa: F405

    # Test yamls and # Test yamls with jsons in in various combinations
    assert generate_diff(
        './tests/fixtures/plain1.yaml',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_DIFF_STR_12  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_DIFF_STR_12  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain1.yml',
        './tests/fixtures/plain2.json'
    ) == PLAIN_DIFF_STR_12  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.yml'
    ) == PLAIN_DIFF_STR_21  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.json'
    ) == PLAIN_DIFF_STR_21  # noqa: F405

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.yaml'
    ) == PLAIN_DIFF_STR_21  # noqa: F405


def test_gendiff_nested():
    # Test jsons
    assert generate_diff(
        './tests/fixtures/nested1.json',
        './tests/fixtures/nested2.json'
    ) == NESTED_DIFF_STR_12     # noqa: F405
