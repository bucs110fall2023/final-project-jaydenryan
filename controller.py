import pygame

from moles import Moles


class Controller:
  
  def __init__(self):
    pygame.init()
    
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    self.background = pygame.Surface((self.width, self.height))

    self.Allmoles = pygame.sprint.Group()

    amountOfMoles = 15

    for i in range(amountOfMoles):
        newMole = Mole(0,0,False)
        self.Allmoles.add(newMole)

    self.state = "MENU"
        
    

    
  def mainloop(self):
    while True:
        if self.state == "GAME":
            self.gameloop()
        elif self.state == "MENU"
            self.menuloop()
        elif self.state == "GAMEOVER":
            self.gameoverloop()
    
        
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "GAME"
                
      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
