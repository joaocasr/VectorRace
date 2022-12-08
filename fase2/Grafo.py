from Simulation import Simulation
from queue import Queue
from datetime import datetime

class Grafo:
    def __init__(self, nodos,mapx,mapy,oriented = False):
        self.oriented = oriented
        self.nodos = nodos
        self.mapSizeX = mapx
        self.mapSizeY = mapy
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

    def devolveAllPecas(self,list):
        pecas=list()
        for l in list:
            pecas.append(l.get_nome())
        return pecas

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

    def pecaVisitada(self,posx,posy,list): # ((nextX,nextY,nextvx,nextvy),(ax,ay),heuristica)
        if len(list)==0: return False
        for ((x,y,vx,vy),(ax,ay),h) in list:
            if x==posx and y==posy:
                return True
        return False

    def constroi(self,path):
        lista = list()
        for peca in path:
            if(peca!=None):
                lista.append((peca.get_x(),peca.get_y()))
        return (lista)

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
    
    def GreedyAlgorithm(self,carro,visitados,path):
        start=datetime.now()
        possiveisPosicoes=list()
        posX_inicial=carro.get_posx()
        posY_inicial=carro.get_posy()
        possiveisPosicoes=Simulation.simulaPossiveisJogadas(carro,self.mapSizeX,self.mapSizeY)
        fronteira = list()
        for ((nextX,nextY,nextvx,nextvy),(ax,ay)) in possiveisPosicoes:
            heuristica = self.calculaHeuristica_Manhataan(nextX,nextY)
            if(self.pecaVisitada(nextX,nextY,visitados)==False):
                 fronteira.append(((nextX,nextY,nextvx,nextvy),(ax,ay),heuristica))
        fronteira.sort(key=lambda x:x[2])
        escolhida=fronteira[0]
        #atualizar valores do carro para a nova posicao
        visitados.append(escolhida)
        xAtual=escolhida[0][0]
        yAtual=escolhida[0][1]
        vxAtual=escolhida[0][2]
        vyAtual=escolhida[0][3]
        peca = self.devolvePeca(xAtual,yAtual)
        carro.set_posx(xAtual)
        carro.set_posy(yAtual)
        carro.set_vx(vxAtual)
        carro.set_vy(vyAtual)
        path.append(peca)
        if(peca!=None and peca.get_tipo().__eq__("WALL")):
            carro.set_vx(0)
            carro.set_vy(0)
            carro.set_posx(posX_inicial)
            carro.set_posy(posY_inicial)
            pecaAnterior=self.devolvePeca(posX_inicial,posY_inicial)
            path.append(pecaAnterior)
        if(peca.get_tipo().__eq__("NONE") and (self.existeParedeNoCaminho(posX_inicial,posY_inicial,xAtual,yAtual)[0]==True)):
            carro.set_vx(0)
            carro.set_vy(0)
            path.pop()
            percurso=self.existeParedeNoCaminho(posX_inicial,posY_inicial,xAtual,yAtual)[1]
            p=self.devolvePrimeiraParede(percurso)
            novaPeca=self.devolveByNome(p)
            path.append(novaPeca)
            carro.set_posx(novaPeca.get_x())
            carro.set_posy(novaPeca.get_y())
            carro.set_posx(posX_inicial)
            carro.set_posy(posY_inicial)
            pecaAnterior=self.devolvePeca(posX_inicial,posY_inicial)
            path.append(pecaAnterior)
        if(peca!=None and peca.get_tipo().__eq__("META")):
            custo=self.calcularCustoTotal(path)
            time=datetime.now()-start
            return (self.constroi(path),str("Custo=")+str(custo),time)
        fronteira.clear()
        possiveisPosicoes.clear()
        res=self.GreedyAlgorithm(carro,visitados,path)
        if res is not None:
            return res
        return (peca.get_nome(),path)

    def procuraDFS(self,carro, path, visited):
        startTime=datetime.now()
        start= self.devolveNome(carro.get_posx(),carro.get_posy())
        path.append(self.devolvePeca(carro.get_posx(),carro.get_posy()))
        visited.add(start)
        if "meta" in start:
            custo = self.calcularCustoTotal(path)
            finalTime=datetime.now()-startTime
            return (self.constroi(path),custo,finalTime)
        for (adjacente,custo) in self.grafo[start]:
            if adjacente not in visited:
                if("parede" in adjacente): #se for parede pop da posicao anterior pois o carro terá de voltar para trás
                    visited.pop()
                    path.append(self.devolveByNome(adjacente))
                    visited.add(adjacente)
                else:
                    peca = self.devolveByNome(adjacente)
                    carro.set_posx(peca.get_x())
                    carro.set_posy(peca.get_y())
                resultado = self.procuraDFS(carro,path,visited)
                if resultado is not None:
                    return resultado
        path.pop()
        return None


       #ir ao grafo à posicao em que o jogador está
       #colocar os filhos desse nodo na fronteira
       #dependendo do valor da heuristica para cada peça o jogador move-se para aquela peca que tiver menor valor de manhataan
       #atualizar os valores do carro a cada jogada | ir armazenando as aceleracoes(direcoes) do simulaPossiveisJogadas
       #verificar que tipo de peça é: se for vazia aumentar o custo +1 caso seja uma parede o jogador tem de fazer moveback e o custo aumenta 25
       #caso de paragem quando chegar a um dos goals F
       # fazer metodo de contagem total do custo
       #quando o carro vai para uma dada posicao simulada pela sua aceleracao este irá pelo caminho mais curto do grafo dado pelo algoritmo bfs pelo que temos de verificar se o carro está a atravessar paredes

    def existeParedeNoCaminho(self,posix,posiy,posfx,posfy):
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
                    if n not in visited:
                        fila.put(n)
                        parent[n] = nodo_atual
                        visited.add(n)
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            existe=False
            for nodoAtual in path:
                if "parede" in nodoAtual:
                    existe=True
        return (existe,path)


    def procuraBFS(self,carro):
        startTime=datetime.now()
        start= self.devolveNome(carro.get_posx(),carro.get_posy())
        visited = set()
        fila = Queue()
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)
        # garantir que o start node nao tem pais
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if "meta" in nodo_atual:
                path_found = True
            else:
                for (n, custo) in self.grafo[nodo_atual]:
                    if (n not in visited) and ("parede" not in n):
                        fila.put(n)
                        parent[n] = nodo_atual
                        visited.add(n)
        path = []
        finalTime=datetime.now()-startTime
        if path_found:
            path.append(self.devolveByNome(nodo_atual))
            while parent[nodo_atual] is not None:
                path.append(self.devolveByNome(parent[nodo_atual]))
                nodo_atual = parent[nodo_atual]
            path.reverse()
            custo = self.calcularCustoTotal(path)
            a=path
            b=1
        return (self.constroi(path),custo,finalTime)




    
    def devolvePrimeiraParede(self,path):
        for p in path:
            if "parede" in p:
                return p

    def calcularCustoTotal(self, path):
        custo = 0
        i = 0
        while (i+1 < len(path)):
            if(path[i]!=None and path[i].get_tipo().__eq__("WALL")):
                custo += 25
            else:
                custo += 1
            i+=1
        return custo


    def calculaHeuristica_Manhataan(self,posX,posY):
        min = list()
        for goal in self.devolveGoals():
            dmanhattan = abs(posX-goal.get_x())+abs(posY-goal.get_y())
            min.append((dmanhattan,goal))
        min.sort(key=lambda x: x[0])
        return min[0][0]

