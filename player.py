from shapes import *
from enum import Enum

#Player is an abstract type
class Player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = Coordinates(0,0,0)

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

# Ball Player is a concrete type
class BallPlayer(Player):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.outline = ShapeFactory().get_shape(ShapeType.CIRCLE, self.width + 5, self.height + 5, RGBA(0,0,0,255))
        self.body = ShapeFactory().get_shape(ShapeType.CIRCLE, self.width, self.height, RGBA(255,150,150,255))
        self.reflection = ShapeFactory().get_shape(ShapeType.CIRCLE, self.width/2, self.height/2, RGBA(255,180,180,255))
        self.eye = ShapeFactory().get_shape(ShapeType.CIRCLE, self.width/10, self.height/10, RGBA(0,0,0,255))
    
    # order of drawing matters! begin with background, end with foreground
    def draw(self):
        for shape in (self.outline, self.body, self.reflection, self.eye):
            shape.draw()

# BoxPlayer is a concrete type
class BoxPlayer(Player):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.outline = ShapeFactory().get_shape(ShapeType.QUAD, self.width + 5, self.height + 5, RGBA(0,0,0,255))
        self.body = ShapeFactory().get_shape(ShapeType.QUAD, self.width, self.height, RGBA(255,150,150,255))
        self.reflection = ShapeFactory().get_shape(ShapeType.QUAD, self.width/2, self.height/2, RGBA(255,180,180,255))
        self.eye = ShapeFactory().get_shape(ShapeType.QUAD, self.width/10, self.height/10, RGBA(0,0,0,255))

    # order of drawing matters! begin with background, end with foreground
    def draw(self):
        for shape in (self.outline, self.body, self.reflection, self.eye):
            shape.draw()

class PlayerType(Enum):
    BALL = 1
    BOX = 2

class PlayerFactory:
    def get_player(self, type):
        if type == PlayerType.BALL:
            return BallPlayer(100, 100)
        else:
            return BoxPlayer(100, 100)

