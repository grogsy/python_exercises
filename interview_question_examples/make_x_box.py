# Some interview question posted on r/programmerhumor

def make_x_box(width, height):
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


# less hacky and more box-y
def make_x_box(height):
    width = height + 1
    
    for y in range(height+1):
        build = 'x'
        for x in range(width):
            if y == 0 or y == height or x==y or y+x == width-1:
                build += 'x'
            else:
                build += ' '
        build += 'x'
        print(build)
        
print(make_x_box(10))
