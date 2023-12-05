import pygame
import time
import random


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

    
    newMole = Moles(0,0)
    self.allMoles.append(newMole)
    self.amountOfMoles = 1

    self.state = "MENU"

    self.score = 0
        
    

    
  def mainloop(self):
    while True:
        if self.state == "MENU":
            self.menuloop()
        elif self.state == "EXPLAIN":
            self.explinationloop()
        elif self.state == "GAME":
            self.gameloop()
        elif self.state == "GAMEOVER":
            self.gameoverloop()
            
    
        
  

  def menuloop(self):
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "GAME"
            elif event.key == pygame.K_e:
                self.state = "EXPLAIN"

                
      #update data


    self.screen.blit(self.background, (0, 0))
    pygame.display.flip()



  def explinationloop(self):
      
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) or (event.key == pygame.K_e):
                self.state = "MENU"
      #update data


      self.screen.blit(self.background, (0, 0))
      pygame.display.flip()





      
  def gameloop(self):
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

           if self.allMoles[0].rect.collidepoint(event.pos):
                self.score = self.score + 1
                self.allMoles[0].up_down = False

      self.allMoles[0].update()


      if (self.allMoles[0].up_down == False):
        del self.allMoles[0]

      if len(self.allMoles)<1:
        newMole = Moles(random.randrange(0,100),random.randrange(0,100))
        self.allMoles.append(newMole)
        self.amountOfMoles = self.amountOfMoles + 1
        
      if self.amountOfMoles > 10:
        self.state = "GAMEOVER"

      self.screen.blit(self.background, (0, 0))
      self.screen.blit(self.allMoles[0].image,self.allMoles[0].rect)
      pygame.display.flip()
      
    
  def gameoverloop(self):

    print(self.score)

    self.screen.blit(self.background, (0, 0))
    pygame.display.flip()








      
