import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style

style.use('dark_background')

#lorenzrayleigh.py graphs the behavior of the lorenz system as rayleigh's number increases.

RATE_INCREMENT = 0.01

#Setup parameters
sigma = 10 #Prandtl number
r = 0 #Rayleigh's number
b = (8/3)

#Setup initial conditions
last_x = 0 
last_y = 1
last_z = 0

r_map = []
x_map = []
y_map = []
z_map = []

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel('rayleigh\'s number')
ax.set_ylabel('z')

def main():

    gen_map()
    plt.show()

def gen_map():
    global r
    global r_map
    global x_map
    global y_map
    global z_map
    global last_x
    global last_y
    global last_z

    while r <= 30:
        last_x = 0 
        last_y = 1
        last_z = 0
        
         #plot values of x
        for i in range(0, 10000):
            newx = last_x
            newy = last_y
            newz = last_z

            newx += (sigma*(last_y-last_x)) * 0.01

            newy+= ((r*last_x)-last_y-(last_x*last_z)) * 0.01

            newz+= ((last_x*last_y)-(b*last_z)) * 0.01

            last_x = newx
            last_y = newy
            last_z = newz

        #plot values of x
        for i in range(0, 300):
            r_map.append(r)
            x_map.append(last_x)
            z_map.append(last_z)
            y_map.append(last_y)

            newx = last_x
            newy = last_y
            newz = last_z

            newx += (sigma*(last_y-last_x)) * 0.01

            newy+= ((r*last_x)-last_y-(last_x*last_z)) * 0.01

            newz+= ((last_x*last_y)-(b*last_z)) * 0.01

            last_x = newx
            last_y = newy
            last_z = newz


        r += RATE_INCREMENT
    plt.scatter(r_map, z_map, 0.001)

main()