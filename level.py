from scenery import *

class Level:
    def __init__(self, player, background, platform):
        self.player = player
        self.background = background
        self.platform = platform
        self.platform.quad.coordinates = Coordinates(0,-400,0) #set center

    def draw(self):
        self.background.draw()
        self.player.draw()
        self.platform.quad.draw()
