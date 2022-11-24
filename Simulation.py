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
    
    def nextMove(pecaAntiga,c1,pecaFutura,c2,maze):
        maze[c2[0]][c2[1]]='P'
        maze[c1[0]][c1[1]]=pecaAntiga 
        print(str("Coordenadas: (")+str(c2[0]+1)+str(",")+str(c2[1]+1)+str(")"))
        return maze

    def printMaze(maze1,maze2):
        nl=len(maze1)
        nc=len(maze1[0])
        il=0
        ic=0
        while(il<nl):
            while(ic<nc):
                if maze2[il][ic]=='X' and maze1[il][ic]=='-':
                    maze1[il][ic]='X'
                ic+=1
            ic=0
            il+=1
        eeline=""
        for e in maze1:
            for ee in e:
                eeline+=ee
            print(eeline)
            eeline=""


            
        




