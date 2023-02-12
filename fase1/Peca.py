import pygame

class Peca:
    def __init__(self,nome,l,c,tipo):
        self.nome = nome
        self.x = l
        self.y = c
        self.type = tipo
        self.rect = pygame.Rect(l,c,18,18)
    def set_rect(self,x,y):
        self.rect=pygame.Rect(x,y,18,18)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y
    def get_tipo(self):
        return self.type
    def get_nome(self):
        return self.nome    
    def __str__(self):
        return "("+str(self.nome)+",("+str(self.x)+","+str(self.y)+"),"+str(self.type)+")"

