import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import scipy.integrate as intg
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
        
        #k1
        x1 = (sigma*(last_y-last_x))*0.01
        y1 = ((r*last_x)-last_y-(last_x*last_z))*0.01
        z1 = ((last_x*last_y)-(b*last_z))*0.01
        
        #k2
        x2 = (sigma*(y1-x1))*(0.01/2)
        y2 = ((r*x1)-y1-(x1*z1))*(0.01/2)
        z2 = ((x1*y1)-(b*z1))*(0.01/2)
        
        #k3
        x3 = (sigma*(y2-x2))*(0.01/2)
        y3 = ((r*x2)-y2-(x2*z2))*(0.01/2)
        z3 = ((x2*y2)-(b*z2))*(0.01/2)
        
        #k4
        x4 = (sigma*(y3-x3))*(0.01)
        y4 = ((r*x3)-y3-(x3*z3))*(0.01)
        z4 = ((x3*y3)-(b*z3))*(0.01)
        
        new_x = last_x + (((x1 + 2*x2 + 2*x3 + x4)/6))
        new_y = last_y + (((y1 + 2*y2 + 2*y3 + y4)/6))
        new_z = last_z + (((z1 + 2*z2 + 2*z3 + z4)/6))

        last_x = new_x
        last_y = new_y
        last_z = new_z

        iteration += 0.01

main()