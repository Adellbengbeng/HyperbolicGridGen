import numpy as np
import random
import os

class Grid:
    def __init__(self,gridfile):
        # Initialization
        # INPUTS:
        #    'gridfile': string specifying filename of the gridfile
        self.gridFilename = gridfile
        airfoildirectory = r"/home/anthony/HyperbolicGridGen/AirfoilGeometry/"
        fullpath = airfoildirectory + gridfile
        with open(fullpath, "r") as file:
            XY = [[float(digit) for digit in line.split()] for line in file]
        self.X = np.zeros([len(XY),1])
        self.Y = np.zeros([len(XY),1])
        for i in range(0,len(self.X)):
            self.X[i] = XY[i][0]
            self.Y[i] = XY[i][1]
