import argparse
import glob
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='unix find')
    parser.add_argument('-cd', type=str, help='directory to search(default is cwd)')
    parser.add_argument('-L', action='store_true', help='Follow symbolic links(get abs path)')
    parser.add_argument('-name', type=str, help='get matches with the specified pattern')
    parser.add_argument('-print', action='store_true', help='display results')

    return parser.parse_args()


def main(args):
    directory = args['cd'] or '.'

    os.chdir(directory)

    res = [link for link in glob.iglob(args['name'])]
    if args['L']:
        res = [os.path.realpath(link) for link in res]

    if args['print']:
        sys.stdout.write('\n'.join(res))


if __name__ == '__main__':
    main(vars(parse_args()))
