import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
from matplotlib import style
import random as rand
style.use('dark_background')

#Lorenz.py pseudorandomly generates a lorenz systems.

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

    gen_lorenz()
    ax.plot3D(x, y, z, color='black')

    plt.show()

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z

    iteration = 0
    while iteration < 5000:
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