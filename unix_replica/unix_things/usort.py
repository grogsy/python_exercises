import argparse
from operator import itemgetter
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='unix sort')
    parser.add_argument('file')
    parser.add_argument('-n', action='store_true', help='Sort by string unicode point')
    parser.add_argument('-k', type=int, nargs='+', help='Sort by specified key(s)')
    parser.add_argument('-r', action='store_true', help='Reverse')
    parser.add_argument('-f', action='store_ture', help='Ignore case')
    parser.add_argument('-g', action='store_true', help='Attempt to sort numerically')

    return parser.parse_args()


def find_numeric(line):
    for word in line:
        try:
            return int(word)
        except:
            continue


def calculate_unicode_value(line):
    return sum([ord(c) for word in line for c in word])


def main(args):
    txt = sorted([line for line in open(args['file'], 'r').readlines()])

    if args['f']:
        txt = sorted(txt, key=lambda s: s.casefold())
    if args['k']:
        column_keys = itemgetter(*args['k'])
        try:
            txt = sorted(txt, key=lambda s: int(column_keys(s.split())))
        except:
            pass
    if args['g']:
        txt = sorted(txt, key=lambda s: find_numeric(s))
    if args['n']:
        txt = sorted(txt, key=lambda s: calculate_unicode_value(s))
    if args['r']:
        txt = reversed(txt)

    sys.stdout.write('\n'.join(txt))


if __name__ == '__main__':
    main(vars(parse_args()))
