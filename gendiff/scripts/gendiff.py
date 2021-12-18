#!/usr/bin/env python

import argparse
import json


# FIX: REMOVE!
def increment(num: int):
    return num + 1


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


def generate_diff(file_path1, file_path2):

    # FIX!
    # print("generate_diff launched 19:46!!!")
    # return

    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))
    diff_dict = generate_dicts_difference_dict(json1, json2)
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


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('filename1', metavar='first_file')
    parser.add_argument('filename2', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def main():
    args = parse_args()

    filename1, filename2 = args.filename1, args.filename2
    if not args.format:
        args.format = 'json'

    print(generate_diff(filename1, filename2))


if __name__ == '__main__':
    main()
