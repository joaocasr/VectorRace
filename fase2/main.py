import random
from Grafo import Grafo
from Peca import Peca
from Player import Player
from Simulation import Simulation
from pathlib import Path

def main():
    while(1):
        menu = {"1":"Simulação da corrida através do algoritmo DFS",
                "2":"Simulação da corrida através do algoritmo BFS",
                "3":"Simulação da corrida através do algoritmo A*",
                "4":"Simulação da corrida através do algoritmo Greedy",
                "5":"Encerrar"}
        print("\n******************** VectorRace ********************")
        for option in menu.keys():
            print(option+"- "+menu[option])
        print("****************************************************")
        getOpcao = input("Digite a opção pretendida:")
        if(getOpcao=="5"): 
            break;
        
        ficheiro=input("Digite o nome do ficheiro do mapa:")
        nomePlayer1=input("Player P:")
        print(nomePlayer1+"-> P")
        nomePlayer2=input("Player J:")
        print(nomePlayer2+"-> J")
        dir = Path(__file__).resolve().parent
        directory = dir.as_posix()+str("/maps/")+str(ficheiro)
        print(directory)
        f = open(directory,"r")
        l = list()
        circuito=list()
        rowCircuito=list()
        allPieces = list()
        countLine =1
        countColumn = 1
        coordX=0
        goals=list()
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
                    goals.append(p)
                if(x=='J'):
                    p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"NONE")
                    player2 = Player(nomePlayer2,countLine,countColumn,0,0)
                    rowCircuito.append('J')
                if(x=='P'):
                    p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"NONE")
                    player1 = Player(nomePlayer1,countLine,countColumn,0,0)
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
        #print(g.devolvePeca(3,11))
        #for pecinha in allPieces:
        #    print(pecinha)
        
        vis1=list()
        path1=list()
        vis2=list()
        path2=list()
        print(str("posição inicial do carro: ")+str((player1.get_posx(),player1.get_posy())))
        print(str("posição inicial do carro: ")+str((player2.get_posx(),player2.get_posy())))

        carroX1=player1.get_posx()
        carroY1=player1.get_posy()

        carroX2=player2.get_posx()
        carroY2=player2.get_posy()

        if(getOpcao=="1"):
            caminho1=list()
            caminho2=list()
            visit1=set()
            visit2=set()
            path1d=list()
            path2d=list()
            (caminho1,custo1,tempo1)=g.procuraDFS(player1,path1d,visit1)
            (caminho2,custo2,tempo2)=g.procuraDFS(player2,path2d,visit2)
        if(getOpcao=="2"):
            (caminho1,custo1,tempo1)=g.procuraBFS(player1)
            (caminho2,custo2,tempo2)=g.procuraBFS(player2)
        if(getOpcao=="3"):
            (caminho1,custo1,tempo1)=g.aStar(player1)
            (caminho2,custo2,tempo2)=g.aStar(player2)
        if(getOpcao=="4"): 
            (caminho1,custo1,tempo1)=g.GreedyAlgorithm(player1,vis1,path1)
            (caminho2,custo2,tempo2)=g.GreedyAlgorithm(player2,vis2,path2)
        maze=list()
        mazeLine=list()
        i=0
        for elemento in circuito[0]:
            mazeLine.append(elemento)
            i+=1
            if(i==coordY+1):
                maze.append(mazeLine)
                i=0
                mazeLine=list()
        eeline=""
        for e in maze:
            for ee in e:
                eeline+=ee
            print(eeline)
            eeline=""
        maze2=list()
        mazeLine=list()
        i=1
        for elemento in circuito[0]:
            mazeLine.append(elemento)
            i+=1
            if(i==coordY+1):
                maze2.append(mazeLine)
                i=1
                mazeLine=list()
        eeline=""
        j1=len(caminho1)
        j2=len(caminho2)
        i1=1
        i2=1
        inj=1
        res=2
        while(i1<j1 or i2<j2):
            if(j1==0 or j2==0): break
            mazef=Simulation.nextMove((caminho1[i1-1][0]-1,caminho1[i1-1][1]-1),'P',(caminho2[i2-1][0]-1,caminho2[i2-1][1]-1),'J',maze)
            maze=mazef
            if(i1<j1): i1+=1
            if(i2<j2): i2+=1
            print("Simulação da Jogada nº "+str(inj))
            inj+=1
            Simulation.printMaze(mazef)
        print(str("Percurso da Corrida piloto 1: ")+str(caminho1))
        print("Custo: "+str(custo1)+str(" Tempo: ")+str(tempo1))
        print(str("Percurso da Corrida piloto 2: ")+str(caminho2))
        print("Custo: "+str(custo2)+str(" Tempo: ")+str(tempo2))
        vencedor=nomePlayer1
        if(tempo1>tempo2):
            vencedor=nomePlayer2
        print("***********************************************")
        print("*                                             *")
        print("    Parabéns,"+str(vencedor)+"!Você ganhou a corrida!      ")
        print("*                                             *")
        print("***********************************************")

    #print(g.existeParedeNoCaminho(6,9,3,13))
    #for key in g.grafo.keys():
    #    print(str(key)+str("->"),end=' ')
    #    for (n,custo) in g.grafo[key]:
    #         print((n,custo),end=' ')
    #    print("\n")


if __name__ == "__main__":
    main()
