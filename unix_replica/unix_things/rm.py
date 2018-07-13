import argparse
import os
import sys


PROMPT = "Really delete %s? (Y)es/(N)o/Yes to (A)ll, Ctrl+C to break out: "
VERBOSE = "\nDeleting %s\n"
SUCCESS = "Successfully deleted %s\n"


def parse_args():
    parser = argparse.ArgumentParser()
    # nargs='?': this indicates optional positional argument
    # preceding a regex with '?' means 0 or more
    parser.add_argument('file', metavar='file(s)/directory', nargs='?')
    parser.add_argument('-i', action='store_true', help='prompt before every removal')
    parser.add_argument('-d', action='store_true', help='delete empty directories')
    parser.add_argument('-v', action='store_true', help='more detail on removals being done')
    parser.add_argument('-r', action='store_true', help='remove a directory recursively')
    return parser.parse_args()


def main(args):
    if args['d']:
       remove_empty_directories(args['i'], args['v'])
    elif args['r']:
        directory = args['file']
        remove_recursively(directory, args['i'], args['v'])
    else:
        if args['i']:
            ans = input(PROMPT % args['file']).lower()
            if 'y' in ans:
                if args['v']:
                    sys.stdout.write(VERBOSE % args['file'])
            else:
                exit()
        os.remove(args['file'])
        sys.stdout.write(SUCCESS % args['file'])


def remove_empty_directories(interactive=None, verbose=None):
    dirs = [link for link in os.listdir() if os.path.isdir(link)]
    for d in dirs:
        if not os.listdir(d):
            if interactive:
                ans = input(PROMPT % d).lower()
                if 'y' in ans:
                    pass
                elif 'a' in ans:
                    interactive = False
                else:
                    continue
            if verbose:
                sys.stdout.write(VERBOSE % d)
            os.rmdir(d)
            sys.stdout.write(SUCCESS % d)

    exit()

def remove_recursively(directory, interactive=None, verbose=None):
    os.chdir(directory)
    for link in os.listdir():
        if interactive:
            ans = input(PROMPT % link).lower()
            if 'y' in ans:
                pass
            elif 'a' in ans:
                interactive = False
            else:
                continue
        if os.path.isdir(link):
            remove_recursively(link, interactive, verbose)
        else:
            if verbose:
                sys.stdout.write(VERBOSE % link)
            os.remove(link)
            sys.stdout.write(SUCCESS % link)
    os.chdir('..')
    os.rmdir(directory)
    sys.stdout.write(SUCCESS % directory)

if __name__ == '__main__':
    main(vars(parse_args()))
