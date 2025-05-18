import cv2
import numpy as np
import pyvista as pv

class vertexData:
    def __init__(self,x,y,z,index):
        self.x = x
        self.y = y
        self.z = z
        self.index = index

class faceData:
    def __init__(self, p1, p2, p3, index):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.index = index


img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=.25, fy=.25)


#img = cv2.imread('scaled_image.jpg', cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape

vertexMatrix = np.ndarray((rows,cols), dtype=np.object_)

#x,y,z
verticies = np.empty((cols*rows,3))

faces = np.zeros((2*(cols-1)*(rows-1),3))


count = 0
for x in range(cols):
    for y in range(rows):
        z = img[y,x]/32
        verticies[count] = [x,y,z]
        vertex = vertexData(x,y,z, count)
        vertexMatrix[y,x] = vertex
        count+=1

faceCount= 0
for x in range(cols-1):
    for y in range(rows-1):
       
        topLeft = vertexMatrix[y,x]
        topRight = vertexMatrix[y,x+1]
        bottomLeft = vertexMatrix[y+1,x]
        bottomRight = vertexMatrix[y+1,x+1]

        # asseble 2 triangles per 4 points
        faces[faceCount] = [topLeft.index, topRight.index, bottomLeft.index]
        faceCount+=1
        faces[faceCount] = [topRight.index, bottomRight.index, bottomLeft.index]
        faceCount+=1



cloud = pv.PolyData(verticies)
surf = cloud.delaunay_2d()
surf.plot(show_edges=True)
#cloud.plot(eye_dome_lighting=True)
# cloud.plot()

# volume = cloud.delaunay_3d(alpha=1.25)
# shell = volume.extract_geometry()
# shell.plot()   


