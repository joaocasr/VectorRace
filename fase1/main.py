import random
from Grafo import Grafo
from Player import Player
from Simulation import Simulation
from pathlib import Path
import pygame , sys
import os
from Peca import Peca
from Button import Button
import time
from random import randrange

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

BACKGROUND = pygame.image.load("/home/joao/IA22-23/fase1/assets/vector.JPG")
STARTBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/thumbnail_startbutton.png")
QUITBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/thumbnail_quitbutton.png")
DFSBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/DFS.png")
BFSBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/BFS.png")
ASTARBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/ASTAR.png")
GREEDYBUTTON = pygame.image.load("/home/joao/IA22-23/fase1/assets/GREEDY.png")

pygame.font.init()
fontTXT = pygame.font.SysFont("arial", 20)

pygame.init()
pygame.display.set_caption("VECTOR RACE")
screen= pygame.display.set_mode((750,500))

  

def main():
    menu()

def algo():
    pygame.display.set_caption("MENU VECTOR RACE")
    while (True):
        screen.blit(BACKGROUND,(0,0)) 
        MOUSE = pygame.mouse.get_pos()  
        
        dfs = pygame.transform.scale(DFSBUTTON, (400, 280))
        bfs = pygame.transform.scale(BFSBUTTON, (400, 280))
        astar = pygame.transform.scale(ASTARBUTTON, (400, 280))
        greedy = pygame.transform.scale(GREEDYBUTTON, (400, 280))
        DFSButton= Button(200,100,dfs)
        BFSButton = Button(500,100,bfs)
        ASTARButton = Button(200,350,astar)
        GREEDYButton = Button(500,350,greedy)
        
        DFSButton.update(screen)
        BFSButton.update(screen)
        ASTARButton.update(screen)
        GREEDYButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DFSButton.check(MOUSE):
                    play(1)
                if BFSButton.check(MOUSE):
                    play(2)
                if ASTARButton.check(MOUSE):
                    play(3)
                if GREEDYButton.check(MOUSE):
                    play(4)
        pygame.display.update()   


def play(algo):
    pygame.display.set_caption("VECTOR RACE")
    maze = ["XXXXXXXXXXXXXXXXXFFFXXXXXXXXX",
            "X---------------------------X",
            "X---X-------------------X---X",
            "X---X---XXX----XX-------X---X",
            "X---X-----------------------X",
            "X---X---XXXXXXX---XXXXXX----X",
            "X---------------------------X",
            "X----XXXXXX-------X---------X",
            "X------------XXXXXX---XXXX--X",
            "X--------X--------X---------X",
            "X--------X------------------X",
            "X----X---X---XXXXXXX-----X--X",
            "X----X---X---------------X--X",
            "X----X---------XXXXXXX---X--X",
            "X---------------------------X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

    
    maze1=list()
    linha=list()
    x=y=0
    carx=14#randrange(len(maze))
    cary=3#randrange(len(maze[0]))
    for l in maze:
            for c in l:
                if(x==carx and y==cary):
                    linha.append("P")
                else:
                    linha.append(maze[x][y])
                y+=1
            maze1.append(linha)
            linha=list()
            y=0
            x+=1
    l = list()
    auxmaze1=maze1
    circuito=list()
    rowCircuito=list()
    allPieces = list()
    countLine =1
    countColumn = 1
    coordY=len(maze1[0])-1
    coordX=0
    for linha in maze1:
            coordY=len(linha)-1
            l.append(linha)
    for linha in maze1:
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
                    p = Peca("vazio("+str(countLine)+","+str(countColumn)+")",countLine,countColumn,"NONE")
                    player = Player("player1",countLine,countColumn,0,0)
                    rowCircuito.append('P')
                allPieces.append(p)
                countColumn +=1
            countLine +=1
            countColumn=1
         
    #for p in allPieces:
    #    print(p.get_nome())
    g = Grafo(allPieces,coordX,coordY)
    for piece in allPieces:
        g.constroiGrafo(g.devolvePecabyNome(piece))
        #print(g.devolvePeca(3,11))
        #for pecinha in allPieces:
        #    print(pecinha)
    
    vis=list()
    path=list()
    print(str("posição inicial do carro: ")+str((player.get_posx(),player.get_posy())))
    carroX=player.get_posx()
    carroY=player.get_posy()
    
    if algo==1:
        visited=set()
        path=list()
        print("dfs")
        (caminho,custo,tempo)=g.procuraDFS(player,path,visited)
    if algo==2:
        print("bfs")
        (caminho,custo,tempo)=g.procuraBFS(player)
    if algo==3:
        print("star")
        (caminho,custo,tempo)=g.aStar(player)
    if algo==4:
        print("greedy")
        (caminho,custo,tempo)=g.GreedyAlgorithm(player,vis,path)

    print((caminho,custo,tempo))
    i=0
    lastPiece=""
    futurePiece=""
    while(True):
        walls = []
        metas = []
        players = []
        x = y = 0
        for row in maze1:
            for col in row:
                if col == "X":
                    p =Peca("parede("+str(x)+","+str(y)+")",x,y,"WALL")
                    walls.append(p)
                if col == "F":
                    p =Peca("meta("+str(x)+","+str(y)+")",x,y,"META")
                    metas.append(p)
                if col == "P":
                    p =Player("player1",x,y,0,0)
                    players.append(p)
                x += 17
            y += 17
            x = 0
        screen.fill((0,0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_q]:
            pygame.quit()

        for wall in walls:
            if wall.get_tipo().__eq__("PLAYER"):
                pygame.draw.rect(screen,RED,wall.rect)
            else: pygame.draw.rect(screen, BLUE, wall.rect)
        for meta in metas:
            if meta.get_tipo().__eq__("PLAYER"):
                pygame.draw.rect(screen,RED,meta.rect)
            else: pygame.draw.rect(screen, WHITE, meta.rect)
        for player in players:
            pygame.draw.rect(screen,RED,player.rect)
        pygame.display.flip()
        time.sleep(1)
        if(i==len(caminho)):
            break
        carx=caminho[i][0]
        cary=caminho[i][1]
        maze2=list()
        linha = list()
        x=y=0

        if(i==0): 
            lastPiece="-"
        else: 
            lastPiece=auxmaze1[caminho[i-1][0]-1][caminho[i-1][1]-1]
        for l in maze1:
            for c in l:
                if(x==carx-1 and y==cary-1):
                    linha.append("P")
                elif(maze1[x][y]=="P" and lastPiece=="X"):
                    linha.append("X")
                elif(maze1[x][y]=="P" and lastPiece=="-"):
                    linha.append("-")
                else:
                    linha.append(maze1[x][y])
                y+=1
            maze2.append(linha)
            linha=list()
            y=0
            x+=1
        maze1=maze2
        if(i>0):
            print("coord: "+str(caminho[i-1][0])+";"+str(caminho[i-1][1]))
            # print(auxmaze1[caminho[i-1][0]][caminho[i-1][1]])
        eeline=""
        for e in auxmaze1:
            for ee in e:
                eeline+=ee
            print(eeline)
            eeline=""
        i+=1
    text=fontTXT.render("Custo: "+str(custo),1,WHITE)
    screen.blit(text,(550,200))
    pygame.display.update()
    time.sleep(2)
    main()

def menu():
    pygame.display.set_caption("MENU VECTOR RACE")
    while (True):
        screen.blit(BACKGROUND,(0,0))   
        MOUSE = pygame.mouse.get_pos()
        start = pygame.transform.scale(STARTBUTTON, (200, 80))
        quit = pygame.transform.scale(QUITBUTTON, (200, 80))
        startButton= Button(360,200,start)
        quitButton = Button(360,300,quit)
        
        startButton.update(screen)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.check(MOUSE):
                    algo()
                if quitButton.check(MOUSE):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()   


if __name__ == "__main__":
    main()
