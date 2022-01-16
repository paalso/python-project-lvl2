from gendiff.generate_dicts_difference_dict import set_dict_value
from gendiff.generate_dicts_difference_dict import \
    generate_dicts_difference_dict as gen_diff
from tests.fixtures.expected_dicts import NESTED_DICT_1
from tests.fixtures.expected_dicts import NESTED_DICT_2
from tests.fixtures.expected_dicts import NESTED_DIFF_DICT_12
from tests.fixtures.expected_dicts import NESTED_DIFF_DICT_21


# ----- set_dict_value tests -----
def test_set_dict_value0():
    coll = {}
    set_dict_value(coll, [], 1)
    assert coll == {}


def test_set_dict_value1():
    coll = {}
    set_dict_value(coll, ['a'], 1)
    assert coll == {'a': 1}

    coll = {}
    set_dict_value(coll, ['a', 'b', 'c'], 1)
    assert coll == {'a': {'b': {'c': 1}}}


def test_set_dict_value2():
    coll = {'a': {'b': {'c': 3}}}

    set_dict_value(coll, ['a', 'b', 'c'], 4)
    assert coll == {'a': {'b': {'c': 4}}}

    set_dict_value(coll, ['a', 'b', 'c', 'd'], 5)
    assert coll == {'a': {'b': {'c': {'d': 5}}}}

    set_dict_value(coll, ['a', 'b', 'c', 'e'], 6)
    assert coll == {'a': {'b': {'c': {'d': 5, 'e': 6}}}}

    set_dict_value(coll, ['a', 'b'], 4)
    assert coll == {'a': {'b': 4}}

    set_dict_value(coll, ['x', 'y', 'z'], 5)
    assert coll == {'a': {'b': 4}, 'x': {'y': {'z': 5}}}


def test_gen_diff_nested():
    assert gen_diff(NESTED_DICT_1, NESTED_DICT_2) == NESTED_DIFF_DICT_12
    assert gen_diff(NESTED_DICT_2, NESTED_DICT_1) == NESTED_DIFF_DICT_21
