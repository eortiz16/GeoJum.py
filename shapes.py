from OpenGL.GL import *
from OpenGL.GLU import *

# The objects represented in this file are primitive shapes along with thier corresponding methods 
class RGBA:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

# The Coordinates class will be used to keep track of the position of a shape. If the shape is "movable" then this class
# will also be used to simulate a vector in space
class Coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def printState(self):
        print("x: ", self.x)
        print("y: ", self.y)
        print("z: ", self.z)


class Circle:
    width = 0
    height = 0
    color = RGBA

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        coordinates = Coordinates(0,0,0)
        velocity = Coordinates(0,0,0)

    @classmethod
    def draw(self):
        glColor4fv(128,120,1,0)
        glBegin(GL_QUADS)
        glVertex3f(self.width, -self.width, 0)
        glVertex3f(self.width, self.width, 0)
        glVertex3f(-self.width, self.width, 0)
        glVertex3f(-self.width, -self.width, 0)
        glEnd()

class Square:
    width = 0
    height = 0
    color = RGBA
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    @classmethod
    def draw(self):
        glBegin(GL_QUADS)
        glVertex3f(self.width, -self.width, 0)
        glVertex3f(self.width, self.width, 0)
        glVertex3f(-self.width, self.width, 0)
        glVertex3f(-self.width, -self.width, 0)
        glEnd()
