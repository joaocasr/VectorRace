import random
from Grafo import Grafo
from Peca import Peca
from Player import Player
from Simulation import Simulation

def main():
    f = open("/home/joao/IA22-23/map5.txt","r")
    l = list()
    circuito=list()
    rowCircuito=list()
    allPieces = list()
    countLine =1
    countColumn = 1
    coordX=0
    for linha in f:
        coordY=len(linha)-1
        l.append(linha)
    for linha in l:
        coordX+=1
        for x in linha:
            if(x=='X'):
                p = Peca("parede("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"WALL")
                rowCircuito.append('X')
            if(x=='-'):
                p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"NONE")
                rowCircuito.append('-')
            if(x=='F'):
                p = Peca("meta("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"META")
                rowCircuito.append('F')
            if(x=='P'):
                p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"None")
                player = Player("player1",countLine,countColumn,0,0)
                rowCircuito.append('P')
            allPieces.append(p)
            countColumn +=1
        countLine +=1
        countColumn=1
    circuito.append(rowCircuito)
    
    #for p in allPieces:
    #    print(p.get_nome())
    g = Grafo(allPieces,coordX,coordY)
    for piece in allPieces:
        g.constroiGrafo(g.devolvePecabyNome(piece))
    vis=list()
    path=list()
    print(str("posição inicial do carro: ")+str((player.get_posx(),player.get_posy())))
    carroX=player.get_posx()
    carroY=player.get_posy()
    (caminho,custo,tempo)=g.GreedyAlgorithm(player,vis,path)

    maze=list()
    mazeLine=list()
    i=1
    for elemento in circuito[0]:
        mazeLine.append(elemento)
        i+=1
        if(i==coordY+1):
            maze.append(mazeLine)
            i=1
            mazeLine=list()
    eeline=""
    for e in maze:
        for ee in e:
            eeline+=ee
        print(eeline)
        eeline=""
    pecaaAlterar= list()
    pecaaAlterar.append('-')
    for pecaCoord in caminho:
        pecaaAlterar.append(maze[pecaCoord[0]-1][pecaCoord[0]-1])
    #print(pecaaAlterar)
    print("Simulação Jogada nº 1")
    Simulation.printMaze(Simulation.nextMove('-',(carroX-1,carroY-1),maze[caminho[0][0]-1][caminho[0][1]-1],(caminho[0][0]-1,caminho[0][1]-1),maze))

    jogadas=len(caminho)
    j=1
    n=0
    while(j!=jogadas):
        print(str("Simulação Jogada nº ")+str(j+1))
        Simulation.printMaze(Simulation.nextMove(pecaaAlterar[j],(caminho[n][0]-1,caminho[n][1]-1),pecaaAlterar[j+1],(caminho[n+1][0]-1,caminho[n+1][1]-1),maze))
        n+=1
        j+=1
    
    print(str("Percurso da Corrida: ")+str(caminho))
    print("Custo: "+str(custo)+str(" Tempo: ")+str(tempo))
    #for key in g.grafo.keys():
    #    print(str(key)+str("->"),end=' ')
    #    for (n,custo) in g.grafo[key]:
    #         print((n,custo),end=' ')
    #    print("\n")



if __name__ == "__main__":
    main()
