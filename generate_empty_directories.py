import os
import random


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def make_dir(make_files=False):
    for i in range(5):
        dir_name = ''.join(random.choice(alphabet) for _ in range(5))
        os.mkdir(dir_name)
        print("%s succesfully created" % dir_name)
        if make_files:
            mkf(dir_name)


def mkf(directory, amt=2):
    for i in range(amt):
        file_name = ''.join(random.choice(alphabet) for _ in range(5))
        full_name = os.path.join(directory, file_name)
        with open(full_name, 'w') as f:
            f.write(''.join(random.choice(alphabet) for _ in range(5)))
        print("%s successfully created" % full_name)


