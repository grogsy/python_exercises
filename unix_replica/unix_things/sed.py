import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='bare implementation of unix sed')
    parser.add_argument('file', type=str)
    parser.add_argument('-s', type=str, metavar='<OLD>', help='search string or regex to replace')
    parser.add_argument('-g', type=str, metavar='<NEW>', help='replacement expression')
    parser.add_argument('-w', action='store_true', help='write change to current file')
    parser.add_argument('-i', action='store_true', help='case-insensitive')
    return parser.parse_args()


def main(args):
    # for use with ignore case option
    flag = 0
    if args['i']:
        flag = re.IGNORECASE
    old_exp = re.compile(args['s'], flags=flag)
    new_exp = args['g']

    with open(args['file'], 'r+') as f:
        txt = [line.strip('\n') for line in f.readlines()]
        # clean txt list of any excess/stray new-lines
        txt = [line for line in txt if line]
        txt = '\n'.join(old_exp.sub(new_exp, line) for line in txt)
        if args['w']:
            f.seek(0)
            f.write(txt)

    # We capture the data stream to send up the command pipe
    sys.stdout.write(txt)

if __name__ == '__main__':
    main(vars(parse_args()))
