import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import os
import grid

gridfile = "NACA23012.dat"
mygrid = grid.Grid(gridfile)
mygrid.interpolateSurf()

X = mygrid.X
Y = mygrid.Y
plt.plot(X,Y,'-o')
plt.axis('equal')
plt.draw()
plt.show()
