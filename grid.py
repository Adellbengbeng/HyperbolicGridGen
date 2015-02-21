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
        XTotal = np.zeros([len(X),1])
        YTotal = np.zeros([len(Y),1])
        for i in range(0,len(X)):
            X[i] = XY[i][0]
            Y[i] = XY[i][1]
        self.X = np.concatenate(X); 
        self.Y = np.concatenate(Y);
        XTotal[:,0] = self.X;
        YTotal[:,0] = self.Y;
        self.XTotal = XTotal;
        self.YTotal = YTotal;
        self.N = 1.;
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
        self.Xinterp = fX(t2); self.Yinterp = fY(t2); self.Sinterp = t2
    def calcDxi(self):
        # Function to differentiate grid (x,y) coordinates in the xi direction
        # Second-order, central differencing
        xi = self.Sinterp; x = self.Xinterp; y = self.Yinterp
        dxi = xi[1]-xi[0]
        DxDxi = np.zeros(len(xi))
        DyDxi = np.zeros(len(xi))
        DxDxi[1:len(DxDxi)-1] = (x[2:len(x)]-x[0:len(x)-2])/2/dxi
        DyDxi[1:len(DyDxi)-1] = (y[2:len(y)]-y[0:len(y)-2])/2/dxi
        DxDxi[0] = (x[1]-x[0])/dxi
        DyDxi[0] = (y[1]-y[0])/dxi
        DxDxi[len(x)-1] = (x[len(x)-1]-x[len(x)-2])/dxi
        DyDxi[len(x)-1] = (y[len(y)-1]-y[len(y)-2])/dxi
        fDxDxi = interp1d(xi,DxDxi,kind='cubic')
        fDyDxi = interp1d(xi,DyDxi,kind='cubic')
        self.DxDxi = fDxDxi(self.S)
        self.DyDxi = fDyDxi(self.S)
    def calcDeta(self):
        # Function to calculate derivatives in the marching direction
        DxDxi = self.DxDxi; DyDxi = self.DyDxi;
        dxi = np.diff(self.S);
        k = self.N/20; self.detadxi = k;
        Area = k*np.power(dxi,0)
        Deta = np.zeros([len(dxi)+1,2])
        for i in range(0,len(dxi)):
            A = np.matrix([[DxDxi[i],DyDxi[i]],[-DyDxi[i],DxDxi[i]]]);
            f = np.array([[0],[Area[i]]])
            sol = np.matrix(np.linalg.solve(A,f))
            Deta[i,:] = np.transpose(sol)
        Deta[len(Deta)-1,:] = Deta[len(Deta)-2,:]
        self.DxDeta = Deta[:,0]
        self.DyDeta = Deta[:,1]
    def marchGrid(self):
        # Function to march the grid front one step in eta and then
        # reset the grid to be equal to the new front
        DxDeta = self.DxDeta; DyDeta = self.DyDeta;
        x = self.X; y = self.Y;
        xNP1 = np.zeros(len(x));
        yNP1 = np.zeros(len(x));
        k = self.detadxi
        dxi = np.zeros([len(x)])
        dxi[0:len(dxi)-1] = np.diff(self.S)
        dxi[len(dxi)-1] = dxi[len(dxi)-2]
        for i in range(0,len(xNP1)):
            xNP1[i] = x[i] + DxDeta[i]*k*dxi[i]
            yNP1[i] = y[i] + DyDeta[i]*k*dxi[i]
        xtotal = self.XTotal; ytotal = self.YTotal;
        Xcat = np.zeros([len(xtotal),np.size(xtotal,1)+1])
        Ycat = np.zeros([len(ytotal),np.size(ytotal,1)+1])
        Xcat[:,:-1] = xtotal; Xcat[:,np.size(Xcat,1)-1] = xNP1;
        Ycat[:,:-1] = ytotal; Ycat[:,np.size(Ycat,1)-1] = yNP1;
        self.XTotal = Xcat; self.YTotal = Ycat;
        self.X = xNP1; self.Y = yNP1
        self.N = self.N+1
        
        
        
        
