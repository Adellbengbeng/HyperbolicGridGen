import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import os

airfoildirectory = "AirfoilGeometry/"
gridfile = 'NACA23012.dat'
for filename in os.listdir(airfoildirectory):
    with open(os.path.join(airfoildirectory, gridfile), "r") as file:
        XY = [[float(digit) for digit in line.split()] for line in file]
fig = plt.figure()
X = np.zeros([len(XY),1])
Y = np.zeros([len(XY),1])
for i in range(0,len(X)):
    X[i] = XY[i][0]
    Y[i] = XY[i][1]
plt.plot(X,Y,'-o')
plt.axis('equal')
plt.draw()
plt.show()

