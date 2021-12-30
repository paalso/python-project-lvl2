import gendiff.input_parser as input_parser


def generate_dicts_difference_dict(old_dict, new_dict):

    diff_dict = dict()

    for key in old_dict.keys() | new_dict.keys():
        if key not in old_dict:
            diff_dict[key] = 'added'
        elif key not in new_dict:
            diff_dict[key] = 'deleted'
        elif new_dict[key] != old_dict[key]:
            diff_dict[key] = 'changed'
        else:
            diff_dict[key] = 'unchanged'
    return diff_dict


def stringify_value(value):
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    str_value = str(value)
    return special_values.get(str_value, str_value)


def generate_diff(file_path1, file_path2):
    dict1 = input_parser.get_dict_from_datafile(file_path1)
    dict2 = input_parser.get_dict_from_datafile(file_path2)
    diff_dict = generate_dicts_difference_dict(dict1, dict2)

    tokens = ['{']
    for key in sorted(diff_dict):
        if diff_dict[key] == 'added':
            tokens.append(f'  + {key}: {stringify_value(dict2[key])}')
        elif diff_dict[key] == 'deleted':
            tokens.append(f'  - {key}: {stringify_value(dict1[key])}')
        elif diff_dict[key] == 'unchanged':
            tokens.append(f'    {key}: {stringify_value(dict1[key])}')
        else:
            tokens.append(f'  - {key}: {stringify_value(dict1[key])}')
            tokens.append(f'  + {key}: {stringify_value(dict2[key])}')
    tokens.append('}')

    return '\n'.join(tokens)
