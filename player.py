from shapes import *

class Player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.outline = Square(self.width + 5, self.height + 5, RGBA(0,0,0,255))
        self.body = Square(self.width, self.height, RGBA(255,150,150,255))
        self.reflection = Square(self.width/2, self.height/2, RGBA(255,180,180,255))
        self.eye = Square(self.width/10, self.height/10, RGBA(0,0,0,255))
        self.center = Coordinates(0,0,0)
    
    # order of drawing matters! begin with background, end with foreground
    def draw(self):
        for shape in (self.outline, self.body, self.reflection, self.eye):
            shape.draw()

    # update all chapes with new center (as character moves accross the screen)
    def update(self):
        self.outline.coordinates = self.center
        self.body.coordinates = self.center
        self.reflection.coordinates = self.center
        self.eye.coordinates = self.center

    def printState(self):
        print("Width: ", self.width, "\n")
        print("Height: ", self.height, "\n")
        for shape in (self.outline, self.body, self.reflection, self.eye):
            shape.printState()