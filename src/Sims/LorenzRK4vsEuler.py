import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

sigma = 10
r = 24.74 #rayleigh number
b = 8/3

last_x = 1
last_y = 1
last_z = 1

x = []
y = []
z = []

all_x2 = []
all_y2 = []
all_z2 = []

last_x2 = 1
last_y2 = 1
last_z2 = 1

xprime = []
yprime = []
zprime = []

xprime2 = []
yprime2 = []
zprime2 = []

fig = plt.figure()
ax = plt.axes()

def main():
    
    gen_lorenz()
    ani = animation.FuncAnimation(fig, animate, len(x), interval=10)

    plt.show()


times = []
def animate(i):
    ax.clear()
    xprime.append(x[i])
    yprime.append(y[i])
    zprime.append(z[i])

    xprime2.append(all_x2[i])
    yprime2.append(all_y2[i])
    zprime2.append(all_z2[i])

    times.append(i*.01)
    ax.plot(times, xprime, color='blue')
    ax.plot(times, xprime2, color='red')
    #ax.plot(x[i], y[i], markerfacecolor='r', markeredgecolor='r', marker='.', markersize=10, alpha=0.6)

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global last_x2
    global x
    global y
    global z
    global last_x2
    global last_y2
    global last_z2
    global last_x2
    global all_x2
    global all_y2
    global all_z2

    iteration = 0
    while iteration < 500:
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

    iteration = 0

    while iteration < 500:
        all_x2.append(last_x2)
        all_y2.append(last_y2)
        all_z2.append(last_z2)

        newx = last_x2
        newy = last_y2
        newz = last_z2

        newx += (sigma*(last_y2-last_x2)) * 0.01
        
        newy+= ((r*last_x2)-last_y2-(last_x2*last_z2)) * 0.01
        
        newz+= ((last_x2*last_y2)-(b*last_z2)) * 0.01

        last_x2 = newx
        last_y2 = newy
        last_z2 = newz

        iteration += 0.01

main()