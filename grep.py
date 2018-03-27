# bare implementation of unix grep in python
#
# works like so :
# grep <files to search> <pattern> <other opts>
# exactly in this order or for some reason the program will break
# i might just make files to search resolve to a destination variable
# in order to work around this
#
# returns :
# <num> matches found for <pattern> in <file>
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

args = parser.parse_args()

# args.pattern returns a list even its one item, so
pattern = re.compile(args.pattern[0])

for file in args.files:

    if file not in os.listdir():
        print("File {} does not exist in this directory".format(file))
        continue

    with open(file, 'r') as current_file:
        contents = current_file.readlines()
        if args.show_lines:
            matches = [str(line_num + 1) + " " + line for line_num, line in enumerate(contents) if pattern.search(line)]
        else:
            matches = [line for line in contents if pattern.search(line)]

        if not matches:
            print("No matches of <{}> occured for {}".format(args.pattern[0], file))
            continue

        print("{} lines contain pattern <{}> in {}:\n".format(len(matches), args.pattern[0], file))

        for line in matches:
            print(line)
