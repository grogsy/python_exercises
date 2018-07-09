import glob
import subprocess

DEST = 'old_unix_things'
for f in glob.iglob('*.py'):
    subprocess.run(['mv', f, DEST])
