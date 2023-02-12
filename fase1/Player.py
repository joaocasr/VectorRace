import pygame

class Player:
    def __init__(self,nome,x,y,vx,vy):
        self.nome = nome
        self.x = x
        self.y = y
        self.velocX = vx
        self.velocY = vy
        self.rect = pygame.Rect(x,y,18,18)

    def set_rect(self,x,y):
        self.rect=pygame.Rect(x,y,18,18)

    def get_nome(self):
        return self.nome
    
    def get_posx(self):
        return self.x
    
    def get_posy(self):
        return self.y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_velocX(self):
        return self.velocX

    def get_velocY(self):
        return self.velocY

    def set_posx(self,posx):
        self.x = posx
    
    def set_posy(self,posy):
        self.y = posy
    
    def set_vx(self,vx):
        self.velocX = vx
    
    def set_vy(self,vy):
        self.velocY = vy
    
    def get_tipo(self):
        return "PLAYER"
    


    
    