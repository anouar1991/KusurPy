import numpy as np

class Kasr :
    def __init__(self, up, down):
        self.up = up
        self.down = down
        self.mat = np.array([[up],[down]])
    def __mul__(self, other):
        other = self.handleType(other)
        newMulMat = np.multiply(self.mat,other.mat)
        return Kasr(newMulMat[0,0],newMulMat[1,0])
    def __add__(self, other):
        other = self.handleType(other)
        tempMat= np.column_stack((self.mat, other.mat))
        '''
        [a,b].[c,d].T*[[0,1],[1,0]] = a * d + b * c
        '''
        dc = np.dot(tempMat[1,:].T,np.array([[0,1],[1,0]]))
        ab = tempMat[0,:]
        newUp = np.dot(ab,dc)
        '''
        c*d
        '''
        newDown = np.product(tempMat[1,:])
        return Kasr(newUp, newDown)
    def handleType(self,value):
        if(type(value) == int or type(value) == float ):
            return Kasr(value, 1)
