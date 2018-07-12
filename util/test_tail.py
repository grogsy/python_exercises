import time
for i in range(100):
    f = open('foo.txt', 'a')
    fmt = "Foo! {}\n"
    print("Wrote 'Foo! {}'".format(i))
    f.close()
    time.sleep(1.75)

# Run this in a separate process while running "python tail.py foo.txt -f -s 3" in another
