import argparse
import os
import grep
import re

# Note to self about argparse:
#   supplying 'nargs="+"' as an argument to add_argument
#   forces it to turn into a list of arguments
#   instead of just a single arg

parser = argparse.ArgumentParser(description='Find files matching a text pattern')

parser.add_argument('--match', '-m', dest='pattern',
                    type=str,
                    help='Match a file name in the directory.')

parser.add_argument('--dir', '-d', dest='arg_path', type=str, default=None,
                    help='Specify a directory to search, default=cwd')

parser.add_argument('-s', dest='sub_grep', type=str, default=None,
                    help='Specify a term to search for within matched filenames')


def find(pattern, path_specified=None, sub_grep=None):
    re_pattern = re.compile(pattern)
    if path_specified:
        try:
            os.chdir(path)
        except FileNotFoundError:
            print("Unable to locate specified path")
            return
    matches = [file for file in os.listdir() if re_pattern.search(file)]
    if not matches:
        return 'No files match the specified pattern'
    if sub_grep:
        for result in generate_sub_greps(matches, sub_grep):
            print('\n'.join(line for line in result))
    else:
        print('\n'.join(file for file in matches))


def generate_sub_greps(matches, sub_grep):
    for file in matches:
        print("Match in {}\n".format(file))
        yield grep.search(file, sub_grep, True)


if __name__ == '__main__':

    args = parser.parse_args()
    print(args)

    path = args.arg_path
    pattern = args.pattern
    sub_grep = args.sub_grep

    find(pattern, path, sub_grep)
