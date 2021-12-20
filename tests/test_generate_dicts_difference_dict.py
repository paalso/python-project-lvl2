from gendiff.gendiff import generate_dicts_difference_dict

gen_diff = generate_dicts_difference_dict


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
