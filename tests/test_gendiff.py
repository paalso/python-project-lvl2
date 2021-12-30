from gendiff.gendiff import generate_diff
from tests.fixtures.expected import PLAIN_JSONS_DIFF_STR_12
from tests.fixtures.expected import PLAIN_JSONS_DIFF_STR_21


def test_gendiff_plain():
    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.json'
    ) == PLAIN_JSONS_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain1.yaml',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_JSONS_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain1.json',
        './tests/fixtures/plain2.yaml'
    ) == PLAIN_JSONS_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain1.yml',
        './tests/fixtures/plain2.json'
    ) == PLAIN_JSONS_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.json'
    ) == PLAIN_JSONS_DIFF_STR_21

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.yml'
    ) == PLAIN_JSONS_DIFF_STR_21

    assert generate_diff(
        './tests/fixtures/plain2.yml',
        './tests/fixtures/plain1.json'
    ) == PLAIN_JSONS_DIFF_STR_21

    assert generate_diff(
        './tests/fixtures/plain2.json',
        './tests/fixtures/plain1.yaml'
    ) == PLAIN_JSONS_DIFF_STR_21
