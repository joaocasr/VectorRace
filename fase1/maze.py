import pygame
import os
from Peca import Peca

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


pygame.init()
pygame.display.set_caption("VECTOR RACE")
screen= pygame.display.set_mode((1200,800))

maze = ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X------X-----X--------X---------X",
        "X------X-----X--------X---------X",
        "X------X-----X----XXXXXXXXXX----X",
        "X------X-----X------------------X",
        "X------------X------------------X",
        "X-----------------------------XXX",
        "X-----XXXX------------X-------F-X",
        "X---------------------X-------F-X",
        "X---------------------X-------F-X",
        "X-----------------------------XXX",
        "X-------------------------------X",
        "X--------------------XXX--------X",
        "X------------X--------X---------X",
        "X--P---------X--------X---------X",
        "X------------X------------------X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
walls = []
metas = []
x = y = 0
for row in maze:
    for col in row:
        if col == "X":
            p =Peca("parede("+str(x)+","+str(y)+")",x,y,"WALL")
            walls.append(p)
        if col == "F":
            p =Peca("meta("+str(x)+","+str(y)+")",x,y,"META")
            metas.append(p)
        x += 16
    y += 16
    x = 0

while(True):
    screen.fill((0,0,0))
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall.rect)
    for meta in metas:
        pygame.draw.rect(screen,WHITE,meta.rect)
    pygame.display.flip()