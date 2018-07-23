import argparse
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='bare implementation of unix sed')
    parser.add_argument('files', type=str, nargs='*')
    parser.add_argument('expression', metavar='s/<OLD>/<NEW>/opts<g>', type=str, help='use this template to search and replace text')
    parser.add_argument('-w', action='store_true', help='write change to current file')
    parser.add_argument('-i', action='store_true', help='case-insensitive')
    return parser.parse_args()


def parse_sed_args(args):
    sed_parser = argparse.ArgumentParser()
    sub_parser = sed_parser.add_subparsers()
    substitution_parser = sub_parser.add_parser('s')
    substitution_parser.add_argument('old', type=str)
    substitution_parser.add_argument('new', type=str)
    substitution_parser.add_argument('extra-opts', type=str)

    return sed_parser.parse_args(args)



def main(args):
    flag = re.IGNORECASE if args['i'] else 0

    sed_args = args['expression'].split('/')

    regex_args = vars(parse_sed_args(sed_args))

    old_exp = re.compile(regex_args['old'], flags=flag)
    new_exp = regex_args['new']

    # For now we have global replacing by default
    txt = [line.strip('\n') for f in args['files'] for line in open(f, 'r').readlines()]
    txt = [old_exp.sub(new_exp, line) for line in txt]
    if args['w']:
        with open(args['file'], 'w') as f:
            f.write('\n'.join(txt))

    # We capture the data stream to send up the command pipe
    sys.stdout.write('\n'.join(txt))

if __name__ == '__main__':
    main(vars(parse_args()))

