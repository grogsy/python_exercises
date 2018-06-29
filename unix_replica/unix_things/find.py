import argparse
import glob
import os
import sys

# Note to self: os.scandir(...) is another interesting option as it returns an iterable of dir entry objects of the files gotten
# dir entry objects also contain relevant info such as .inode, .id_dir(), .is_file, stat(), name, and path
# in fact dir_entry.stat() returns stat info of the file that is equivalent to os.stat(dir_entry.name)


def parse_args():
    parser = argparse.ArgumentParser(description='unix find')
    parser.add_argument('-cd', type=str, metavar='<DIR>', help='directory to search(default is cwd)')
    parser.add_argument('-L', action='store_true', help='Follow symbolic links(get abs path)')
    parser.add_argument('-name', type=str, metavar='<pattern>', help='get matches with the specified (regex) pattern')
    parser.add_argument('-print', action='store_true', help='display results')
    parser.add_argument('-empty', action='store_true', help='get matches that are either empty or a directory')
    parser.add_argument('-readable', action='store_true', help='get matches that are readable by the current user')
    parser.add_argument('-executable', action='store_true', help='same as -readable but checks for x-permision')
    parser.add_argument('-writable', action='store_true', help='same as -readable but checks for w-permission')
    parser.add_argument('-samefile', type=str, metavar='<name>', help='get matches which have the same inode as <name>')
    parser.add_argument('-size', type=int, metavar='<n>', help='get matches that have <n> size')
    parser.add_argument('-amin', type=int, metavar='<n>', help='File accessed <n> minutes ago')
    parser.add_argument('-cmin', type=int, metavar='<n>', help='File was changed <n> minutes ago')
    parser.add_argument('-mmin', type=int, metavar='<n>', help='File was modified <n> minutes ago')
    parser.add_argument('-atime', type=int, metavar='<n>', help='File was accessed <n> days ago')
    parser.add_argument('-ctime', type=int, metavar='<n>', help='File was changed <n> days ago')
    parser.add_argument('-mtime', type=int, metavar='<n>', help='File was modified <n> days ago')

    return parser.parse_args()


def check_by_time(links, time_args):
    import time

    for k, v in time_args.items():
        if k.endswith('min'):
            seconds = 60
        elif k.endswith('time'):
            seconds = 86400

        adj = v * seconds
        now = time.time()
        earliest = now - adj

        if k.startswith('a'):
            links = [link for link in links if os.stat(link).st_atime >= earliest]
        elif k.startswith('c'):
            links = [link for link in links if os.stat(link).st_ctime >= earliest]
        elif k.startswith('m'):
            links = [link for link in links if os.stat(link).st_mtime >= earliest]

    return links


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

    # Check several access times
    time_args = {k: v for k, v in args.items() if (k.endswith('min') or k.endswith('time')) and v}
    res = check_by_time(res, time_args)

    # Check other stats. Other find opts that need implementation: anewer, cnewer, gid, mnewer,path
    # Check man find just to make sure if I missed anything else
    if args['size']:
        res = [link for link in res if os.stat(link).st_size == args['size']]
    if args['samefile']:
        res = [link for link in res if os.stat(link).st_ino == os.stat(args['samefile']).st_ino]
    if args['empty']:
        tmp = []
        for link in res:
            try:
                if os.path.isdir(link) or not open(link, 'r').readlines() or not open(link, 'rb').readlines():
                    tmp.append(link)
            except PermissionError: # Can't tell if it contains anything; no read permission. Just assume it does
                pass
            except UnicodeError:    # The fact that we run into a unicode error means it contains something, skip it
                pass
        res = tmp

    if args['print']:
        sys.stdout.write('\n'.join(res))


if __name__ == '__main__':
    main(vars(parse_args()))
