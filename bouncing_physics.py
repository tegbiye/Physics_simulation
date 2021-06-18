#function which does the logic for the simple collission
# using pygame module
class Bouncing:
  def bouncing_ball(self, col1,col2, wid, height, screen):
    self.col1 = col1
    self.col2 = col2
    self.wid = wid
    self.height = height
    self.screen = screen
    
    self.ballx, self.bally = 0, 0
    self.vx, self.vy = 1, 1
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
