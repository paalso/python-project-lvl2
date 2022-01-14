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
        'follow': ('added', False),
        'setting1': ('unchanged', 'Value 1'),
        'setting2': ('deleted', 200),
        'setting3': ('changed', (True, None)),
        'setting4': ('added', 'blah blah'),
        'setting5': ('added', {'key5': 'value5'}),
        'setting6': {
            'key': ('unchanged', 'value'),
            'doge': {
                'wow': ('changed', ('', 'so much')),
            },
            'ops': ('added', 'vops'),
        },
    },
    'group1': {
        'baz': ('changed', ('bas', 'bars')),
        'foo': ('unchanged', 'bar'),
        'nest': ('changed', ({'key': 'value'}, 'str')),
    },
    'group2': ('deleted', {'abc': 12345, 'deep': {'id': 45}}),
    'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})
}

NESTED_DIFF_DICT_21 = {
    'common': {
        'follow': ('deleted', False),
        'setting1': ('unchanged', 'Value 1'),
        'setting2': ('added', 200),
        'setting3': ('changed', (None, True)),
        'setting4': ('deleted', 'blah blah'),
        'setting5': ('deleted', {'key5': 'value5'}),
        'setting6': {
            'key': ('unchanged', 'value'),
            'doge': {
                'wow': ('changed', ('so much', '')),
            },
            'ops': ('deleted', 'vops'),
        },
    },
    'group1': {
        'baz': ('changed', ('bars', 'bas')),
        'foo': ('unchanged', 'bar'),
        'nest': ('changed', ('str', {'key': 'value'})),
    },
    'group2': ('added', {'abc': 12345, 'deep': {'id': 45}}),
    'group3': ('deleted', {'deep': {'id': {'number': 45}}, 'fee': 100500})
}
