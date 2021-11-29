import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#aniLorenz.py is an animated graph of the Lorenz System.

#Setup parameters
sigma = 10 #Prandtl number
r = 24.74 #Rayleigh's number
b = (8/3)

#Setup initial conditions
last_x = 0 
last_y = 1
last_z = 0

x = [] #All x coordinates
y = [] #ALl y coordinates
z = [] #ALl z coordinates

x_current = [] #All current x coordinates
y_current = [] #All current y coordinates
z_current = [] #All current z coordinates

fig = plt.figure()
ax = plt.axes(projection='3d')

def main():
    
    gen_lorenz()
    ani = animation.FuncAnimation(fig, animate, len(x), interval=10)
    plt.show()

def animate(i):
    ax.clear()
    x_current.append(x[i])
    y_current.append(y[i])
    z_current.append(z[i])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot3D(x_current, y_current, z_current, color='black')
    ax.plot(x[i], y[i], z[i], markerfacecolor='r', markeredgecolor='r', marker='.', markersize=10, alpha=0.6)

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z

    iteration = 0
    while iteration < 500:
        x.append(last_x)
        y.append(last_y)
        z.append(last_z)

        new_x = last_x
        new_y = last_y
        new_z = last_z

        new_x += (sigma*(last_y-last_x)) * 0.01
        new_y+= ((r*last_x)-last_y-(last_x*last_z)) * 0.01
        new_z+= ((last_x*last_y)-(b*last_z)) * 0.01

        last_x = new_x
        last_y = new_y
        last_z = new_z

        iteration += 0.01

main()