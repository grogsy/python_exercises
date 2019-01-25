from random import choice
import matplotlib.pyplot as plt

#code example is mostly taken from the Python Crash Course

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
            
        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
                
            #calculate the next x and y values
            next_x = self.x_values[-1] + x_direction
            next_y = self.y_values[-1] + y_direction
                
            self.x_values.append(next_x)
            self.y_values.append(next_y)


def generate_random_walks():
    while True:
        rw = RandomWalk(50000)
        rw.fill_walk()
        
        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,
                    edgecolor='none', s=5)
        
        #emphasize the first and last points
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
        
        #plt.axes().get_xaxis().set_visible(False)
        #plt.axes().get_yaxis().set_visible(False)
        
        plt.show()
        
        keep_running = input("Another? ")
        
        if keep_running == 'n':
            break
