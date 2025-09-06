import time
from Grafo import Grafo
from Peca import Peca
from Player import Player
from Button import Button
from Simulation import Simulation
from PathfindingThread import PathfindingThread
from pathlib import Path
import pygame , sys
import os
from random import randrange

# --- Cores e Recursos (Constantes) ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
background_original = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/vector.JPG")
BACKGROUND = pygame.transform.scale(background_original, (950, 600))
# Carregar as imagens dos botões
STARTBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/thumbnail_startbutton.png")
QUITBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/thumbnail_quitbutton.png")
DFSBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/DFS.png")
BFSBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/BFS.png")
ASTARBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/ASTAR.png")
GREEDYBUTTON = pygame.image.load("/home/joao/VectorRace/multiplayer-vectorace/assets/GREEDY.png")

# Função para criar uma versão "hover" da imagem
def darken_image(image):
    dark_img = image.copy()
    dark_overlay = pygame.Surface(dark_img.get_size(), pygame.SRCALPHA)
    dark_overlay.fill((0, 0, 0, 10))
    dark_img.blit(dark_overlay, (0, 0))
    return dark_img

DFSBUTTON_HOVER = darken_image(DFSBUTTON)
BFSBUTTON_HOVER = darken_image(BFSBUTTON)
ASTARBUTTON_HOVER = darken_image(ASTARBUTTON)
GREEDYBUTTON_HOVER = darken_image(GREEDYBUTTON)

pygame.font.init()
fontTXT = pygame.font.SysFont("arial", 20)
pygame.init()
screen= pygame.display.set_mode((950,600))

# --- Variáveis Globais para Multithreading ---
player_results = []
player_threads = []


# --- Funções do Jogo ---

def menu():
    pygame.display.set_caption("MENU VECTOR RACE")
    while True:
        screen.blit(BACKGROUND, (0,0))
        MOUSE = pygame.mouse.get_pos()
        
        start_scaled = pygame.transform.scale(STARTBUTTON, (200, 80))
        quit_scaled = pygame.transform.scale(QUITBUTTON, (200, 80))
        
        startButton = Button(360, 200, start_scaled, hover_image=None) 
        quitButton = Button(360, 300, quit_scaled, hover_image=None)      

        
        startButton.update(screen)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.check_click(MOUSE):
                    algo()
                if quitButton.check_click(MOUSE):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def algo():
    pygame.display.set_caption("MENU VECTOR RACE")
    while True:
        screen.blit(BACKGROUND, (0,0))
        MOUSE = pygame.mouse.get_pos()
        
        dfs_scaled = pygame.transform.scale(DFSBUTTON,(400, 280))
        bfs_scaled = pygame.transform.scale(BFSBUTTON,(400, 280))
        astar_scaled = pygame.transform.scale(ASTARBUTTON,(400, 280))
        greedy_scaled = pygame.transform.scale(GREEDYBUTTON,(400, 280))
        
        DFSButton = Button(150, 150, dfs_scaled)
        BFSButton = Button(400, 150, bfs_scaled)
        ASTARButton = Button(150, 300, astar_scaled)
        GREEDYButton = Button(400, 300, greedy_scaled)
        
        for button in [DFSButton, BFSButton, ASTARButton, GREEDYButton]:
            button.check_hover(MOUSE)
        
        for button in [DFSButton, BFSButton, ASTARButton, GREEDYButton]:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DFSButton.check_click(MOUSE):
                    play(1)
                if BFSButton.check_click(MOUSE):
                    play(2)
                if ASTARButton.check_click(MOUSE):
                    play(3)
                if GREEDYButton.check_click(MOUSE):
                    play(4)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def play(algo):
    global player_results
    pygame.display.set_caption("VECTOR RACE")

    maze_template = ["XXXXXXXXXXXXXXXXXFFFXXXXXXXXX",
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

    num_players = 2
    players = []
    player_colors = {0: RED, 1: GREEN}
    
    maze_current = [list(row) for row in maze_template]

    for i in range(num_players):
        while True:
            carx = randrange(len(maze_current))
            cary = randrange(len(maze_current[0]))
            if maze_current[carx][cary] == '-':
                players.append(Player(f"player_{i}", carx + 1, cary + 1, 0, 0))
                maze_current[carx][cary] = str(i)
                break

    allPieces = []
    for r_idx, row in enumerate(maze_current):
        for c_idx, cell in enumerate(row):
            if cell == 'X':
                allPieces.append(Peca(f"parede({r_idx+1},{c_idx+1})", r_idx+1, c_idx+1, "WALL"))
            elif cell == 'F':
                allPieces.append(Peca(f"meta({r_idx+1},{c_idx+1})", r_idx+1, c_idx+1, "META"))
            else:
                 allPieces.append(Peca(f"vazio({r_idx+1},{c_idx+1})", r_idx+1, c_idx+1, "NONE"))

    g = Grafo(allPieces, len(maze_current), len(maze_current[0]))
    for piece in allPieces:
        g.constroiGrafo(g.devolvePecabyNome(piece))

    player_threads = []
    player_results = []
    for player in players:
        thread = PathfindingThread(player, g, algo)
        player_threads.append(thread)
        thread.start()

    while any(thread.is_alive() for thread in player_threads):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        loading_text = fontTXT.render("Calculando caminhos...", True, WHITE)
        text_rect = loading_text.get_rect(center=(750/2, 500/2))
        screen.blit(loading_text, text_rect)
        pygame.display.flip()
    
    for thread in player_threads:
        player_results.append({'player': thread.player, 'path': thread.path, 'cost': thread.cost, 'time': thread.time})

    if not all(res['path'] for res in player_results):
        print("Um ou mais jogadores não encontraram um caminho.")
        time.sleep(2)
        return

    simulation_start_time = time.time()
    path_indices = [0] * num_players
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        cell_size = 17
        
        for r, row in enumerate(maze_template):
            for c, cell in enumerate(row):
                rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
                if cell == 'X':
                    pygame.draw.rect(screen, BLUE, rect)
                elif cell == 'F':
                    pygame.draw.rect(screen, WHITE, rect)
        
        for i, result in enumerate(player_results):
            player_path = result['path']
            current_index = path_indices[i]
            
            if current_index < len(player_path):
                pos = player_path[current_index]
                rect = pygame.Rect((pos[1] - 1) * cell_size, (pos[0] - 1) * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, player_colors[i], rect)
        
        for i in range(num_players):
            if path_indices[i] < len(player_results[i]['path']):
                path_indices[i] += 1
        
        simulation_elapsed_time = time.time() - simulation_start_time
        
        y_offset = 400
        for i, result in enumerate(player_results):
            tempo_algoritmo_segundos = result['time'].total_seconds()
            text_info = fontTXT.render(f"P{i+1} Custo: {result['cost']} | Tempo de Busca: {round(tempo_algoritmo_segundos, 10)}s", True, player_colors[i])
            screen.blit(text_info, (80, y_offset + i * 40)) # Posição X alterada para 480

        sim_time_text = fontTXT.render(f"Tempo de Simulação: {round(simulation_elapsed_time, 2)}s", True, WHITE)
        screen.blit(sim_time_text, (80, y_offset + num_players * 40 + 10)) # Posição X alterada para 480        
        
        pygame.display.flip()
        time.sleep(0.5)

        if all(idx >= len(res['path']) for idx, res in zip(path_indices, player_results)):
            time.sleep(2)
            menu()
            break

if __name__ == "__main__":
    menu()