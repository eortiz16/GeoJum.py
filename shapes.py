from OpenGL.GL import *
from OpenGL.GLU import *

# The objects represented in this file are primitive shapes along with thier corresponding methods 
class RGBA:
    red = int
    green = int
    blue = int
    alpha = int

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
    
    @classmethod
    def printState(self):
        print("r: ", self.red)
        print("g: ", self.green)
        print("b: ", self.blue)
        print("a: ", self.alpha)

# The Coordinates class will be used to keep track of the position of a shape. If the shape is "movable" then this class
# will also be used to simulate a vector in space
class Coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def printState(self):
        print("x: ", self.x)
        print("y: ", self.y)
        print("z: ", self.z)

# Circle is a concrete type
class Circle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.coordinates = Coordinates(0,0,0)
        self.velocity = Coordinates(0,0,0)

    def draw(self):
        right = self.coordinates.x + self.width
        left = self.coordinates.x - self.width
        top = self.coordinates.y + self.height
        bottom = self.coordinates.y - self.height

        glColor4ubv((self.color.red, self.color.green, self.color.blue, self.color.alpha))
        glBegin(GL_QUADS)
        glVertex2f(right, bottom)
        glVertex2f(right, top)
        glVertex2f(left, top)
        glVertex2f(left, bottom)
        glEnd()
    
    def printState(self):
        print("Width: ", self.width)
        print("Height: ", self.height)
        self.color.printState()
        self.coordinates.printState()
        self.velocity.printState()

# Square is a concrete type
class Square:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.coordinates = Coordinates(0,0,0)
        self.velocity = Coordinates(0,0,0)
    
    def draw(self):
        right = self.coordinates.x + self.width
        left = self.coordinates.x - self.width
        top = self.coordinates.y + self.height
        bottom = self.coordinates.y - self.height

        glColor4ubv((self.color.red, self.color.green, self.color.blue, self.color.alpha))
        glBegin(GL_QUADS)
        glVertex2f(right, bottom)
        glVertex2f(right, top)
        glVertex2f(left, top)
        glVertex2f(left, bottom)
        glEnd()

    def printState(self):
        print("Width: ", self.width)
        print("Height: ", self.height)
        self.color.printState()
        self.coordinates.printState()
        self.velocity.printState()

