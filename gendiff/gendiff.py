from gendiff.generate_dicts_difference_dict import \
    generate_dicts_difference_dict
from gendiff.input_parser import get_dict_from_datafile


def stringify_simple_value(value):
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    str_value = str(value)
    return special_values.get(str_value, str_value)


def stringify(data, replacer=' ', spaces_count=4, indent_size=0):

    def helper(data, depth):
        if not isinstance(data, dict):
            return stringify_simple_value(data)

        indent = replacer * (depth * spaces_count + indent_size)
        inner_tokens = (f'{indent}{key}: {helper(value, depth + 1)}'
                        for key, value in data.items())

        right_brace_indent = \
            replacer * ((depth - 1) * spaces_count + indent_size)
        tokens = ['{', *inner_tokens,
                  f'{right_brace_indent}}}']
        return "\n".join(tokens)

    return helper(data, 1)


def generate_diff(file_path1: str, file_path2: str) -> str:
    dict1 = get_dict_from_datafile(file_path1)
    dict2 = get_dict_from_datafile(file_path2)
    diff_dict = generate_dicts_difference_dict(dict1, dict2)

    def helper(dict_value, depth):
        deep_indent_size = depth * 4
        deep_indent = (deep_indent_size - 2) * ' '
        right_brace_indent = (deep_indent_size - 4) * ' '

        tokens = ['{']
        for key in sorted(dict_value):
            value = dict_value[key]
            if isinstance(value, dict):
                tokens.append(
                    f'{deep_indent}  {key}: {helper(value, depth + 1)}')
                continue

            status, content = value
            if status == 'changed':
                old_content, new_content = content
                value_str_old = stringify(
                    old_content, indent_size=deep_indent_size)
                value_str_new = stringify(
                    new_content, indent_size=deep_indent_size)
                tokens.append(f'{deep_indent}- {key}: {value_str_old}')
                tokens.append(f'{deep_indent}+ {key}: {value_str_new}')
                continue

            change_status_sign = {
                'added': '+', 'deleted': '-', 'unchanged': ' '
            }[status]
            value_str = stringify(content, indent_size=deep_indent_size)
            tokens.append(
                f'{deep_indent}{change_status_sign} {key}: {value_str}')

        tokens.append(f'{right_brace_indent}}}')

        return '\n'.join(tokens)

    return helper(diff_dict, 1)
