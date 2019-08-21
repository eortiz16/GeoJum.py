from shapes import *

# Platform is an object that player will interact with. 
class Platform:
    def __init__(self, quad):
        self.quad = quad 

    def draw(self):
        self.quad.draw()


