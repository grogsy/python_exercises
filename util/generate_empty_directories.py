'''
Used this to test rm.py
Go to any throw-away directory you choose and and run generate_random_directories.py
'''
import argparse
import os
import random


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def make_dir(make_files=False, num_of_files=None):
    for i in range(5):
        dir_name = ''.join(random.choice(alphabet) for _ in range(5))
        os.mkdir(dir_name)
        print("%s succesfully created" % dir_name)
        if make_files:
            mkf(dir_name, num_of_files)


def mkf(directory, amt=2):
    for i in range(amt):
        file_name = ''.join(random.choice(alphabet) for _ in range(5))
        full_name = os.path.join(directory, file_name)
        with open(full_name, 'w') as f:
            f.write(''.join(random.choice(alphabet) for _ in range(5)))
        print("%s successfully created" % full_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-mkf', action='store_true')
    parser.add_argument('-n', metavar='--number-of-files', type=int, default=2,
                        help='with -mkf specify how many throwaway files to put in each folder')
    args = vars(parser.parse_args())

    if args['mkf']:
        amount = args['n'] or 2
        make_dir(make_files=True, num_of_files=amount)
    else:
        make_dir()
