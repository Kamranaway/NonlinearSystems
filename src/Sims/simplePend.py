import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#simplePend.py simulates a simple pendulum.

TIMESTEP = .01

last_x = 1
last_y = 1


x = [] #pregen
y = [] #pregen
bob_angles = []

xprime = []
yprime = []

mass = 10
fig, ax = plt.subplots(2)

plane_angles = []
plane_vels = []



length = 3
omega = np.sqrt(9.8*10/length) #radians/second
theta_max = (np.pi)/3 #radians
phi = 0


def main():
    gen_states()
    ani = animation.FuncAnimation(fig, animate, len(bob_angles), interval=10)
    plt.show()


def animate(i):
    ax[0].clear()
    ax[1].clear()

    ax[0].set_xlim(-5, 5)
    ax[0].set_ylim(-5, 5)

    
    ly = length*np.cos(bob_angles[i])
    lx = length*np.sin(bob_angles[i])
    string = [[0], [0]]
    string[0].append(lx)
    string[1].append(-ly)
    ax[0].plot(string[0], string[1], color='white')
    ax[0].plot(lx, -ly, markerfacecolor='r', markeredgecolor='r', marker='.', markersize=30, alpha=1)

    
    if (i > 2):
        theta = bob_angles[i]
        velocity = (bob_angles[i]-bob_angles[i-1])/TIMESTEP
        plane_angles.append(theta)
        plane_vels.append(velocity)
        ax[1].plot(plane_angles, plane_vels, color='white')

        ax[1].set_xlim(-5, 5)
        ax[1].set_ylim(-8, 8)
        ax[1].plot(theta, velocity, markerfacecolor='r', markeredgecolor='r', marker='.', markersize=10, alpha=1)

     
        
def gen_states():
    time = 0

    while time < 500:
        angle = theta_max*np.cos(omega*time + phi)
        bob_angles.append(angle)
        time += TIMESTEP

main()