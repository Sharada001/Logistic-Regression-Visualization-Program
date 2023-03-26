import numpy as np

def Sigmoid(z):
    return 1/(1+np.exp(-1*z))