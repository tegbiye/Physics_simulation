#function which does the logic for the simple collission
# using pygame module
class Bouncing:
  def __init__(self, col1, col2, wid, height, screen):
    self.col1 = col1
    self.col2 = col2
    self.wid = wid
    self.height = height
    self.screen = screen
    
    self.ballx, self.bally = 0, 0
    self.vx, self.vy = 1, 1
    
  def bouncing_ball(self,pygame,sys):
    while True:
      self.screen.fill(self.col1)
      for self.event in pygame.event.get():
        if self.event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      self.ballx += self.vx
      self.bally += self.vy
      if self.ballx < 0 or self.ballx > self.wid:
        self.vx = -self.vx
      if self.bally < 0 or self.bally > self.height:
        self.vy = -self.vy
      pygame.draw.circle(self.screen, self.col2, (self.ballx, self.bally), 10)
      pygame.display.update()
