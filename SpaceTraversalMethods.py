import numpy as np

def BreadthSpaceTraversal(width,depth,height,x,y,z):
    #create a matrix to hold the traverse progress
    matrix = np.zeros((width,depth,height), dtype=bool)