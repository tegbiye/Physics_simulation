#function which does the logic for the simple collission
# using pygame module
def bouncing_ball(col1,col2, wid, height, screen):
  ballx, bally = 0, 0
  vx, vy = 1, 1
  
  while True:
    screen.fill(col1)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    ballx += vx
    bally += vy
    
    if ballx < 0 or ballx > wid:
      vx = -vx
    if bally < 0 or bally > height:
      vy = -vy
    pygame.draw.circle(screen, col2, (ballx, bally), 10)
    pygame.display.update()
