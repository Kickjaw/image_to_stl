import numpy as np
from enum import Enum


def BreadthTraversalList(rows, cols):
    traversalList = np.zeros((rows*cols,2))
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1
    x = 0
    y = 0
    startX = x
    startY = y

    
    count = 0
    while True:
        traversalList[count] = [x,y]
        count+=1
        if startX == cols and startY == rows:
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

def VerticalDepthTraversalList(rows, cols):
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1

    x=0
    y=0
    startX = 0
    startY = 0

    traversalList = np.zeros(( (rows+1)*(cols+1), 2 ))  # Changed to numpy array

    count = 0
    while True:
        traversalList[count] = [x,y]
        count += 1
        if startX == cols and y == rows:
            return traversalList[:count]
        elif y == rows:
            startX +=1
            x = startX
            y = 0
        else:
            y+=1


def HorizontalDepthTraversalList(rows, cols):
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1

    x=0
    y=0
    startX = 0
    startY = 0

    traversalList = np.zeros(( (rows+1)*(cols+1), 2 ))  # Changed to numpy array

    count = 0
    while True:
        traversalList[count] = [x,y]
        count += 1
        if x == cols and startY == rows:
            return traversalList[:count]
        elif x == cols:
            startY +=1
            x = 0
            y = startY
        else:
            x+=1            

def SnakeVerticalTraversalList(rows,cols):
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1

    x=0
    y=0
    yTarget = rows

    up = False

    traversalList = np.zeros(( (rows+1)*(cols+1), 2 ))  # Changed to numpy array

    count = 0
    while True:
        traversalList[count] = [x,y]
        count += 1
        if x == cols and y == yTarget:
            return traversalList[:count]
        elif y == yTarget:
            if up:
                up = False
                yTarget = rows
                x += 1
            else:
                up = True
                yTarget = 0
                x +=1
        else:
            if up:
                y -=1
            else:
                y +=1 

def SnakeHorizontalTraversalList(rows,cols):
    #subtract one as arrays are 0 based
    rows -=1
    cols -=1

    x=0
    y=0
    xTarget = cols

    right = True

    traversalList = np.zeros(( (rows+1)*(cols+1), 2 ))  # Changed to numpy array

    count = 0
    while True:
        traversalList[count] = [x,y]
        count += 1
        if x == xTarget and y == rows:
            return traversalList[:count]
        elif x == xTarget:
            if right:
                right = False
                xTarget = 0
                y += 1
            else:
                right = True
                xTarget = cols
                y +=1
        else:
            if right:
                x +=1
            else:
                x -=1

class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

class Rotation(Enum):
    ClockWise = 1
    Counter = 2

#assumes starting in the top left corner
class TraverseSpiralInwards():
    def __init__(self, rows, cols, rotation):
        self.x = 0
        self.y = 0
        self.rows = rows
        self.cols = cols
        self.rotation = rotation
        self.direction = Direction.Right if self.rotation == Rotation.ClockWise else Direction.Down
        self.traverseList = np.zeros((self.rows*self.cols,2))
        self.visitedMatrix = np.zeros((rows,cols), dtype=bool)

    def Traverse(self):
        count = 0
        while True:
            self.traverseList[count]=[self.x, self.y]
            count+=1
            self.visitedMatrix[self.x, self.y] = True

            if self.CheckMove():
                self.Move()
            else:
                self.ChangeDirection()
                if self.CheckMove():
                    self.Move()
                else:
                    break

    def CheckMove(self):
        xTarget = self.x
        yTarget = self.y

        if self.direction == Direction.Up:
            yTarget -=1
        elif self.direction == Direction.Right:
            xTarget +=1
        elif self.direction == Direction.Down:
            yTarget +=1
        elif self.direction == Direction.Left:
            xTarget -=1
        
        if xTarget > self.cols-1 or xTarget < 0:
            return False
        if yTarget > self.rows-1 or yTarget < 0:
            return False

        if self.visitedMatrix[xTarget,yTarget]:
            return False
        
        return True


    def Move(self):
        if self.direction == Direction.Up:
            self.y -=1
        elif self.direction == Direction.Right:
            self.x +=1
        elif self.direction == Direction.Down:
            self.y +=1
        elif self.direction == Direction.Left:
            self.x -=1

    def ChangeDirection(self):
        if self.rotation == Rotation.ClockWise:
            if self.direction == Direction.Up:
                self.direction = Direction.Right
            elif self.direction == Direction.Right:
                self.direction = Direction.Down
            elif self.direction == Direction.Down:
                self.direction = Direction.Left
            elif self.direction == Direction.Left:
                self.direction = Direction.Up
        else:
            if self.direction == Direction.Up:
                self.direction = Direction.Left
            elif self.direction == Direction.Right:
                self.direction = Direction.Up
            elif self.direction == Direction.Down:
                self.direction = Direction.Right
            elif self.direction == Direction.Left:
                self.direction = Direction.Down


    def ReturnTraverseList(self):
        return self.traverseList