import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
from numpy.lib.function_base import append
style.use('dark_background')

#doublePend.py is a graph of a double pendulum system.
#Equations for double pendulum taken from https://www.myphysicslab.com/pendulum/double-pendulum-en.html

TIMESTEP = .01

last_x = 1
last_y = 1


x = [] #pregen
y = [] #pregen
bob_angles = []

xprime = []
yprime = []

mass = 10
fig, ax = plt.subplots(1)

G = 9.8 * 100
theta_1 = np.pi/3
theta_2 = np.pi/3 
length_1 = 20
length_2 = 15
mass_1 = 10
mass_2 = 10
ang_v_1 = 5
ang_v_2 = -6
theta_ones = []
theta_twos = []

def main():
    gen_states()
    ani = animation.FuncAnimation(fig, animate, len(theta_ones), interval=1)
    plt.show()


current_t1 = []
current_t2 = []
def animate(i):
    ax.clear()
    #ax.set_xlim(0, 40)
    #ax.set_ylim(-25, 25)
    current_t1.append(theta_twos[i])
    current_t2.append(theta_ones[i])
    ax.plot(current_t1, current_t2, color='white')
    
        
def gen_states():
    global theta_1
    global theta_2
    global length_1
    global length_2
    global ang_v_1
    global ang_v_2

    time = 0

    while time < 500:
        change_in_angular_1 = (-G*(2*mass_1+mass_2)*np.sin(theta_1)-mass_2*G*np.sin(theta_1-2*theta_2)-2*np.sin(theta_1-theta_2)*mass_2*(ang_v_2*ang_v_2*length_2+ang_v_1*ang_v_1*length_1*np.cos(theta_1-theta_2)))/(length_1*(2*mass_1+mass_2-mass_2*np.cos(2*theta_1-2*theta_2)))
        change_in_angular_2 = (2*np.sin(theta_1-theta_2)*(ang_v_1*ang_v_1*length_1*(mass_1+mass_2)+G*(mass_1+mass_2)*np.cos(theta_1)+(ang_v_2*ang_v_2*length_2*mass_2*np.cos(theta_1-theta_2))))/(length_2*(2*mass_1+mass_2-mass_2*np.cos(2*theta_1-2*theta_2)))
        ang_v_1 += change_in_angular_1*TIMESTEP
        ang_v_2 += change_in_angular_2*TIMESTEP
        theta_1+=ang_v_1*TIMESTEP
        theta_2+=ang_v_2*TIMESTEP
        theta_ones.append(theta_1)
        theta_twos.append(theta_2)
        time += TIMESTEP

main()