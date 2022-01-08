from gendiff.gendiff import generate_diff
from gendiff.gendiff import stringify_value
from tests.fixtures.expected_strings import PLAIN_DIFF_STR_12
from tests.fixtures.expected_strings import PLAIN_DIFF_STR_21


def test_stringify_value():
    assert stringify_value('Hexlet') == 'Hexlet'
    assert stringify_value(50) == '50'
    assert stringify_value(1.0) == '1.0'
    assert stringify_value(1e0) == '1.0'
    assert stringify_value(0.1e1) == '1.0'
    assert stringify_value(True) == 'true'
    assert stringify_value(False) == 'false'
    assert stringify_value(None) == 'null'


def test_gendiff_plain():
    # Test jsons
    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.json'
    ) == PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.json'
    ) == PLAIN_DIFF_STR_21

    # Test yamls and # Test yamls with jsons in in various combinations
    assert generate_diff(
        './tests/fixtures/plain1.yaml',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain1.yml',
        './tests/fixtures/plain2.json'
    ) == PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.yml'
    ) == PLAIN_DIFF_STR_21

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.json'
    ) == PLAIN_DIFF_STR_21

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.yaml'
    ) == PLAIN_DIFF_STR_21
