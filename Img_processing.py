import numpy as np
import Image
from solid import *
from solid.utils import *
from stl import mesh
import math

# Create 6 faces of a cube, 2 triagles per face
data = np.zeros(12, dtype=mesh.Mesh.dtype)
#cube defined in stl format 
# Top of the cube
data['vectors'][0] = np.array([[0, 1, 1],
                                  [1, 0, 1],
                                  [0, 0, 1]])
data['vectors'][1] = np.array([[1, 0, 1],
                                  [0, 1, 1],
                                  [1, 1, 1]])
# Right face
data['vectors'][2] = np.array([[1, 0, 0],
                                  [1, 0, 1],
                                  [1, 1, 0]])
data['vectors'][3] = np.array([[1, 1, 1],
                                  [1, 0, 1],
                                  [1, 1, 0]])
# Left face
data['vectors'][4] = np.array([[0, 0, 0],
                                  [1, 0, 0],
                                  [1, 0, 1]])
data['vectors'][5] = np.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [1, 0, 1]])
# Bottem of the cube
data['vectors'][6] = np.array([[0, 1, 0],
                                  [1, 0, 0],
                                  [0, 0, 0]])
data['vectors'][7] = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [1, 1, 0]])
# Right back
data['vectors'][8] = np.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [0, 1, 0]])
data['vectors'][9] = np.array([[0, 1, 1],
                                  [0, 0, 1],
                                  [0, 1, 0]])
# Left back 
data['vectors'][10] = np.array([[0, 1, 0],
                                  [1, 1, 0],
                                  [1, 1, 1]])
data['vectors'][11] = np.array([[0, 1, 0],
                                  [0, 1, 1],
                                  [1, 1, 1]])


def ArrayToSquare(array,scadlist):  #takes in 3 bit depth array and creates a cube with proper hight and location
	x_value = 0
	y_value = 0
	
	for row in array:
		x_value = 0
		for pixel in row:
			scadlist.append(translate([x_value, y_value, 0])(cube([1, 1, pixel])))
			x_value += 1
		y_value += 1


def Conversion(array):  #converts 8 bit greyscale to 3 bit depth for 3d model
	row_count = 0
	item = 0
	for row in array:
		item = 0
		for pixel in row:
			if pixel < 32:
				array[row_count][item] =8
			elif pixel < 64:
				array[row_count][item] =7
			elif pixel < 96:
				array[row_count][item] =6
			elif pixel < 128:
				array[row_count][item] =5
			elif pixel < 160:
				array[row_count][item] =4
			elif pixel < 192:
				array[row_count][item] =3
			elif pixel < 224:
				array[row_count][item] =2
			else:
				array[row_count][item] =1
			item += 1
		row_count += 1
	return array

def ImageToArray(image, array):
	pix = image.load()
	for i in range((width/scale)):
		row = []
		for j in range((height/scale)):
			row.append(pix[i,j])
		picture.append(row)

def ArrayToList(inarray, outarray): #takes in an array and converts it into one long list
	for row in inarray:
		outarray.extend(row)
	return outarray


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


"""nessary temp variable"""

testfile = [] #list to hold all the cubes and there locations generated from ArrayToSquare
picture = [] #array holding all the pixel values with their location corisponding to thier location in the array
image = [] #list to hold all the pixel values to put into scaled picture


#-------------Startup--------------i

input_file = raw_input("file name? ")

img = Image.open(input_file).convert("L") #load the desired image as greyscale/

print "current size is " + str(img.size)

width,height = img.size

scale = input("scale factor: ")

scaled_img = img.resize(((width/scale), (height/scale))) #scales image to 64 x 64 pixels

scaled_img.save("scaled_image.jpg")

ImageToArray(scaled_img, picture)

np.savetxt("array.txt", picture, fmt='%s', delimiter=',')  #saves the pixel values to a text file

Conversion(picture)

# Generate 4 different meshes so we can rotate them later
meshes = [mesh.Mesh(data.copy()) for _ in range((len(picture)*len(picture[0])))]

ArrayToSTL(picture, meshes)

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
scale = np.concatenate([m.points for m in meshes]).flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()

scale.save("test.stl")


# ArrayToSquare(Conversion(picture), testfile) #takes in pixel depth array and outputs list of cubes with translations

# d = union()(testfile) #combines all cubes into one code file for openscad

#save_file = raw_input("save file as?")

#scad_render_to_file(d, save_file + ".scad") #saves the scad file


