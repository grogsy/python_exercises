import os
import random


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def make_dir():
    for i in range(5):
        dir_name = ''.join(random.choice(alphabet) for _ in range(5))
        os.mkdir(dir_name)
        print("%s succesfully created" % dir_name)



