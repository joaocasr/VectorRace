class Button:
    def __init__(self,x,y,image):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x,self.y))    
    
    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image,self.rect)
    
    def check(self,MOUSE_POS):
        if MOUSE_POS[0] in range(self.rect.left,self.rect.right) and MOUSE_POS[1] in range(self.rect.top,self.rect.bottom):
            return True
        return False