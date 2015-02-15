import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random
import os
import grid

gridfile = "NACA23012.dat"
mygrid = grid.Grid(gridfile)
plt.plot(mygrid.X,mygrid.Y,'-o')
plt.axis('equal')
plt.draw()
plt.show()
