import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from player import *

def main():
    # Initialize Environment, Window, and Viewport
    player1 = Player(100,100)

    pygame.init()
    display = (800,600)
    pygame.display.set_caption("Geometric Jum.py") 
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glOrtho(-800, 800, -600, 600, -1, 1)

    # Begin Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glColor4ubv((128,120,110,255))
        glBegin(GL_QUADS)
        glVertex2f(100, -100)
        glVertex2f(100, 100)
        glVertex2f(-100, 100)
        glVertex2f(-100, -100)
        glEnd()

        pygame.display.flip()

main()