import cv2
import numpy as np
import pyvista as pv
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import ArrayTraversalMethods as atm
from ArrayTraversalMethods import TraverseSpiralInwards as TSI


class vertexData:
    def __init__(self,x,y,z,index):
        self.x = x
        self.y = y
        self.z = z
        self.index = index
        self.visited = False

class faceData:
    def __init__(self, p1, p2, p3, index):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.index = index


img = cv2.imread('test images/test.jpg', cv2.IMREAD_GRAYSCALE)
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



# cloud = pv.PolyData(verticies)
# surf = cloud.delaunay_2d()
# surf.plot(show_edges=True)
#cloud.plot(eye_dome_lighting=True)
# cloud.plot()

# volume = cloud.delaunay_3d(alpha=1.25)
# shell = volume.extract_geometry()
# shell.plot()

def display_vertices_3d(vertices):
    """
    Display vertices in a 3D plot
    Args:
        vertices: numpy array of shape (N, 3) containing x,y,z coordinates
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Split vertices into x, y, z coordinates
    x = vertices[:, 0]
    y = vertices[:, 1]
    z = vertices[:, 2]
    
    # Create the 3D scatter plot
    ax.scatter(x, y, z, c=z, cmap='viridis')
    
    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Point Cloud')
    
    plt.show()

def animate_vertices_3d(vertices):
    """
    Animate vertices being added to a 3D plot.
    Args:
        vertices: numpy array of shape (N, 3) containing x,y,z coordinates
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print(vertices)
    print(verticies[:,0])

    ax.set_xlim([np.min(vertices[:,0]), np.max(vertices[:,0])])
    ax.set_ylim([np.min(vertices[:,1]), np.max(vertices[:,1])])
    ax.set_zlim([np.min(vertices[:,2]), np.max(vertices[:,2])])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Point Cloud Animation')

    scat = ax.scatter([], [], [], c=[], cmap='viridis')

    def update(frame):
        x = vertices[:frame, 0]
        y = vertices[:frame, 1]
        z = vertices[:frame, 2]
        c = z
        scat._offsets3d = (x, y, z)
        scat.set_array(c)
        return scat,

    ani = animation.FuncAnimation(
        fig, update, frames=len(vertices)+1, interval=20, blit=False, repeat=False
    )
    plt.show()

def display_points_2d(points):
    """
    Display a list of 2D points in a 2D scatter plot.
    Args:
        points: numpy array of shape (N, 2) containing x, y coordinates
    """
    plt.figure()
    x = points[:, 0]
    y = points[:, 1]
    plt.scatter(x, y, c='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Point Plot')
    plt.axis('equal')
    plt.show()




def animate_points_2d(points):
    """
    Animate points being added to a 2D scatter plot.
    Args:
        points: numpy array of shape (N, 2) containing x, y coordinates
    """
    fig, ax = plt.subplots()
    ax.set_xlim([np.min(points[:, 0]), np.max(points[:, 0])])
    ax.set_ylim([np.min(points[:, 1]), np.max(points[:, 1])])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('2D Point Animation')
    scat = ax.scatter([], [], c='blue')

    def update(frame):
        x = points[:frame, 0]
        y = points[:frame, 1]
        scat.set_offsets(np.c_[x, y])
        return scat,

    ani = animation.FuncAnimation(
        fig, update, frames=len(points)+1, interval=20, blit=False, repeat=False
    )
    plt.show()

# array = atm.BreadthTraversalList(10,10)
# animate_points_2d(array)
# array = atm.VerticalDepthTraversalList(10,10)
# animate_points_2d(array)
# array = atm.HorizontalDepthTraversalList(10,10)
# animate_points_2d(array)
# array = atm.SnakeVerticalTraversalList(10,10)
# animate_points_2d(array)
# array = atm.SnakeHorizontalTraversalList(10,10)
# animate_points_2d(array)

tsi = TSI(20,20,1)
tsi.Traverse()
array = tsi.ReturnTraverseList()
animate_points_2d(array)

# Example usage:
# animate_points_2d(points_2d)

# Example usage:
# points_2d = np.array([[1, 2], [2, 3], [3, 1]])
# display_points_2d(points_2d)

# Usage:
#display_vertices_3d(verticies)
#animate_vertices_3d(verticies)


