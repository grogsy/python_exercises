import datetime as dt
import random
import time

seed = range(100000000, int(time.time()))

# Just an example of time format, plenty different ones to use from datetime.strftime
fmt = '%a %m/%d/%Y %I:%M:%S%p'

l = []
for _ in range(10):
    #print(dt.datetime.utcfromtimestamp(random.choice(seed)).strftime(fmt))
    l.append(dt.datetime.utcfromtimestamp(random.choice(seed)).strftime(fmt))

with open('random_dates.txt', 'w') as f:
    f.write('\n'.join(l))
