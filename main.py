import cv2
import numpy as np
import pyvista as pv


# root = tk.TK()

# root.title("Image to STL")

# tk.Label(root, text="Intensity Scale").pack()


# root.mainloop()

def CreateTraversalList(rows, cols):
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1

    #1. 0,0
    #2  0,1 - 1,0
    #3  0,2 - 1,1 - 2,0
    #4  1,2 - 2,1
    #5  2,2

    x = 0
    y = 0
    startX = x
    startY = y

    traversalList = []

    while True:
        traversalList.append([x,y])
        if startX == cols and startY == rows:
            print(traversalList)
            return traversalList
        elif y == 0:           
            if startY == rows:
                startX +=1
            else:
                startY +=1
            x = startX    
            y = startY
        
        elif x == cols:
            if startY == rows:
                startX +=1
            else:
                startY +=1
            x = startX    
            y = startY
        else:
            x += 1
            y -= 1      

CreateTraversalList(5,3)


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

        # assemble 2 triangles per 4 points
        faces[faceCount] = [topLeft.index, topRight.index, bottomLeft.index]
        faceCount+=1
        faces[faceCount] = [topRight.index, bottomRight.index, bottomLeft.index]
        faceCount+=1





def Smoothing(vertexMatrix, maxDelta):
    #need to rewrite to be a recursive algorithm that crawls the hole point cloud
    #want to do it by distance to start not by going down one column and then the next
    #start in the upper left corner
    #check if down exists, find delta in z 
    #check if right exists, find delta in z



    






    if y == 0 or x == cols:
        #we have reached the end of an arc
        x = startX+1
            


    for vertex in vertexMatrix:
        top,bottom,right,left = vertex,vertex,vertex,vertex

        if vertex.x > 0:
            left = vertexMatrix[vertex.y, vertex.x-1]
        if vertex.x < cols:
            right = vertexMatrix[vertex.y, vertex.x+1]
        if vertex.y > 0:
            top = vertexMatrix[vertex.y-1, x]
        if vertex.y < rows:
            bottom = vertexMatrix[vertex.y+1, x]

        vertDelta = abs(top.z-bottom.z)
        horizDelta = abs(right.z - left.z)      




cloud = pv.PolyData(verticies)
surf = cloud.delaunay_2d()
surf.plot(show_edges=True)
#cloud.plot(eye_dome_lighting=True)
# cloud.plot()

# volume = cloud.delaunay_3d(alpha=1.25)
# shell = volume.extract_geometry()
# shell.plot()   


