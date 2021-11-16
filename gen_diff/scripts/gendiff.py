#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('filename1', metavar='first_file', nargs=1)
    parser.add_argument('filename2', metavar='second_file', nargs=1)

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    if not args.format:
        args.format = 'json'
    print(first_file)


if __name__ == '__main__':
    main()
