from shapes import *

# This class will interface with glortho to provide a camera-like experience that will center around the player as they move

class Camera:
    width = 200
    height = 150
    center = Coordinates(0,0,0)

    def __init__(self, center, zoomFactor):
        # self.center = center
        self.zoomFactor = zoomFactor
        self.left = center.x - self.width * self.zoomFactor
        self.right = center.x + self.width * self.zoomFactor
        self.bottom = center.y - self.height * self.zoomFactor
        self.top = center.y + self.height * self.zoomFactor
    
    @classmethod
    def update(playerCenter):
        center = playerCenter

