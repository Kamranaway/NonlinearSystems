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

#gravRandMap.py maps certain parts of the n-body system in phase space.
#Credit to https://academic.oup.com/mnras/article/425/2/1104/1188012

TIMESTEP = .0001
GCONSTANT = 6.67408e-11

num_bodies = 3
bodies = []
body_tracks = []
track_x = []
track_y = []
track_z = []

for i in range(0, num_bodies):
    bodies.append(Physicsbody(rand.uniform(-1, 1) * 3 , rand.uniform(-1, 1) * 3 , rand.uniform(-1, 1) * 3 ))
    bodies[i].color = 'r'
    bodies[i].vel_vector.x = rand.uniform(-1, 1) * 10
    bodies[i].vel_vector.y = rand.uniform(-1, 1) * 10
    bodies[i].vel_vector.z = rand.uniform(-1, 1) * 10

fig = plt.figure(figsize=(8,5))
ax = plt.axes(projection='3d')

#ax.axes.set_xlim3d(left=0, right=10) 
#ax.axes.set_ylim3d(bottom=0, top=10) 
#ax.axes.set_zlim3d(bottom=0, top=10) 
plt.autoscale(False)

def main():
    init()
    iteration = 0
    while (True):
        animate(iteration)
        iteration += 1
        if (iteration == 10000*5): break
    ax.clear()
    ax.plot(track_x, track_y, track_z, color = 'yellow')
    #ax.scatter(track_x, track_y, track_z)
    #ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()

def init():
    pass

def run_processes():
    global track_x
    global track_y
    global track_z
    
    deltaxs = []
    deltays = []
    deltazs = []
    for body in Physicsbody.bodies:
        body.accel_vector.zero()
        for other_body in Physicsbody.bodies:
            if other_body != body:
                
                delta_x = other_body.pos_vector.x - body.pos_vector.x
                delta_y = other_body.pos_vector.y - body.pos_vector.y
                delta_z = other_body.pos_vector.z - body.pos_vector.z 
                
                deltaxs.append(delta_x)
                deltays.append(delta_y)
                deltazs.append(delta_z)

                magnitude_r = math.sqrt((delta_x*delta_x + delta_y*delta_y + delta_z*delta_z))
              

                #Hacky solution.
                #if magnitude_r < 0.5:
                    #break

                r = Vector(x=delta_x, y=delta_y, z=delta_z)
                r_hat = Vector(x=(r.x/magnitude_r), y=(r.y/magnitude_r), z=(r.z/magnitude_r))

                ax = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r + 0.5*0.5, 3/2)) * r_hat.x
                ay = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r + 0.5*0.5, 3/2)) * r_hat.y
                az = ((GCONSTANT * (1.9891 * 1e13))/pow(magnitude_r + 0.5*0.5, 3/2)) * r_hat.z
                
                body.accel_vector.x += ax 
                body.accel_vector.y += ay
                body.accel_vector.z += az

        body.physics_process(TIMESTEP)
    
   
    
    #track_x.append(np.sqrt(Physicsbody.bodies[0].vel_vector.y * Physicsbody.bodies[0].vel_vector.y + Physicsbody.bodies[0].vel_vector.x * Physicsbody.bodies[0].vel_vector.x + Physicsbody.bodies[0].vel_vector.z * Physicsbody.bodies[0].vel_vector.z))
    #track_y.append(np.sqrt(Physicsbody.bodies[1].vel_vector.y * Physicsbody.bodies[1].vel_vector.y + Physicsbody.bodies[1].vel_vector.x * Physicsbody.bodies[1].vel_vector.x + + Physicsbody.bodies[1].vel_vector.z * Physicsbody.bodies[1].vel_vector.z))
    #track_z.append(np.sqrt(Physicsbody.bodies[2].vel_vector.y * Physicsbody.bodies[2].vel_vector.y + Physicsbody.bodies[2].vel_vector.x * Physicsbody.bodies[2].vel_vector.x + Physicsbody.bodies[2].vel_vector.z * Physicsbody.bodies[2].vel_vector.z))
    
    #track_x.append(np.sqrt(Physicsbody.bodies[0].accel_vector.y * Physicsbody.bodies[0].accel_vector.y + Physicsbody.bodies[0].accel_vector.x * Physicsbody.bodies[0].accel_vector.x + Physicsbody.bodies[0].accel_vector.z * Physicsbody.bodies[0].accel_vector.z))
    #track_y.append(np.sqrt(Physicsbody.bodies[1].accel_vector.y * Physicsbody.bodies[1].accel_vector.y + Physicsbody.bodies[1].accel_vector.x * Physicsbody.bodies[1].accel_vector.x + + Physicsbody.bodies[1].accel_vector.z * Physicsbody.bodies[1].accel_vector.z))
    #track_z.append(np.sqrt(Physicsbody.bodies[2].accel_vector.y * Physicsbody.bodies[2].accel_vector.y + Physicsbody.bodies[2].accel_vector.x * Physicsbody.bodies[2].accel_vector.x + Physicsbody.bodies[2].accel_vector.z * Physicsbody.bodies[2].accel_vector.z))

    #track_x.append(Physicsbody.bodies[0].vel_vector.x)
    #track_y.append(Physicsbody.bodies[1].vel_vector.x)
    #track_z.append(Physicsbody.bodies[2].vel_vector.x)
    
    b1vec = 0
    b2vec = 0
    b3vec = 0
    
    #b1vec += pow(Physicsbody.bodies[0].pos_vector.x, 2) + pow(Physicsbody.bodies[0].pos_vector.y, 2) + pow(Physicsbody.bodies[0].pos_vector.z, 2)
    b1vec += pow(Physicsbody.bodies[0].vel_vector.x, 2) + pow(Physicsbody.bodies[0].vel_vector.y, 2) + pow(Physicsbody.bodies[0].vel_vector.z, 2)
    b1vec += pow(deltaxs[0], 2) + pow(deltays[0], 2) + pow(deltazs[0], 2) + pow(deltaxs[1], 2) + pow(deltays[1], 2) + pow(deltazs[1], 2)
    b1vec += pow(Physicsbody.bodies[0].accel_vector.x, 2) + pow(Physicsbody.bodies[0].accel_vector.y, 2) + pow(Physicsbody.bodies[0].accel_vector.z, 2)
    b1vec = np.sqrt(b1vec)
    
    #b2vec += pow(Physicsbody.bodies[1].pos_vector.x, 2) + pow(Physicsbody.bodies[1].pos_vector.y, 2) + pow(Physicsbody.bodies[1].pos_vector.z, 2)
    b2vec += pow(Physicsbody.bodies[1].vel_vector.x, 2) + pow(Physicsbody.bodies[1].vel_vector.y, 2) + pow(Physicsbody.bodies[1].vel_vector.z, 2)
    b2vec += pow(deltaxs[2], 2) + pow(deltays[2], 2) + pow(deltazs[2], 2) + pow(deltaxs[3], 2) + pow(deltays[3], 2) + pow(deltazs[3], 2) 
    b2vec += pow(Physicsbody.bodies[1].accel_vector.x, 2) + pow(Physicsbody.bodies[1].accel_vector.y, 2) + pow(Physicsbody.bodies[1].accel_vector.z, 2)
    b2vec = np.sqrt(b2vec)
    
    #b3vec += pow(Physicsbody.bodies[2].pos_vector.x, 2) + pow(Physicsbody.bodies[2].pos_vector.y, 2) + pow(Physicsbody.bodies[2].pos_vector.z, 2)
    b3vec += pow(deltaxs[4], 2) + pow(deltays[4], 2) + pow(deltazs[4], 2) + pow(deltaxs[5], 2) + pow(deltays[5], 2) + pow(deltazs[5], 2) 
    b3vec += pow(Physicsbody.bodies[2].vel_vector.x, 2) + pow(Physicsbody.bodies[2].vel_vector.y, 2) + pow(Physicsbody.bodies[2].vel_vector.z, 2)
    b3vec += pow(Physicsbody.bodies[2].accel_vector.x, 2) + pow(Physicsbody.bodies[2].accel_vector.y, 2) + pow(Physicsbody.bodies[2].accel_vector.z, 2)
    b3vec = np.sqrt(b3vec)
    
    #track_x.append((deltaxs[0] + deltaxs[1] + deltaxs[2])/3)
    #track_y.append((deltays[0] + deltays[1] + deltays[2])/3)
    #track_z.append((deltazs[0] + deltazs[1] + deltazs[2])/3)
    
    track_x.append(b1vec)
    track_y.append(b2vec)
    track_z.append(b3vec)
    
    


def animate(i):
    global track_x
    global track_y
    global track_z
    
    #ax.clear()
    run_processes()
    

    


main()