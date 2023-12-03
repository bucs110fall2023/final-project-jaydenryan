import mole.png

class Moles:

    def __intit__(self,x,y,img_file,up_down):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.up_down = up_down

    def pop_up(self):
        self.up_down = True
    
    def pop_down(self):
        self.up_down = False

    def hit(self):
        