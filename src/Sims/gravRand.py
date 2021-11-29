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

TIMESTEP = .01
GCONSTANT = 6.67408e-11

num_bodies = 10
bodies = []
body_tracks = []
cm_track_x = []
cm_track_y = []
cm_track_z = []

for i in range(0, num_bodies):
    bodies.append(Physicsbody(rand.uniform(-1, 1) * 10 , rand.uniform(-1, 1) * 10 , rand.uniform(-1, 1) * 10 ))
    bodies[i].color = 'r'
    bodies[i].vel_vector.x = rand.uniform(-1, 1) * 1
    bodies[i].vel_vector.y = rand.uniform(-1, 1) * 1
    bodies[i].vel_vector.z = rand.uniform(-1, 1) * 1


    
    

#do vectors

#do colors

#Do tracks
# for i in range(0, num_bodies):
#     body_tracks.append([[], [], []])



fig = plt.figure(figsize=(8,5))
ax = plt.axes(projection='3d')

ax.axes.set_xlim3d(left=0, right=10) 
ax.axes.set_ylim3d(bottom=0, top=10) 
ax.axes.set_zlim3d(bottom=0, top=10) 
plt.autoscale(False)

def main():
    init()
    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()

def init():
    pass

def run_processes():
    global cm_track_x
    global cm_track_y
    global cm_track_z

    cm_x = 0
    cm_y = 0
    cm_z = 0
    for body in Physicsbody.bodies:
        cm_x += body.pos_vector.x
        cm_y += body.pos_vector.y
        cm_z += body.pos_vector.z

        body.accel_vector.zero()
        for other_body in Physicsbody.bodies:
            if other_body != body:
                
                delta_x = other_body.pos_vector.x - body.pos_vector.x
                delta_y = other_body.pos_vector.y - body.pos_vector.y
                delta_z = other_body.pos_vector.z - body.pos_vector.z 

                magnitude_r = math.sqrt((delta_x*delta_x + delta_y*delta_y + delta_z*delta_z))

                #Hacky solution.
                if magnitude_r < 0.25:
                    break

                r = Vector(x=delta_x, y=delta_y, z=delta_z)
                r_hat = Vector(x=(r.x/magnitude_r), y=(r.y/magnitude_r), z=(r.z/magnitude_r))

                ax = ((GCONSTANT * (1.9891))/pow(magnitude_r, 2)) * r_hat.x
                ay = ((GCONSTANT * (1.9891))/pow(magnitude_r, 2)) * r_hat.y
                az = ((GCONSTANT * (1.9891))/pow(magnitude_r, 2)) * r_hat.z

                

                body.accel_vector.x += ax * 1e12
                body.accel_vector.y += ay * 1e12
                body.accel_vector.z += az * 1e12

        body.physics_process(TIMESTEP)
    cm_x /= len(Physicsbody.bodies)
    cm_y /= len(Physicsbody.bodies)
    cm_z /= len(Physicsbody.bodies)
    cm_track_x.append(cm_x)
    cm_track_y.append(cm_y)
    cm_track_z.append(cm_z)





    #append tracks
    # for i in range (0, len(body_tracks)):
    #     for body in bodies:
    #         body_tracks[i][0].append(body.pos_vector.x)
    #         body_tracks[i][1].append(body.pos_vector.y)
    #         body_tracks[i][2].append(body.pos_vector.z)
   
    

def animate(i):
    global cm_track_x
    global cm_track_y
    global cm_track_z
    
    ax.clear()
    run_processes()

    # for i in range (0, len(body_tracks)):
    #     ax.plot3D(body_tracks[i][0], body_tracks[i][1], body_tracks[i][2], color = 'black')
    

    ax.axes.set_xlim3d(left=-10, right=10) 
    ax.axes.set_ylim3d(bottom=-10, top=10) 
    ax.axes.set_zlim3d(bottom=-10, top=10)
    plt.autoscale(False)

    for body in Physicsbody.bodies:
        ax.plot(body.pos_vector.x, body.pos_vector.y, body.pos_vector.z, markerfacecolor=body.color, markeredgecolor=body.color, marker='.', markersize=10, alpha=0.6)
        ax.plot(cm_track_x, cm_track_y, cm_track_z, color = 'yellow')


main()