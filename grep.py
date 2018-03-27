# bare implementation of unix grep in python
#
# works like so :
# grep <files to search> <pattern> <other opts>
# for some reason the file to be searched needs to go first
# or the program won't work
#
# returns :
# <num> lines contain <pattern> in <file>
# etc

import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument('files', type=str, nargs='+',
                    help='File or list of files to search')
parser.add_argument('-p', '--pattern', type=str,
                    nargs='+', dest='pattern',
                    help='Pattern to search for')
parser.add_argument('-l', '--lines', dest='show_lines',
                    action='store_true',
                    help='Give this argument to show what line number pattern occurs in')


def search(file, pattern, show_lines=False):

    re_pattern = re.compile(pattern)

    if file not in os.listdir():
        print("File {} does not exist in this directory".format(file))
        return

    with open(file, 'r') as current_file:
        contents = current_file.readlines()
        if show_lines:
            matches = [str(line_num + 1) + ": " + line for line_num, line in enumerate(contents) if re_pattern.search(line)]
        else:
            matches = [line for line in contents if re_pattern.search(line)]

        if not matches:
            print("No matches of <{}> occured for file {}".format(pattern, file))
            return

        print("{} lines contain pattern <{}> in {}:\n".format(len(matches), pattern, file))

        for line in matches:
            print(line)


if __name__ == '__main__':
    args = parser.parse_args()
    pattern = args.pattern[0]

    for file in args.files:
        search(file, pattern, args.show_lines)
