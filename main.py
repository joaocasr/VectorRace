import random
from Grafo import Grafo
from Peca import Peca
from Player import Player

def main():
    f = open("/home/joao/IA22-23/map5.txt","r")
    l = list()
    allPieces = list()
    countLine =1
    countColumn = 1
    coordX=1
    coordY=1
    for linha in f:
        l.append(linha)
    for linha in l:
        coordX+=1
        for x in linha:
            coordY+=1
            if(x=='X'):
                p = Peca("parede("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"WALL")
            if(x=='-'):
                p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"NONE")
            if(x=='F'):
                p = Peca("meta("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"META")        
            if(x=='P'):
                p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"None")
                player = Player("player1",countLine,countColumn,0,0)
            allPieces.append(p)
            countColumn +=1
        countLine +=1
        countColumn=1
    #for p in allPieces:
    #    print(p.get_nome())
    g = Grafo(allPieces,coordX,coordY)
    for piece in allPieces:
        g.constroiGrafo(g.devolvePecabyNome(piece))
    vis=list()
    path=list()
    print(str("posição inicial do carro: ")+str((player.get_posx(),player.get_posy())))
    print(g.GreedyAlgorithm(player,vis,path))

    #for key in g.grafo.keys():
    #    print(str(key)+str("->"),end=' ')
    #    for (n,custo) in g.grafo[key]:
    #         print((n,custo),end=' ')
    #    print("\n")



if __name__ == "__main__":
    main()
