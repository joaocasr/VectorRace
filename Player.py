class Player:
    def __init__(self,nome,x,y,vx,vy,ax,ay):
        self.nome = nome
        self.x = x
        self.y = y
        self.velocX = vx
        self.velocY = vy
        self.acelaX = ax
        self.acelaY = ay

    def inc_posY(self):
        self.y += self.velocY + self.acelaY

    def inc_posX(self):
        self.x += self.velocX + self.acelaX

    def inc_velY(self):
        self.velocY += self.acelaY

    def inc_velX(self):
        self.x += self.acelaX

    def get_nome(self):
        return self.nome
    
    def get_posx(self):
        return self.x
    
    def get_posy(self):
        return self.y
    
    def get_velocX(self):
        return self.velocX

    def get_velocY(self):
        return self.velocY

    def get_acelaX(self):
        return self.acelaX
    
    def get_acelaY(self):
        return self.acelaY
    
    