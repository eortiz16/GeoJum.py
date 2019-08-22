import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from player import *
from camera import *
from level import *
from scenery import *

class GeoJumpy:
        title = "Geometric Jum.py"
        width = 800
        height = 600
        # camera = Camera(Coordinates(0,0,0), 2.0)

        def __init__(self):
                # Initialize Environment, Window, and Viewport
                pygame.init()
                display = (800,600)
                pygame.display.set_caption("Geometric Jum.py") 
                pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
                glOrtho(-self.width, self.width, -self.height, self.height, -1, 1) # viewport
                self.level = Level(self.width, self.height)
        
        def loop(self):
                # Begin Game Loop
                while True:
                        # Process events
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()

                        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                        # draw and update every frame
                        self.level.draw()
                        self.level.update()
                        pygame.display.flip()




