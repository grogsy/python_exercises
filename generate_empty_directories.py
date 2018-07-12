import os
import random


alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(5):
    dir_name = ''.join(random.choice(alphabet) for _ in range(5))
    os.mkdir(dir_name)
