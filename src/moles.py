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

        '''
        Changes the mole from down to up
        args: (N/A)
        return: (N/A)
        '''
    
    def pop_down(self):
        self.up_down = False
        '''
        Changes the mole from up to down
        args: (N/A)
        return: (N/A)
        '''


    def update(self):
       
        if(int((time.time()-self.startTime) > 1)):
            self.up_down = False

        '''
        Updates the mole to go down after 1 second
        args: (N/A)
        return: (N/A)
        '''
            
            
            
        
        
