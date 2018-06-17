import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(description='Stream editor')
    
    parser.add_argument('files', type=str, nargs='+')

    parser.add_argument('-s', type=str, help='Use this to search for a literal string to substitute')

    parser.add_argument('-e', type=str, help='Use this to search for a regular expression substitution')

    parser.add_argument('-g', type=str, help='The string to replace')

    return parser.parse_args()


def re_replace(txt, pattern, target):
    return '\n'.join(re.sub(pattern, target, line) for line in text)


def str_replace(txt, sub, target):
    return '\n'.join(line.replace(target, sub) for line in txt)


if __name__=='__main__':
    args = vars(parse_args())

    files = args['files']
    target = args['g']

    if args['s'] and args['e']:
        exit("Can't substitute using both regex and literal string")

    for file in files:
        with open(file, 'r+') as cur:
            txt = cur.readlines()
            cur.seek(0)
            if args['s']:
                sub = args['s']
                txt = str_replace(txt, sub, target)
            elif args['e']:
                pattern = re.compile(args['e'])
                txt = re_replace(txt, pattern, target)
            cur.write(txt)
            
