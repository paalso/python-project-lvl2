from gendiff.gendiff import generate_dicts_difference_dict
from gendiff.gendiff import stringify_value

gen_diff = generate_dicts_difference_dict


def test_stringify_value():
    assert stringify_value('Hexlet') == 'Hexlet'
    assert stringify_value(50) == '50'
    assert stringify_value(1.0) == '1.0'
    assert stringify_value(1e0) == '1.0'
    assert stringify_value(0.1e1) == '1.0'
    assert stringify_value(True) == 'true'
    assert stringify_value(False) == 'false'
    assert stringify_value(None) == 'null'


def test_gen_diff_with_empty_dict():
    assert gen_diff({}, {"two": "own"}) == {"two": "added"}
    assert gen_diff({"one": "eon"}, {}) == {"one": "deleted"}


def test_gen_diff():
    assert gen_diff(
        {"three": "eerht"},
        {"four": "ruof"},
    ) == {
        "three": "deleted",
        "four": "added",
    }

    assert gen_diff(
        {"five": 5, "six": 6},
        {"six": "xis", "five": 5},
    ) == {
        "six": 'changed',
        "five": 'unchanged',
    }

    assert gen_diff(
        {"seven": "neves"},
        {"eighth": True},
    ) == {
        "seven": "deleted",
        "eighth": "added",
    }
