def set_dict_value(d: dict, path: tuple, value):
    if len(path) != 0:
        current = d
        for key in path[:-1]:
            if key not in current or type(current[key]) != dict:
                current[key] = {}
            current = current[key]
        current[path[-1]] = value


def generate_dicts_difference_dict(dict_old: dict, dict_new: dict) -> dict:  # noqa: C901, E501
    diff_dict = {}

    def helper(dict_old, dict_new, path):

        old_keys = dict_old.keys()
        new_keys = dict_new.keys()

        added_keys = new_keys - old_keys
        deleted_keys = old_keys - new_keys
        common_keys = new_keys & old_keys

        for key in added_keys:
            set_dict_value(diff_dict, path + (key,), 'added')

        for key in deleted_keys:
            set_dict_value(diff_dict, path + (key,), 'deleted')

        for key in common_keys:
            value_new = dict_new[key]
            value_old = dict_old[key]

            if type(value_new) == type(value_old) == dict:
                helper(value_old, value_new, path + (key,))
            elif value_new != value_old:
                set_dict_value(diff_dict, path + (key,), 'changed')
            else:
                set_dict_value(diff_dict, path + (key,), 'unchanged')

    helper(dict_old, dict_new, tuple())
    return diff_dict
