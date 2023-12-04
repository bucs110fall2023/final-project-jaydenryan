import pygame



from moles import Moles


class Controller:
  
  def __init__(self):
    pygame.init()
    
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    self.background = pygame.Surface((self.width, self.height))
    self.background_color = "white"
    self.background.fill(self.background_color)

    self.allMoles = []

    amountOfMoles = 15

    
    newMole = Moles(0,0)
    self.allMoles.append(newMole)

    self.state = "GAME"

    self.score = 0
        
    

    
  def mainloop(self):
    while True:
        if self.state == "MENU":
            self.menuloop()
        elif self.state == "GAME":
            self.gameloop()
        elif self.state == "GAMEOVER":
            self.gameoverloop()
    
        
  

  def menuloop(self):
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "GAME"
                
      #update data

      #redraw
      
  def gameloop(self):
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for mole in self.allMoles:
              if mole.rect.collidepoint(event.pos):
                score = score + 1
                mole.updown = False

      self.allMoles[0].update()


      if (self.allMoles[0].up_down == False):
        del self.allMoles[0]

      if len(self.allMoles)<1:
        newMole = Moles(0,0)
        self.allMoles.append(newMole)

      self.background.fill(self.background_color)
      self.screen.blit(self.background, (0, 0))
      self.screen.blit(self.allMoles[0].image,self.allMoles[0].rect)
      pygame.display.flip()
      
    
  #def gameoverloop(self):
      #event loop

      #update data

      #redraw
