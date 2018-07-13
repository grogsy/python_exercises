import argparse
import sys

# For formatting display data with line numbers
LINE_FMT = '{0:>{w}} {1}'


def parse_args():
    parser = argparse.ArgumentParser("Unix cat. Run without a file arg then echo to stdout.")
    parser.add_argument('file', nargs='?')
    parser.add_argument('-n', action='store_true', help='print line numbers')
    parser.add_argument('-s', action='store_true', help='squeeze blank lines')
    parser.add_argument('-b', action='store_true', help='like -n but only numbers for non-empty lines')
    parser.add_argument('-E', action='store_true', help='denote eol with "$"')
    parser.add_argument('-T', action='store_true', help='denote tabs(\\t) as ^I')

    return parser.parse_args()


def main(args):
    if not args['file']:
        c = 1
        while True:
            txt = input()
            if args['E']:
                txt += '$'
            if args['T']:
                txt = txt.replace('\t', '^I')
            if args['n']:
                txt = LINE_FMT.format(c, txt, w=5)
                c+=1
            sys.stdout.write(txt+'\n')
    else:
        txt = [line.strip('\n') for line in open(args['file'], 'r').readlines()]
        if args['s']:
            txt = [line for line in txt if line]
        if args['E']:
            txt = [line+'$' for line in txt]
        if args['T']:
            txt = [line.replace('\t', '^I') for line in txt]

        if args['n']:
            new_txt = list(enumerate(txt, start=1))
            num_width = len(str(len(txt)))
            sys.stdout.write('\n'.join(LINE_FMT.format(num, line, w=num_width) for num, line in new_txt))
        elif args['b']:
            c = 1
            new_txt = []
            width = len(str(len(txt)))
            for line in txt:
                if line:
                    new_txt.append(LINE_FMT.format(c, line, w=width))
                    c += 1
                else:
                    new_txt.append(line)
            sys.stdout.write('\n'.join(new_txt))
        else:
            sys.stdout.write('\n'.join(line for line in txt))


if __name__ == '__main__':
    main(vars(parse_args()))
