import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from player import *
from camera import *

class GeoJumpy:
        title = "Geometric Jum.py"
        width = 800
        height = 600
        background = Square(width*2, height*2, RGBA(0,155,255,255)) #sky blue background
        # camera = Camera(Coordinates(0,0,0), 2.0)

        def __init__(self):
                # Initialize Environment, Window, and Viewport
                pygame.init()
                display = (800,600)
                pygame.display.set_caption("Geometric Jum.py") 
                pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
                
                glOrtho(-self.width, self.width, -self.height, self.height, -1, 1)

                self.player = Player(100, 100)
        
        def loop(self):
                # Begin Game Loop
                while True:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()

                        # glOrtho(self.camera.left, self.camera.right, self.camera.bottom, self.camera.top, -1, 1)
                        # glOrtho(self.player.center.x - 800, self.player.center.x + 800, self.player.center.y - 600, self.player.center.y + 600, -1, 1)


                        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                        self.background.draw()
                        self.player.draw()

                        pygame.display.flip()




