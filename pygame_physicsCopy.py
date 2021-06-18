import pygame, sys
from bouncing_physics import Bouncing

# main loop
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Width and Height
WIDTH, HEIGHT = 640, 480

Bouncing.bouncing_ball.__init__(BLACK, WHITE, WIDTH, HEIGHT)
pygame.display.set_caption('Bouncing Ball SImulation')

Bouncing.bouncing_ball()
