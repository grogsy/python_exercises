# I hate this
# Some interview question posted on r/programmerhumor

def make_x_box(width, height):
    # To make this frickin box more symmetrical
    height += 2
    
    for y in range(height):
        build = 'x'
        for x in range(width):
            if y == 0 or y == height-1 or x==y-1 or y+x == width:
                build += 'x'
            else:
                build += ' '
        build += 'x'
        print(build)
make_x_box(10,10)
