# Couldn't find a solution that worked for me to pipe a list of files to wc that would produce the line count for all the files
# So this is a script that tries
# On the one hand you can I could do something like cat <list of files> | wc -l but its kind of pointless if there are too many files

import glob
import subprocess


count = 0

# Count the lines of all python files in cwd
for f in glob.iglob("*.py"):
    res = subprocess.run(['wc', '-l', f], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
    count += int(res)
    
print(res)
