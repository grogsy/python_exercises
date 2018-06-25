import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='unix grep')
    parser.add_argument('file', type=str)
    parser.add_argument('-e', type=str, help='regex pattern')
    parser.add_argument('-i', action='store_true', help='ignore case')
    parser.add_argument('-v', action='store_true', help='invert matching(get non-matching lines)')
    parser.add_argument('-c', action='store_true', help='instead of printing matches, print match count instead')
    parser.add_argument('-n', action='store_true', help='prefix each line with a line number')
    parser.add_argument('-m', type=int, help='get the first n occurences of a match')

    return parser.parse_args()


def main(args):
    txt = [line.strip('\n') for line in open(args['file'], 'r').readlines()]
    if args['n']:
        ntmp = list(enumerate(txt, start=1))
        fmt = '{0:>w}} {1}'
        padding_width = len(str(max((num for num, _ in ntmp))))
        txt = [fmt.format(num, line, w=padding_width) for num, line in ntmp]

    iflag = re.IGNORECASE if args['i'] else 0
    target_exp = re.compile(args['e'], flags=iflag)

    if args['v']:
        filtered_txt = [line for line in txt if not target_exp.search(line)]
    else:
        filtered_txt = [line for line in txt if target_exp.search(line)]

    if args['m']:
        filtered_txt = filtered_txt[:args['m']]

    if args['c']:
        sys.stdout.write(str(len(filtered_txt)))
    else:
        sys.stdout.write('\n'.join(filtered_txt))

if __name__ == '__main__':
    main(vars(parse_args()))
