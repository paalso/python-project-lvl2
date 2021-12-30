from gendiff.gendiff import stringify_value


def test_stringify_value():
    assert stringify_value('Hexlet') == 'Hexlet'
    assert stringify_value(50) == '50'
    assert stringify_value(1.0) == '1.0'
    assert stringify_value(1e0) == '1.0'
    assert stringify_value(0.1e1) == '1.0'
    assert stringify_value(True) == 'true'
    assert stringify_value(False) == 'false'
    assert stringify_value(None) == 'null'
