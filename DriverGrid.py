import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import os
import grid

gridfile = "NACA23012.dat"
mygrid = grid.Grid(gridfile)
mygrid.interpolateSurf()
#mygrid.calcDxi()
#mygrid.calcDeta()
#mygrid.marchGrid()
for i in range(0,5):
    mygrid.calcDxi()
    mygrid.calcDeta()
    mygrid.marchGrid()
    print(i)

X = mygrid.XTotal
Y = mygrid.YTotal
plt.plot(X,Y,'k-')
plt.plot(np.transpose(X),np.transpose(Y),'b-')
plt.axis('equal')
plt.draw()
plt.show()
