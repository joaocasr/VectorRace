from Player import Player

allAceleracoes =list()
for ax in [1,-1,0]:
    for ay in [1,-1,0]:
        allAceleracoes.append((ax,ay))

class Simulation:
    
    def move(x,y,vx,vy,aceleracao): #direction = (ax,ay)
        vx1= vx+aceleracao[0]
        vy1= vy+aceleracao[1]
        #possivel posição para uma dada direcao
        px1 = x+vx1 
        py1 = y+vy1
        return (px1,py1,vx1,vy1) #devolve estado do jogador

    def move_back(x,y,vx,vy,aceleracao):
        vx1= vx-aceleracao[0]
        vy1= vy-aceleracao[1]
        #possivel posição para uma dada direcao
        px1 = x-vx1 
        py1 = y-vy1
        return (px1,py1,vx1,vy1)  #devolve estado do jogador

    def simulaPossiveisJogadas(player,sizeX,sizeY):
        possiveisEstados = list()
        for (ax,ay) in allAceleracoes:
            nextvx = player.get_velocX()+ax
            nextvy = player.get_velocY()+ay
            nextX = player.get_posx()+player.get_velocX() +ax
            nextY = player.get_posy() +player.get_velocY()+ ay

            #garantir que o jogador nao sai do circuito
            if(nextX > sizeX or nextX<=0):
                continue
            if(nextY>sizeY or nextY<=0):
                continue
            #print(str(i)+" volta -"+str((nextvx,nextY)))
            #print("\n")
            possiveisEstados.append(((nextX,nextY,nextvx,nextvy),(ax,ay)))
        return possiveisEstados
    
    def nextMove(cxy1,jogador1,cxy2,jogador2,maze):
        if(maze[cxy1[0]][cxy1[1]]!='X'):
            maze[cxy1[0]][cxy1[1]]=jogador1
        if(maze[cxy2[0]][cxy2[1]]!='X'):
            maze[cxy2[0]][cxy2[1]]=jogador2

        print(str("Coordenadas Player P: ")+str(cxy1))
        print(str("Coordenadas Player J: ")+str(cxy2))
        return maze

    def printMaze(maze1):
        eeline=""
        for e in maze1:
            for ee in e:
                eeline+=ee
            print(eeline)
            eeline=""
            
        




