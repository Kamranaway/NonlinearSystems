import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from physics.physicsbody import Physicsbody
import math
import random as rand
from matplotlib import style
from physics.vector import Vector
style.use('dark_background')

#gravRandHackyTrack.py is a toy model for gravity, of which represents the n-body problem. It involves a hacky solution for when bodies approach each other.

TIMESTEP = .001
GCONSTANT = 6.67408e-11

num_bodies = 30
bodies = []

t1x = []
t1y = []
t1z = []

t2x = []
t2y = []
t2z = []

t3x = []
t3y = []
t3z = []

for i in range(0, num_bodies):
    bodies.append(Physicsbody(rand.uniform(-1, 1) * 3 , rand.uniform(-1, 1) * 3 , rand.uniform(-1, 1) * 3 ))
    bodies[i].color = 'r'
    bodies[i].vel_vector.x = rand.uniform(-1, 1) * 10
    bodies[i].vel_vector.y = rand.uniform(-1, 1) * 10
    bodies[i].vel_vector.z = rand.uniform(-1, 1) * 10
bodies[0].color = 'y'
bodies[1].color = 'r'
bodies[2].color = 'b'

fig = plt.figure(figsize=(8,5))
ax = plt.axes(projection='3d')

plt.autoscale(False)

def main():
    init()
    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()

def init():
    pass

def run_processes():
    global track_x
    global track_y
    global track_z
    
    magnitudes = []
    for body in Physicsbody.bodies:
        body.accel_vector.zero()
        for other_body in Physicsbody.bodies:
            if other_body != body:
                
                delta_x = other_body.pos_vector.x - body.pos_vector.x
                delta_y = other_body.pos_vector.y - body.pos_vector.y
                delta_z = other_body.pos_vector.z - body.pos_vector.z 

                magnitude_r = math.sqrt((delta_x*delta_x + delta_y*delta_y + delta_z*delta_z))
                magnitudes.append(magnitude_r)
                
                if magnitude_r < 0.5: break

                r = Vector(x=delta_x, y=delta_y, z=delta_z)
                r_hat = Vector(x=(r.x/magnitude_r), y=(r.y/magnitude_r), z=(r.z/magnitude_r))

                ax = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r, 3)) * r_hat.x
                ay = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r, 3)) * r_hat.y
                az = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r, 3)) * r_hat.z
                
                body.accel_vector.x += ax 
                body.accel_vector.y += ay
                body.accel_vector.z += az

        body.physics_process(TIMESTEP)
    
    t1x.append(Physicsbody.bodies[0].pos_vector.x)
    t1y.append(Physicsbody.bodies[0].pos_vector.y)
    t1z.append(Physicsbody.bodies[0].pos_vector.z)
    
    t2x.append(Physicsbody.bodies[1].pos_vector.x)
    t2y.append(Physicsbody.bodies[1].pos_vector.y)
    t2z.append(Physicsbody.bodies[1].pos_vector.z)
    
    t3x.append(Physicsbody.bodies[2].pos_vector.x)
    t3y.append(Physicsbody.bodies[2].pos_vector.y)
    t3z.append(Physicsbody.bodies[2].pos_vector.z)
    
    
    

def animate(i):

    ax.clear()
    run_processes()

    ax.axes.set_xlim3d(left=-5, right=5) 
    ax.axes.set_ylim3d(bottom=-5, top=5) 
    ax.axes.set_zlim3d(bottom=-5, top=5)
    plt.autoscale(False)

    for body in Physicsbody.bodies:
        ax.plot(body.pos_vector.x, body.pos_vector.y, body.pos_vector.z, markerfacecolor=body.color, markeredgecolor=body.color, marker='.', markersize=10, alpha=0.6)
    ax.plot(t1x, t1y, t1z, color = 'yellow')
    ax.plot(t2x, t2y, t2z, color = 'red')
    ax.plot(t3x, t3y, t3z, color = 'blue')


main()