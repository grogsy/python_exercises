import argparse
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser(description='Unix tail')
    parser.add_argument('file')
    parser.add_argument('-n', type=int, default=10, help='print out last n lines(default:10)')

    return parser.parse_args()


def main(args):
    amt = args['n']
    with open(args['file'], 'r+') as f:
        sys.stdout.write(''.join(f.readlines()[-amt:]))


if __name__ == '__main__':
    main(vars(parse_args()))
