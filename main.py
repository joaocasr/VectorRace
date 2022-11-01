import random
from Grafo import Grafo
from Peca import Peca
from Player import Player

def main():
    y = input("Digita o comprimento do mapa:")
    x = input("Digita a largura do mapa:")
    metax = input("Digite a posição x da meta:")
    metay = input("Digite a posição y da meta:")
    estadox = input("Digite a posição x do carro:")
    estadoy = input("Digite a posição y do carro:")
    i=0
    j=0
    lineMap=""
    mapLines=list()
    pecas=['X','-']
    while(j<int(x)):
        while(i<int(y)):
            if(j==0):
                lineMap+="X"
            elif(j==int(estadox) and i==int(estadoy)):
                lineMap+="P"
            elif(j==int(metax) and i==int(metay)):
                lineMap+="F"
            elif(j==int(metax)-1 and i==int(metay)):
                lineMap+="F"
            elif(j==int(metax)+1 and i==int(metay)):
                lineMap+="F"
            elif(i==0):
                lineMap+="X"
            elif(i==int(y)-1):
                lineMap+="X"    
            elif(j==int(x)-1):
                lineMap+="X"
            else:
                lineMap+=pecas[random.randint(0,1)]
            i+=1
        mapLines.append(lineMap)
        lineMap=""
        j+=1
        i=0

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
                p = Peca("wall_"+str(countLine)+"_"+str(countColumn),countLine,countColumn,"WALL")
            if(x=='-'):
                p = Peca("none_"+str(countLine)+"_"+str(countColumn),countLine,countColumn,"NONE")
            if(x=='F'):
                p = Peca("final_"+str(countLine)+"_"+str(countColumn),countLine,countColumn,"FINAL")        
            if(x=='P'):
                p = Peca("none_"+str(countLine)+"_"+str(countColumn),countLine,countColumn,"None")
                player = Player("player1",countLine,countColumn,0,0,0,0)
            allPieces.append(p)
            countColumn +=1
        countLine +=1
        countColumn=1
    #for p in allPieces:
    #    print(p.get_nome())

if __name__ == "__main__":
    main()
