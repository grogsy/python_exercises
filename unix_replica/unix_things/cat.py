import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-n', action='store_true', help='print line numbers')

    return parser.parse_args()


def main(args):
    txt = open(args['file'], 'r').readlines()
    if args['n']:
        fmt = '{0:>{w}} {1}'
        new_txt = enumerate(txt, start=1)
        num_width = len(str(max((num for num, _ in new_txt))))
        new_txt = [fmt.format(num, line, w=num_width) for num, line in new_txt]
        sys.stdout.write('\n'.join(new_txt))
    else:
        sys.stdout.write('\n'.join(line for line in txt))


if __name__ == '__main__':
    main(vars(parse_args()))
