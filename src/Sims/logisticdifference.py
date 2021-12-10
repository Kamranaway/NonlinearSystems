import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

#logisticdifference.py graphs the behavior of the logistic difference equation.

NUM_ITERATIONS = 30
last_x = 0.1
r = 3.3 #Driving force. Adjust to change behavior of system.
x = []



fig = plt.figure()
ax = plt.axes()
ax.set_xlabel('Population')
ax.set_ylabel('Year')

def main():
    
    gen_logistic()
    ax.plot(x, color = 'white')
    plt.show()

def gen_logistic():
    global last_x
    global x
    global r


    iteration = 0
    while iteration < NUM_ITERATIONS:
        x.append(last_x)

        newx = r*last_x*(1-last_x)

        last_x = newx

        iteration += 1

main()