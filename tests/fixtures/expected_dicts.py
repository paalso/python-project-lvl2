NESTED_DICT_1 = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {'key': 'value', 'doge': {'wow': ''}},
    },
    'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
    'group2': {'abc': 12345, 'deep': {'id': 45}},
}


NESTED_DICT_2 = {
    'common': {
        'follow': False,
        'setting1': 'Value 1',
        'setting3': None,
        'setting4': 'blah blah',
        'setting5': {'key5': 'value5'},
        'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}},
    },
    'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'},
    'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500},
}


NESTED_DIFF_DICT_12 = {
    'common': {
        'follow': 'added',
        'setting1': 'unchanged',
        'setting2': 'deleted',
        'setting3': 'changed',
        'setting4': 'added',
        'setting5': 'added',
        'setting6': {
            'key': 'unchanged',
            'doge': {
                'wow': 'changed',
            },
            'ops': 'added',
        },
    },
    'group1': {
        'baz': 'changed',
        'foo': 'unchanged',
        'nest': 'changed',
    },
    'group2': 'deleted',
    'group3': 'added',
}

NESTED_DIFF_DICT_21 = {
    'common': {
        'follow': 'deleted',
        'setting1': 'unchanged',
        'setting2': 'added',
        'setting3': 'changed',
        'setting4': 'deleted',
        'setting5': 'deleted',
        'setting6': {
            'key': 'unchanged',
            'doge': {
                'wow': 'changed',
            },
            'ops': 'deleted',
        },
    },
    'group1': {
        'baz': 'changed',
        'foo': 'unchanged',
        'nest': 'changed',
    },
    'group2': 'added',
    'group3': 'deleted',
}
