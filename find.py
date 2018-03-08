import argparse
import os

parser = argparse.ArgumentParser(description='Find files matching a text pattern')

parser.add_argument('--match', dest='patterns',
                    type=str, nargs='+',
                    help='supply patterns to look for with this arg.')

parser.add_argument('--print', dest='display', action='store_true',
                    help='supply this arg to print to std out.')

parser.add_argument('--dir', dest='arg_path', type=str, default=None,
                    help='supply this arg to specify a directory to search, checks current working directory if omitted')

parser.add_argument('--merge', dest='merge', action='store_true',
                    help='If 2 or more patters are supplied filter through both.')  # not sure how to implement this lol

args = parser.parse_args()

patterns = args.patterns

if args.arg_path:
    try:
        os.chdir(args.arg_path)
    except FileNotFoundError:
        print("Error: Couldn't locate specified path")
        exit(1)

if args.display:
    for pattern in patterns:
        matches = [file for file in os.listdir() if pattern in file]
        print("{} matches found for {} in {}:\n".format(len(matches),
                                                        pattern, os.getcwd()))
        for file in matches:
            print(file)
