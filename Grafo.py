class Grafo:
    def __init__(self, nodos,oriented = False):
        self.oriented = oriented
        self.nodos = nodos
        self.visitados = []
        self.grafo = {}
    
    
    def devolveNome(self,x,y):
        for peca in self.nodos:
            if(peca.get_x()==x and peca.get_y()==y):
                 return peca.get_nome()
        return None

    def devolvePeca(self,x,y):
        for peca in self.nodos:
            if(peca.get_x()==x and peca.get_y()==y):
                 return peca
        return None
    
    def devolvePecabyNome(self,node):
        for peca in self.nodos:
            if(peca.get_nome().__eq__(node.get_nome())):
                 return peca
        return None

    def existePeca(self,x,y):
        for peca in self.nodos:
            if(peca.get_x()==x and peca.get_y()==y):
                 return True
        return False

    #devolve lista de nodos adjacentes
    def devolveAdjs(self,x,y):
        peca = self.devolvePeca(x,y)
        x = peca.get_x()
        y = peca.get_y()
        adjacentes = list()
        if(self.existePeca(x+1,y)): adjacentes.append(self.devolvePeca(x+1,y))
        if(self.existePeca(x-1,y)): adjacentes.append(self.devolvePeca(x-1,y))
        if(self.existePeca(x,y+1)): adjacentes.append(self.devolvePeca(x,y+1))
        if(self.existePeca(x,y-1)): adjacentes.append(self.devolvePeca(x,y-1))
        for p in adjacentes:
            if(p.get_nome() in self.visitados):
                    adjacentes.remove(p)
        return adjacentes

    def constroiGrafo(self,start):
        adjs = self.devolveAdjs(start.get_x(),start.get_y())
        for a in adjs:
            self.adicionaAresta(start,a,1)
        self.visitados.append(start.get_nome())
        

    def adicionaAresta(self, node1, node2, weight):
        if (node1.get_nome() not in self.grafo.keys()):
            self.grafo[node1.get_nome()] = list()
        if (node2.get_nome() not in self.grafo.keys()):
            self.grafo[node2.get_nome()] = list()
        if((node2.get_nome(),weight) not in self.grafo[node1.get_nome()]):
            self.grafo[node1.get_nome()].append((node2.get_nome(), weight))
        if not self.oriented and (node1.get_nome(),weight) not in self.grafo[node2.get_nome()] and not self.oriented:
            self.grafo[node2.get_nome()].append((node1.get_nome(), weight))




    

