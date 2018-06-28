import argparse
import glob
import os
import sys

# Note to self: os.scandir(...) is another interesting option as it returns an iterable of dir entry objects of the files gotten
# dir entry objects also contain relevant info such as .inode, .id_dir(), .is_file, stat(), name, and path
# in fact dir_entry.stat() returns stat info of the file that is equivalent to os.stat(dir_entry.name)


def parse_args():
    parser = argparse.ArgumentParser(description='unix find')
    parser.add_argument('-cd', type=str, help='directory to search(default is cwd)')
    parser.add_argument('-L', action='store_true', help='Follow symbolic links(get abs path)')
    parser.add_argument('-name', type=str, help='get matches with the specified (regex) pattern')
    parser.add_argument('-print', action='store_true', help='display results')
    parser.add_argument('-empty', action='store_true', help='get matches that are either empty or a directory')
    parser.add_argument('-readable', action='store_true', help='get matches that are readable by the current user')
    parser.add_argument('-executable', action='store_true', help='same as -readable but checks for x-permision')
    parser.add_argument('-writable', action='store_true', help='same as -readable but checks for w-permission')
    parser.add_argument('-samefile', type=str, help='get matches which have the same inode as <name>')
    parser.add_argument('-size', type=int, help='get matches that have n size')

    return parser.parse_args()


def main(args):
    directory = args['cd'] or '.'
    os.chdir(directory)

    res = [link for link in glob.iglob(args['name'])]
    if args['L']:
        res = [os.path.realpath(link) for link in res]

    # Check permissions
    if args['readable']:
        res = [link for link in res if os.access(link, os.R_OK)]
    if args['writable']:
        res = [link for link in res if os.access(link, os.W_OK)]
    if args['executable']:
        res = [link for link in res if os.access(link, os.X_OK)]

    # Check other stats
    if args['size']:
        res = [link for link in res if os.stat(link).st_size == args['size']]

    if args['samefile']:
        res = [link for link in res if os.stat(link).st_ino == os.stat(args['samefile']).st_ino]
    if args['empty']:
        res = [link for link in res if os.path.isdir(link) or not open(link, 'r').readlines()]

    if args['print']:
        sys.stdout.write('\n'.join(res))


if __name__ == '__main__':
    main(vars(parse_args()))
