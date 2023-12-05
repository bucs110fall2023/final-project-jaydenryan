import time
import pygame

class Moles():

    def __init__(self,x,y,img = "assets/mole.png"):

        
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.up_down = True
        self.startTime = time.time()
        self.rect.x = x
        self.rect.y = y


    def pop_up(self):
        self.up_down = True
    
    def pop_down(self):
        self.up_down = False


    def update(self):
       
        if(int((time.time()-self.startTime) > 2)):
            self.up_down = False
            
            
            
        
        
