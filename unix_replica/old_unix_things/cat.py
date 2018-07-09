# bare version of the cat program in unix

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+',
                    help='File or list of files used by cat')
parser.add_argument('-n', '--numbers', action='store_true',
                    help='Print line numbers')
parser.add_argument('-o', '--outfile', dest='outfile',
                    default=None, type=argparse.FileType('a'),
                    help='destination file to cat to.')

args = parser.parse_args()

print(">>> parsed args: ", args)

for fname in args.files:
    line_num = 1
    in_file = open(fname, 'r')

    if args.numbers:
        for line in in_file.readlines():
            fmt = "\t{}\t{}"
            print(fmt.format(line_num, line))

            if args.outfile:
                args.outfile.write(fmt.format(line_num, line))

            line_num += 1

    else:
        for line in in_file.readlines():
            print(line)

            if args.outfile:
                args.outfile.write(line)

    in_file.close()
