import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-n', action='store_true', help='print line numbers')
    parser.add_argument('-s', action='store_true', help='squeeze blank lines')

    return parser.parse_args()


def main(args):
    txt = [line.strip('\n') for line in open(args['file'], 'r').readlines()]
    if args['s']:
        txt = [line for line in txt if line]
    if args['n']:
        fmt = '{0:>{w}} {1}'
        new_txt = list(enumerate(txt, start=1))
        num_width = len(str(max((num for num, _ in new_txt))))
        sys.stdout.write('\n'.join(fmt.format(num, line, w=num_width) for num, line in new_txt))
    else:
        sys.stdout.write('\n'.join(line for line in txt))


if __name__ == '__main__':
    main(vars(parse_args()))
