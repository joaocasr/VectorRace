class Peca:
    def __init__(self,nome,l,c,tipo):
        self.nome = nome
        self.x = l
        self.y = c
        self.type = tipo
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_tipo(self):
        return self.tipo
    def get_nome(self):
        return self.nome    
    def __str__(self):
        return "("+str(self.nome)+",("+str(self.x)+","+str(self.y)+"),"+str(self.type)+")"

