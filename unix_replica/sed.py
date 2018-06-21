import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(description='bare implementation of unix sed')
    parser.add_argument('file', type=str, nargs='+')
    parser.add_argument('-s', type=str, help='search string pattern')
    parser.add_argument('-e', type=str, help='search regex pattern')
    parser.add_argument('-g', type=str, help='pattern to sub')
    return parser.parse_args()


def re_replace(txt, pattern, target):
    return '\n'.join(re.sub(pattern, target, line) for line in txt)


def str_replace(txt, target, sub):
    return '\n'.join(line.replace(target, sub) for line in txt)


def main(args):
    target = args['g']
    with open(args['file'], 'r+') as f:
        txt = f.readlines()
        f.seek(0)
        if args['s']:
            sub = args['s']
            txt = str_replace(txt, target, sub)
        elif args['e']:
            pattern = re.compile(args['e'])
            txt = re_replace(txt, pattern, target)
        f.write(txt)
    return txt



if __name__ == '__main__':
    main(vars(parse_args()))
