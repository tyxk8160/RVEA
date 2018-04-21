import numpy as np
import pylab as plt

plt.ion()
fig,ax = plt.subplots()
x = np.random.random()
y =  np.random.random()

for i in range(1000):
    ax.cla()
    dx = np.random.random()
    dy =  np.random.random()
    x+=dx-0.4
    y+=dy -0.4
    ax.scatter(x,y)
    plt.pause(0.1)