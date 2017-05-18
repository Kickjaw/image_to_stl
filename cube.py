from stl import mesh
import math
import numpy

test = [[1,2],[2,1]]

a = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]


# Create 6 faces of a cube, 2 triagles per face
data = numpy.zeros(12, dtype=mesh.Mesh.dtype)
#cube defined in stl format 
# Top of the cube
data['vectors'][0] = numpy.array([[0, 1, 1],
                                  [1, 0, 1],
                                  [0, 0, 1]])
data['vectors'][1] = numpy.array([[1, 0, 1],
                                  [0, 1, 1],
                                  [1, 1, 1]])
# Right face
data['vectors'][2] = numpy.array([[1, 0, 0],
                                  [1, 0, 1],
                                  [1, 1, 0]])
data['vectors'][3] = numpy.array([[1, 1, 1],
                                  [1, 0, 1],
                                  [1, 1, 0]])
# Left face
data['vectors'][4] = numpy.array([[0, 0, 0],
                                  [1, 0, 0],
                                  [1, 0, 1]])
data['vectors'][5] = numpy.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [1, 0, 1]])
# Bottem of the cube
data['vectors'][6] = numpy.array([[0, 1, 0],
                                  [1, 0, 0],
                                  [0, 0, 0]])
data['vectors'][7] = numpy.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [1, 1, 0]])
# Right back
data['vectors'][8] = numpy.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 1, 0]])
data['vectors'][9] = numpy.array([[0, 1, 1],
                                  [0, 0, 1],
                                  [0, 1, 0]])
# Left back 
data['vectors'][10] = numpy.array([[0, 1, 0],
                                  [1, 1, 0],
                                  [1, 1, 1]])
data['vectors'][11] = numpy.array([[0, 1, 0],
                                  [0, 1, 1],
                                  [1, 1, 1]])


# Generate 4 different meshes so we can rotate them later
meshes = [mesh.Mesh(data.copy()) for _ in range(16)]


#iterates through the array and translates cube in the x and y direction acroding 
#to positionn in array and in the z direction acording to eh value stored in the array
def ArrayToSTL(array, STLmesh):
  y_count = 0
  x_count = 0
  count = 0
  for row in array:
    x_count = 0
    for item in row:
      meshes[count].x += x_count
      meshes[count].y += y_count
      meshes[count].z += item
      x_count +=1
      count += 1
    y_count += 1

ArrayToSTL(a, meshes)



# Optionally render the rotated cube faces
from matplotlib import pyplot
from mpl_toolkits import mplot3d

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Render the cube faces
for m in meshes:
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

# Auto scale to the mesh size
scale = numpy.concatenate([m.points for m in meshes]).flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
