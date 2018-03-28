# shoddy cut mimic needs work
# example: can't parse whitespace(e.g. ' ') as a delimiter..

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', type=str)

parser.add_argument('-d', type=str, dest='delim', default=None,
                    help='Delimiter that splits the target text')

parser.add_argument('-f', type=str, dest='fields',
                    help='Specify the slice of each line of text to print out. Must be separated by -')


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


def process_file(file, fields, delimiter=None):

    indices = get_slice(fields)

    if delimiter:
        for line in file:
            print(delimiter.join(line.split(delimiter)[indices]))
    else:
        for line in file:
            print(line[indices])


if __name__ == '__main__':
    args = parser.parse_args()

    f = open(args.file, 'r').readlines()

    if args.delim:
        process_file(f, args.fields, delimiter=args.delim)
    else:
        process_file(f, args.fields)
