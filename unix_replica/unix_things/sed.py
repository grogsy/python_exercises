import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='bare implementation of unix sed')
    parser.add_argument('file', type=str)
    parser.add_argument('-s', type=str, help='search string or regex to replace')
    parser.add_argument('-g', type=str, help='replacement expression')
    parser.add_argument('-w', action='store_true', help='write change to current file')
    return parser.parse_args()


def re_replace(txt, new_exp, old_exp):
    return '\n'.join(old_exp.sub(new_exp, line) for line in txt)


def main(args):
    target = re.compile(args['s'])
    replacement  = args['g']

    with open(args['file'], 'r+') as f:
        txt = f.readlines()
        # clean txt list of any excess/stray new-lines
        txt = [line.strip('\n') for line in txt]
        txt = [line for line in txt if line]
        txt = re_replace(txt, replacement, target)
        if args['w']:
            f.seek(0)
            f.write(txt)

    # We capture the data stream to send up the command pipe
    sys.stdout.write(txt)

if __name__ == '__main__':
    main(vars(parse_args()))
