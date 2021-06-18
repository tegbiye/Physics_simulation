
import pygame, sys

pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Width and Height
WIDTH, HEIGHT = 640, 480


screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Bouncing Ball SImulation')

# main loop

bouncing_physics.bouncing_ball(BLACK, WHITE, WIDTH, HEIGHT, screen)
