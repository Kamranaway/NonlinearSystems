import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#lorenzRK4.py is the RK4 integrated solution for the Lorenz system.
#Source for RK4 algorithm: https://lpsa.swarthmore.edu/NumInt/NumIntFourth.html

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
    #ani = animation.FuncAnimation(fig, animate, len(x), interval=10)
    ax.plot3D(x, y, z, color='black')
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
    while iteration < 200:
        x.append(last_x)
        y.append(last_y)
        z.append(last_z)
        
        #k1
        kx1 = (sigma*(last_y-last_x))
        ky1 = ((r*last_x)-last_y-(last_x*last_z))
        kz1 = ((last_x*last_y)-(b*last_z))
        
        yx1 = last_x + kx1 * 0.01/2
        yy1 = last_y + ky1 * 0.01/2
        yz1 = last_z + kz1 * 0.01/2
        
        #k2
        kx2 = (sigma*(yy1-yx1))
        ky2 = ((r*yx1)-yy1-(yx1*yz1))
        kz2 = ((yx1*yy1)-(b*yz1))
        
        yx2 = last_x + kx2 * 0.01/2
        yy2 = last_y + ky2 * 0.01/2
        yz2 = last_z + kz2 * 0.01/2
        
        #k3
        kx3 = (sigma*(yy2-yx2))
        ky3 = ((r*yx2)-yy2-(yx2*yz2))
        kz3 = ((yx2*yy2)-(b*yz2))
        
        yx3 = last_x + kx3 * 0.01
        yy3 = last_y + ky3 * 0.01
        yz3 = last_z + kz3 * 0.01
        
        #k4
        kx4 = (sigma*(yy3-yx3))
        ky4 = ((r*yx3)-yy3-(yx3*yz3))
        kz4 = ((yx3*yy3)-(b*yz3))
        
        new_x = last_x + (((kx1 + 2*kx2 + 2*kx3 + kx4)*0.01/6))
        new_y = last_y + (((ky1 + 2*ky2 + 2*ky3 + ky4)*0.01/6))
        new_z = last_z + (((kz1 + 2*kz2 + 2*kz3 + kz4)*0.01/6))

        last_x = new_x
        last_y = new_y
        last_z = new_z

        iteration += 0.01

main()
