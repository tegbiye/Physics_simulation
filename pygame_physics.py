
import pygame, sys
import bouncing_physics
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Width and Height
WIDTH, HEIGHT = 640, 480


screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Bouncing Ball SImulation')

# main loop

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  
