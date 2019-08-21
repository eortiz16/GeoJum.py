from shapes import *

class Player:
    outline = Square
    body = Square
    reflection = Square
    eye = Square

    def __init__(self, width, height):
        self.width = width
        self.height = height
        outline = Square(self.width + 5, self.height + 5, RGBA(0,0,0,255))
        body = Square(self.width, self.height, RGBA(255,255,255,255))
        reflection = Square(self.width/5, self.height/5, RGBA(255,255,255,255))
        eye = Square(self.width + 5, self.height + 5, RGBA(255,255,255,255))
        # arm = arm
        isAttacking = False
    
    # order of drawing matters! begin with background, end with foreground
    @classmethod
    def draw(self):
        for shape in (self.outline, self.body, self.reflection, self.eye):
            shape.draw()
    
    @classmethod
    def printState(self):
        print("Width: ", self.width, "\n")
        print("Height: ", self.height, "\n")