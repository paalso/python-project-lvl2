import json


def _generate_dicts_difference_dict(old_dict, new_dict):

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


def generate_diff(file_path1, file_path2):
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))
    diff_dict = _generate_dicts_difference_dict(json1, json2)
    tokens = ['{']

    for key in sorted(diff_dict):
        if diff_dict[key] == 'added':
            tokens.append(f'  + {key}: {json2[key]}')
        elif diff_dict[key] == 'deleted':
            tokens.append(f'  - {key}: {json1[key]}')
        elif diff_dict[key] == 'unchanged':
            tokens.append(f'    {key}: {json1[key]}')
        else:
            tokens.append(f'  - {key}: {json1[key]}')
            tokens.append(f'  + {key}: {json2[key]}')
    tokens.append('}')

    return '\n'.join(tokens)
