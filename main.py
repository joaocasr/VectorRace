import random
from Grafo import Grafo
from Peca import Peca
from Player import Player

def main():
    y = input("Digita o comprimento do mapa:")
    x = input("Digita a largura do mapa:")
    metax = int(x)/2
    metay = int(y)
    estadox = input("Digite a posição x inicial:")
    estadoy = input("Digite a posição y inicial:")
    nobs=3
    i=1
    j=1
    lineMap=""
    mapLines=list()
    while(j<=int(x)):
        while(i<=int(y)):
            if(j==1):
                lineMap+="X"
            elif(nobs<3 and i==(int(y)//2)):
                    lineMap+="X"
                    nobs+=1
            elif(j==int(estadox) and i==int(estadoy)):
                lineMap+="P"
            elif(j==int(metax)-1 and i==int(metay)):
                lineMap+="F"
            elif(j==int(metax) and i==int(metay)):
                lineMap+="F"
            elif(j==int(metax)+1 and i==int(metay)):
                lineMap+="F"
            elif(i==1):
                lineMap+="X"
            elif(i==int(y)):
                lineMap+="X"    
            elif(j==int(x)):
                lineMap+="X"
            else:
                lineMap+="-"
            i+=1
        if(j==(int(x)//2)):
            nobs=0
        if(j==(int(x)//4)):
            nobs=0
        mapLines.append(lineMap)
        lineMap=""
        j+=1
        i=1

    with open('map.txt', 'w') as filename:
        for line in mapLines:
            filename.write(line+"\n")
    f = open("/home/joao/IA22-23/map.txt","r")
    l = list()
    allPieces = list()
    countLine =1
    countColumn = 1
    for linha in f:
        l.append(linha)
    for linha in l:
        for x in linha:
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
    g = Grafo(allPieces,x,y,player)
    for piece in allPieces:
        g.constroiGrafo(g.devolvePecabyNome(piece))

    for key in g.grafo.keys():
        print(str(key)+str("->"),end=' ')
        for (n,custo) in g.grafo[key]:
             print((n,custo),end=' ')
        print("\n")



if __name__ == "__main__":
    main()
