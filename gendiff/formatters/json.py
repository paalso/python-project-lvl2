import json


def gen_json_diff(dicts_diff: dict) -> str:
    """Returns json representation of the given dicts diff file
      inner structure.

    Args:
        dicts_diff: A special format dictionary that describes difference
          between two dictionaries

    Returns:
        A json representation of the dicts_diff inner structure
    """
    return json.dumps(dicts_diff, indent=2)
