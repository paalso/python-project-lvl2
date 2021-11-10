#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('strings', metavar='first_file', type=str, nargs=1,
                        help='')
    parser.add_argument('strings', metavar='second_file', type=str, nargs=1,
                        help='')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
