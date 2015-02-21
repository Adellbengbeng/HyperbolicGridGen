import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import os
import grid

gridfile = "NACA23012.dat"
mygrid = grid.Grid(gridfile)
for i in range(0,19):
    mygrid.interpolateSurf()
    mygrid.calcDxi()
    mygrid.calcDeta()
    mygrid.marchGrid()
    print(i)

X = mygrid.XTotal
Y = mygrid.YTotal
plt.plot(X,Y,'k-',np.transpose(X),np.transpose(Y),'k-')
#plt.plot(X[0,:],Y[0,:],'ko-',X[1,:],Y[1,:],'ko-')
plt.axis('equal')
plt.draw()
plt.show()
