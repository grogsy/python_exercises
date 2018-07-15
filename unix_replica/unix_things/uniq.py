import argparse
from collections import Counter
import sys



def parse_args():
    parser = argparse.ArgumentParser(description='unix uniq in python')
    parser.add_argument('files', type=str, nargs='*')
    parser.add_argument('-d', action='store_true', help='print duplicate lines')
    parser.add_argument('-c', action='store_true', help='show lines and their occurrence')
    return parser.parse_args()


def main(args):
    txt = [line.strip('\n') for f in args['files'] for line in open(f, 'r').readlines()]
    # Don't want to sort empty lines
    txt = [line for line in txt if line]

    counter = Counter(txt)
    if args['d']:
        sys.stdout.write('\n'.join(line for line in counter if counter[line] > 1))
    elif args['c']:
        fmt = '%s:\n\t%d'
        sys.stdout.write('\n'.join(fmt % (line, count) for line, count in counter.items()))
    else:
        sys.stdout.write('\n'.join(line for line in counter.keys()))


if __name__ == '__main__':
    main(vars(parse_args()))
