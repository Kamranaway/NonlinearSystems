import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random as rand
from matplotlib import style
style.use('dark_background')

#multiLorenz.py pseudorandomly generates multiple Lorenz solutions.

NUM_GENERATIONS = 10 #The number of attractors to generate.

#Parameters are pseudo random
sigma = rand.random() * rand.randrange(0, 100) #Prandtl number
r = rand.random() * rand.randrange(0, 100) #Rayleigh's number
b = rand.random() * rand.randrange(0, 100) + 0.1

#Setup initial conditions
last_x = 0
last_y = 1
last_z = 0

x = [] #All x coordinates
y = [] #ALl y coordinates
z = [] #ALl z coordinates

fig = plt.figure()

ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

def main():
    global sigma
    global r
    global b
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z


    n = NUM_GENERATIONS 
    colors = pl.cm.jet(np.linspace(0,1,n))

    for i in range(0, n):
        gen_lorenz()
        last_x = 0.1
        last_y = 0.1
        last_z = 0.1
        ax.plot3D(x, y, z, color=colors[i])
        sigma = rand.random() * rand.randrange(0, 100)
        r = rand.random() * rand.randrange(0, 100)
        b = rand.random() * rand.randrange(0, 100) + 0.1
        x = []
        y = []
        z = []
    plt.show()

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z
    i = 0
    iteration = 0
    iteration = 0
    while iteration < 100:
        x.append(last_x)
        y.append(last_y)
        z.append(last_z)

        newx = last_x
        newy = last_y
        newz = last_z

        newx += (sigma*(last_y-last_x)) * 0.01
        newy+= ((r*last_x)-last_y-(last_x*last_z)) * 0.01
        newz+= ((last_x*last_y)-(b*last_z)) * 0.01

        last_x = newx
        last_y = newy
        last_z = newz

        iteration += 0.01
main()