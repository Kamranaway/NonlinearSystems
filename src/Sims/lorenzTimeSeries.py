import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#lorenzTimeSeries.py is a program that displays the Lorenz system as a time series such that exponential divergence of initial conditions can be observed.

sigma = 10
r = 24.74 #rayleigh number
b = 8/3

last_x = 0
last_y = 1
last_z = 0

x = []
y = []
z = []

x2 = []
y2 = []
z2 = []

last_x2 = 0
last_y2 = 1.1
last_z2 = 0

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

    xprime2.append(x2[i])
    yprime2.append(y2[i])
    zprime2.append(z2[i])

    times.append(i*.01)
    ax.plot(times, xprime, color='blue')
    ax.plot(times, xprime2, color='red')

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
    global last_x22
    global x2
    global y2
    global z2

    iteration = 0
    while iteration < 500:
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

    iteration = 0

    while iteration < 500:
        x2.append(last_x2)
        y2.append(last_y2)
        z2.append(last_z2)

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