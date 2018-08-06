import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='unix grep')
    parser.add_argument('files', type=str, nargs='*')
    parser.add_argument('-e', type=str, metavar='<pattern>', help='regex pattern')
    parser.add_argument('-i', action='store_true', help='ignore case')
    parser.add_argument('-v', action='store_true', help='invert matching(get non-matching lines)')
    parser.add_argument('-c', action='store_true', help='instead of getting matches, get the match count')
    parser.add_argument('-n', action='store_true', help='prefix each line with a line number')
    parser.add_argument('-m', type=int, metavar='<N>', help='get the first N occurences of a match')
    parser.add_argument('-m--last', type=int, metavar='<N>', help='like -m but last N occurences')

    return parser.parse_args()


def main(args):
    txt = [line.strip('\n') for f in args['files'] for line in open(f)]
    if args['n']:
        ntmp = list(enumerate(txt, start=1))
        fmt = '{0:>{w}} {1}'
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
    elif args['m__last']:
        filtered_txt = filtered_txt[-args['m__last']:]

    if args['c']:
        sys.stdout.write(str(len(filtered_txt)))
    else:
        sys.stdout.write('\n'.join(filtered_txt))

if __name__ == '__main__':
    main(vars(parse_args()))
