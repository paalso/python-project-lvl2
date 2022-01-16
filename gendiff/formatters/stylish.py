def _stringify_primitive_value(value):
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    str_value = str(value)
    return special_values.get(str_value, str_value)


def _stringify(data, replacer=' ', spaces_count=4, indent_size=0):
    """Converts any primitive value or standard collection, incl. dictionary
    to a special format string

    Args:
        data to stringify: any primitive value or standard collection,
          incl. dictionary
        replacer: A string indent for a dict key, defaults to ' '
        spaces_count: Number of times to indent a dict key, defaults to 4
        indent_size: Number of additional times to indent a dict content
        for all lines below the opening brace, defaults to 0

    Returns:
        A special format string representing the data
    """

    def helper(data, depth):
        if not isinstance(data, dict):
            return _stringify_primitive_value(data)

        indent = replacer * (depth * spaces_count + indent_size)
        inner_tokens = (f'{indent}{key}: {helper(value, depth + 1)}'
                        for key, value in data.items())

        right_brace_indent = \
            replacer * ((depth - 1) * spaces_count + indent_size)
        tokens = ['{', *inner_tokens,
                  f'{right_brace_indent}}}']
        return "\n".join(tokens)

    return helper(data, 1)


def gen_stylish_diff(dicts_diff: dict) -> str:
    """Returns a special formatted json-like text representation of the given
      dicts diff file.

    Args:
        dicts_diff: A special format dictionary that describes differance
          between two dictionaries

    Returns:
        A special formatted json-like text representation of dicts_diff
    """

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
                value_str_old = _stringify(
                    old_content, indent_size=deep_indent_size)
                value_str_new = _stringify(
                    new_content, indent_size=deep_indent_size)
                tokens.append(f'{deep_indent}- {key}: {value_str_old}')
                tokens.append(f'{deep_indent}+ {key}: {value_str_new}')
                continue

            change_status_sign = {
                'added': '+', 'deleted': '-', 'unchanged': ' '
            }[status]
            value_str = _stringify(content, indent_size=deep_indent_size)
            tokens.append(
                f'{deep_indent}{change_status_sign} {key}: {value_str}')

        tokens.append(f'{right_brace_indent}}}')

        return '\n'.join(tokens)

    return helper(dicts_diff, 1)
