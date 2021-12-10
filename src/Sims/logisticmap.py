import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#logisticmap.py is a program that generates a logistic map.

r = 2.9 #Initial value for r
RATE_INCREMENT = 0.0001 #A higher value (where the value is less than 1) will decrease the time it takes to generate, but also will decrease resolution.

r_map = []
x_map = []

fig = plt.figure()
ax = plt.axes()
ax.set_ylabel('Growth Rate')

def main():
    
    gen_map()
    plt.show()

def gen_map():
    global r
    global r_map
    global x_map

    iteration = 0

    while r <= 4:
        x = 0.1

        #settle to behavior
        for i in range(0, 300):
            x = r*x*(1-x)

        #plot values of x
        for i in range(0, 300):
            #ax.plot(r, x, color = 'white')
            r_map.append(r)
            x_map.append(x)
            x = r*x*(1-x)


        r += RATE_INCREMENT
    plt.scatter(r_map, x_map, 0.01)

main()