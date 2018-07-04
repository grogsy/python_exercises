import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Unix cut")
    parser.add_argument('file', type=str)
    parser.add_argument('-d', type=str, help="Delimiter to indicate fields")
    parser.add_argument('-f', type=str, help="Dash(-) separated values for slice grabbing")
    parser.add_argument('-c', type=str, help="Comma separated values for index grabbing")
    parser.add_argument('-s', action='store_true',
                        help='if -d do not print lines without delimiter')
    return parser.parse_args()


def get_slice(fields):
    lower, upper = fields.split('-')

    try:
        lower = int(lower) - 1
    except ValueError:
        lower = None
    try:
        upper = int(upper)
    except ValueError:
        upper = None

    return slice(lower, upper)


def main(args):
    txt = [line for line in open(args['file'], 'r').readlines()]
    delimiter = args['d']
    fields = args['f']
    chars = args['c']

    if delimiter and not fields:
        exit("Cannot operate with delimiter and no fields")
    if fields and chars:
        exit("Can only choose one of these options: -f/-c")

    if fields:
        if args['s']:
            txt = [line for line in txt if delimiter in line]
        indices = get_slice(fields)
        build = []
        for line in txt:
            build.append(delimiter.join(line.split(delimiter)[indices]))
        sys.stdout.write(''.join(build))

    elif chars:
        build = []

        if '-' in chars:
            indices = get_slice(chars)
            for line in txt:
                build.append(line[indices])
            sys.stdout.write('\n'.join(build))

        elif ',' in chars:
            indices = chars.split(',')
            if '' in indices:
                exit("Can't leave stray comma(,) in -c")
            for line in txt:
                build.append(''.join(line[int(index)] for index in indices))
            sys.stdout.write('\n'.join(build))

        else:
            # Only one index given
            index = int(chars)
            sys.stdout.write('\n'.join(line[index] for line in txt))


if __name__=='__main__':
    main(vars(parse_args()))
