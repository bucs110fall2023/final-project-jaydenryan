import pygame
import time
import random


from src.moles import Moles


class Controller:
  
  def __init__(self):
    pygame.init()
    
    self.screen = pygame.display.set_mode((700,700))
    self.width, self.height = pygame.display.get_window_size()
    self.background = pygame.Surface((self.width, self.height))
    self.background_color = "lightblue"
    self.background.fill(self.background_color)

    self.game_background = pygame.image.load("assets/background.png")

    self.allMoles = []

    
    newMole = Moles(304,160)
    self.allMoles.append(newMole)
    self.amountOfMoles = 1

    self.state = "MENU"

    self.score = 0
        
    

    
  def mainloop(self):

      '''
    Main loop that controls what other loop will be running
    args: (N/A)
    return: (N/A)
    '''
      
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

    '''
    Main menu loop, shows different choices to begin
    args: (N/A)
    return: (N/A)
    '''
    
    default_font = pygame.font.Font(None,70)
    menu_font = pygame.font.SysFont("krungthep",90,True)

    menu_text = "Mole Game"
    menu_surface = menu_font.render(menu_text,True,(0,0,0))

    explain_text = "Press 'E' for instructions"
    explain_surface = default_font.render(explain_text,True,(0,0,0))

    start_text = "Press 'SPACE' to begin"
    start_surface = default_font.render(start_text,True,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.state = "GAME"
            elif event.key == pygame.K_e:
                self.state = "EXPLAIN"

                
      #update data

    self.screen.blit(self.background, (0, 0))
    self.screen.blit(pygame.image.load("assets/mole.png"),(275,190))
    self.screen.blit(menu_surface,(90,50))
    self.screen.blit(explain_surface,(63,500))
    self.screen.blit(start_surface,(90,600))
    pygame.display.flip()

    



  def explinationloop(self):
    
        '''
      Runs after user asks for gameplay instructions and displays the instructions
      args: (N/A)
      return: (N/A)
      '''
        
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) or (event.key == pygame.K_e):
                self.state = "MENU"
      #update data
      smaller_font = pygame.font.Font(None,45)
      default_font = pygame.font.Font(None,70)

      #Explaining text strs
      explination_text1 = "Your goal is to get rid of all the moles!"
      explination_text2 = "Simply click with the mouse to hit them away."
      explination_text3 = "Good luck."

      go_back_text = "Press 'SPACE' or 'E' to return" 

      #Creating surfaces
      explination_surface1 = smaller_font.render(explination_text1,True,(0,0,0))
      explination_surface2 = smaller_font.render(explination_text2,True,(0,0,0))
      explination_surface3 = smaller_font.render(explination_text3,True,(0,0,0))

      go_back_surface = default_font.render(go_back_text,True,(0,0,0))

      #Bliting surfaces
      self.screen.blit(self.background, (0, 0))

      self.screen.blit(go_back_surface, (10,600))
      self.screen.blit(explination_surface1,(70,100))
      self.screen.blit(explination_surface2,(20,200))
      self.screen.blit(explination_surface3,(270,300))

      pygame.display.flip()

    





      
  def gameloop(self):

    '''
      Main gameplay loop, creates the moles and detects for mouse clicks on them
      args: (N/A)
      return: (N/A)
      '''
    
      #Change background
      self.screen.blit(self.game_background, (0, 0))

      #Coordinates of hole locations
      cords = ((135,20),(308,20),(477,20),(133,160),(304,160),(474,160),(133,320),(308,320),(477,320))
      rng = random.randint(0,8)

      #Begin loop
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           if self.allMoles[0].rect.collidepoint(event.pos):
                self.score = self.score + 1
                self.allMoles[0].up_down = False

      self.allMoles[0].update()


      if (self.allMoles[0].up_down == False):
        del self.allMoles[0]

      if len(self.allMoles)<1:
        newMole = Moles(cords[rng][0],cords[rng][1])
        self.allMoles.append(newMole)
        self.amountOfMoles = self.amountOfMoles + 1
        
      if self.amountOfMoles > 15:
        self.state = "GAMEOVER"

      self.screen.blit(self.allMoles[0].image,self.allMoles[0].rect)

      #Display score
      default_font = pygame.font.Font(None,70)
      cur_score_surface = default_font.render("Score:"+str(self.score),True,(0,0,0))
      self.screen.blit(cur_score_surface,(0,0))

      #Mouse as hammer
      self.screen.blit(pygame.image.load("assets/hammer.png"),pygame.mouse.get_pos())

      pygame.display.flip()

      
      
    
  def gameoverloop(self):

  '''
    Appears at the end of the game to display the user their score
    args: (N/A)
    return: (N/A)
    '''
  
    default_font = pygame.font.Font(None,70)
    game_over_font = pygame.font.SysFont("krungthep",90,True)

    game_over_message = "GAME OVER"
    game_over_surface = game_over_font.render(game_over_message,True,(0,0,0))

    if(self.score>10):
      final_message = "You Won!"
    else:
      final_message = "You Lost"
    final_score_surface = default_font.render("Final Score: "+str(self.score),True,(0,0,0))
    final_message_surface = default_font.render(final_message,True,(0,0,0))
    self.screen.blit(self.background, (0,0))
    self.screen.blit(final_score_surface,(165,300))
    self.screen.blit(final_message_surface,(165,200))
    self.screen.blit(game_over_surface, (165,100))

    pygame.display.flip()

  








      
