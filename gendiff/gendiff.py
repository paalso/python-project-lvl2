from gendiff.ast_builder import build_ast
from gendiff.input_parser import parse_datafile
from gendiff.formatters import gen_plain_diff, gen_stylish_diff, gen_json_diff


def generate_diff(
        file_path1: str, file_path2: str, format_name='stylish') -> str:
    """ Returns the given special formatted ('plain'/'stylish'/'json') text
      representation of the difference between two JSONs or YAMLs.

    Args:
        file_path1: Path to the original JSON/YAML
        file_path1: Path to the final JSON/YAML
        format_name: text representation format name, defaults to 'stylish'

    Returns:
        The given special formatted text representation of the difference
      between the given files
    """
    dict1 = parse_datafile(file_path1)
    dict2 = parse_datafile(file_path2)

    return {'plain': gen_plain_diff,
            'stylish': gen_stylish_diff,
            'json': gen_json_diff,
            }[format_name](build_ast(dict1, dict2))
