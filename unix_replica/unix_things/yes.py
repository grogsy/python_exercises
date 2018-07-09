import argparse
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser(description='Unix yes command with a custom option')
    parser.add_argument('string', type=str, nargs='?', default='y', help='String to stdout until terminated')
    parser.add_argument('--delay', type=float, default=.66, help='time between affirming messages')

    return parser.parse_args()


def main(args):
    while True:
        sys.stdout.write(args['string'])
        sys.stdout.write('\n')
        time.sleep(args['delay'])


if __name__ == '__main__':
    main(vars(parse_args()))
