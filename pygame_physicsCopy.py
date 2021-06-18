import pygame, sys
from bouncing_physics import Bouncing

# main loop
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Width and Height
WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bouncing = Bouncing(BLACK, WHITE, WIDTH, HEIGHT, screen)
pygame.display.set_caption('Bouncing Ball SImulation')

bouncing.bounce_ball()
