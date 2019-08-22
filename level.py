from scenery import *
from player import *

class Level:
    def __init__(self, width, height):
        # player = PlayerFactory().get_player(PlayerType.BALL)
        self.player = PlayerFactory().get_player(PlayerType.BOX)
        self.background = ShapeFactory().get_shape(ShapeType.QUAD, width*2, height*2, RGBA(0,155,255,255)) #sky blue background
        self.platform = Platform(ShapeFactory().get_shape(ShapeType.QUAD,400,20, RGBA(0,255,100,255)))
        self.platform.quad.center = Coordinates(0,-400,0) #set center
        self.GRAVITY = 2

    # A method for drawing assets
    def draw(self):
        self.background.draw()
        self.player.draw()
        self.platform.quad.draw()
    
    # Update every frame
    def update(self):
        self.player.update(self.GRAVITY)
        # self.player.velocity.printState()

