import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='bare implementation of unix sed')
    parser.add_argument('file', type=str)
    parser.add_argument('-s', type=str, help='search string pattern')
    parser.add_argument('-e', type=str, help='search regex pattern')
    parser.add_argument('-g', type=str, help='pattern to sub')
    parser.add_argument('-w', action='store_true', help='write change to current file')
    return parser.parse_args()


def re_replace(txt, pattern, target):
    return '\n'.join(re.sub(pattern, target, line) for line in txt)


def str_replace(txt, target, sub):
    return '\n'.join(line.replace(target, sub) for line in txt)


def main(args):
    target = args['g']
    with open(args['file'], 'r+') as f:
        txt = f.readlines()
        # clean txt list of any excess/stray new-lines
        txt = [line.strip('\n') for line in txt]
        txt = [line for line in txt if line]
        if args['s']:
            sub = args['s']
            txt = str_replace(txt, target, sub)
        elif args['e']:
            pattern = re.compile(args['e'])
            txt = re_replace(txt, pattern, target)
        if args['w']:
            f.seek(0)
            f.write(txt)

    # We capture the data stream to send up the command pipe
    sys.stdout.write(txt)

if __name__ == '__main__':
    main(vars(parse_args()))
