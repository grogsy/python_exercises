# bare implementation of unix grep in python
#
# also imported by find.py

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
        return "File {} does not exist in this directory".format(file)
        

    with open(file, 'r') as current_file:
        contents = current_file.readlines()
        if show_lines:
            # to yield/return a generator expression
            matches = (str(line_num + 1) + ": " + line for line_num, line in enumerate(contents) if re_pattern.search(line))
        else:
            matches = (line for line in contents if re_pattern.search(line))

        return matches
        # print("{} lines contain pattern <{}> in {}:\n".format(len(matches), pattern, file))


if __name__ == '__main__':
    args = parser.parse_args()
    pattern = args.pattern[0]

    for file in args.files:
        print('\n'.join(result for result in search(file, pattern, args.show_lines)))
