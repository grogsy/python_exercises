import argparse
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser(description='Unix tail')
    parser.add_argument('file')
    parser.add_argument('-n', type=int, default=10, help='print out last n lines(default:10)')
    parser.add_argument('-s', metavar='--sleep-interval', type=float, default=1.0,
                        help='with -f sleep for n seconds(default:1s)')
    parser.add_argument('-f', action='store_true', help='continue outputting as file updates content')

    return parser.parse_args()


def main(args):
    amt = args['n']
    with open(args['file'], 'r+') as f:
        sys.stdout.write(''.join(f.readlines()[-amt:]))
        if args['f']:
            while True:
                f.seek(0)
                time.sleep(args['s'])
                sys.stdout.write(''.join(f.readlines()[-amt:]))


if __name__ == '__main__':
    main(vars(parse_args()))
