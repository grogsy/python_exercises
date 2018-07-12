import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Unix head')
    parser.add_argument('file')
    parser.add_argument('-n', type=int, default=10,
                        help='Print first n lines of a file(default:10')

    return parser.parse_args()


def main(args):
    sys.stdout.write(''.join(open(args['file']).readlines()[args['n']]))


if __name__ == '__main__':
    main(vars(parse_args()))
