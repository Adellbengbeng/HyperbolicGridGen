import numpy as np
import random
import os
from scipy.interpolate import interp1d

# Class to handle a 2D hyperbolic grid
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
        X = np.zeros([len(XY),1])
        Y = np.zeros([len(XY),1])
        for i in range(0,len(X)):
            X[i] = XY[i][0]
            Y[i] = XY[i][1]
        self.X = np.concatenate(X); self.Y = np.concatenate(Y);
    def calcScoords(self):
        # Function to calculate s-coordinates of grid (x,y) coordinates
        X = self.X; Y = self.Y;
        DX = np.diff(X); DY = np.diff(Y);
        DX = np.insert(DX,0,0); DY = np.insert(DY,0,0);
        DS = np.sqrt(np.power(DX,2) + np.power(DY,2))
        self.S = np.cumsum(DS)
    def interpolateSurf(self):
        # Function to interpolate the grid (x,y) coordinates
        X = self.X; Y = self.Y;
        self.calcScoords()
        s = self.S
        fX = interp1d(s,X,kind='cubic')
        fY = interp1d(s,Y,kind='cubic')
        t2 = np.linspace(0,s[len(s)-1],400)
        self.X = fX(t2); self.Y = fY(t2);
    #def calcDXDxi(self):
        # Function to differentiate grid (x,y) coordinates in the xi direction
        # Second-order, central differencing
        
        
