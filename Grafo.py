from Simulation import Simulation
from queue import Queue


class Grafo:
    def __init__(self, nodos,mapx,mapy,player,oriented = False):
        self.oriented = oriented
        self.nodos = nodos
        self.mapSizeX = mapx
        self.mapSizeY = mapy
        self.car = player
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

    #Usada em PrimeiraParede
    def devolveByNome(self,nome):
        for peca in self.nodos:
            if (peca.get_nome().__eq__(nome)):
                return peca
        return None    

    def devolveGoals(self):
        goals= list()
        for peca in self.nodos:
            if(peca.get_tipo().__eq__("META")): goals.append(peca)
        return goals

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
        if(self.existePeca(x-1,y-1)): adjacentes.append(self.devolvePeca(x-1,y-1))
        if(self.existePeca(x+1,y-1)): adjacentes.append(self.devolvePeca(x+1,y-1))
        if(self.existePeca(x-1,y+1)): adjacentes.append(self.devolvePeca(x-1,y+1))
        if(self.existePeca(x+1,y+1)): adjacentes.append(self.devolvePeca(x+1,y+1))

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

    def GreedyAlgorithm(self):#calcular melhor caminho apos cada jogada
       possiveisPosicoes=list()
       possiveisPosicoes=Simulation.simulaPossiveisJogadas(self.car,self.mapSizeX,self.mapSizeY)#lista de possiveis estados
       #ir ao grafo à posicao em que o jogador está
       #colocar os filhos desse nodo na fronteira
       #dependendo do valor da heuristica para cada peça o jogador move-se para aquela peca que tiver menor valor de manhataan
       #atualizar os valores do carro a cada jogada | ir armazenando as aceleracoes(direcoes) do simulaPossiveisJogadas
       #verificar que tipo de peça é: se for vazia aumentar o custo +1 caso seja uma parede o jogador tem de fazer moveback e o custo aumenta 25
       #caso de paragem quando chegar a um dos goals F
       # fazer metodo de contagem total do custo
       
    def verificaCaminho(self,posix,posiy,posfx,posfy):
        visited = set()
        fila = Queue()

        # converte para string
        start = self.devolveNome(posix, posiy)
        end = self.devolveNome(posfx, posfy)

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais
        parent = dict()
        parent[start] = None

        path_found = False

        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (n, custo) in self.grafo[nodo_atual]:
                    if n not in visited and not n.startswith('parede'):
                        fila.put(n)
                        parent[n] = nodo_atual
                        visited.add(n)


        if path_found:
            return(1)
        else:
            return(0)

    
    def devolvePrimeiraParede(self,posix,posiy,posfx,posfy):
        visited = set()
        fila = Queue()

        start = self.devolveNome(posix, posiy)
        end = self.devolveNome(posfx, posfy)

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False

        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (n, custo) in self.grafo[nodo_atual]:
                    if n not in visited:
                        if n.startswith('parede'):
                            peca = self.devolveByNome(n)
                            return (peca)
                        else:
                            fila.put(n)
                            parent[n] = nodo_atual
                            visited.add(n)

        return None

    def calcularCustoTotal(self, path):
        test = path
        custo = 0
        i = 0
        while (i+1 < len(test)):
            if (path[i].get_tipo().__eq__("P")):
                custo += 25
            else:
                custo += 1
        return custo




    def calculaHeuristica_Manhataan(self,nodo):
        x = nodo.get_x()
        y = nodo.get_y()
        min = list()
        for goal in self.devolveGoals():
            dmanhattan = abs(x-goal.get_x())+abs(y-goal.get_y())
            min.append((dmanhattan,goal))
        min.sort(key=lambda x: x[0])
        return min[0][0]

