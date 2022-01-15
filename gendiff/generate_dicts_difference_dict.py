def set_dict_value(d: dict, path: tuple, value):
    """ In the given dictionary, changes (or adds) the value in
    the specified path. The function mutates the dictionary.
    """
    if len(path) != 0:
        current = d
        for key in path[:-1]:
            if key not in current or type(current[key]) != dict:
                current[key] = {}
            current = current[key]
        current[path[-1]] = value


def generate_dicts_difference_dict(     # noqa: C901
        dict_old: dict, dict_new: dict) -> dict:
    """ Generates a special format diff dictionary that describes what happened
    to each key in the given compared dictionaries: whether it was added,
    changed, or removed, as well as the corresponding dictionary values.
    """

    diff_dict = {}

    def helper(dict_old, dict_new, path):

        old_keys = dict_old.keys()
        new_keys = dict_new.keys()

        added_keys = new_keys - old_keys
        deleted_keys = old_keys - new_keys
        common_keys = new_keys & old_keys

        for key in added_keys:
            set_dict_value(diff_dict, path + (key,),
                           ('added', dict_new[key]))

        for key in deleted_keys:
            set_dict_value(diff_dict, path + (key,),
                           ('deleted', dict_old[key]))

        for key in common_keys:
            value_new = dict_new[key]
            value_old = dict_old[key]

            if type(value_new) == type(value_old) == dict:
                helper(value_old, value_new, path + (key,))
            elif value_new != value_old:
                set_dict_value(diff_dict, path + (key,),
                               ('changed', (value_old, value_new)))
            else:
                set_dict_value(diff_dict, path + (key,),
                               ('unchanged', value_old))

    helper(dict_old, dict_new, tuple())
    return diff_dict
