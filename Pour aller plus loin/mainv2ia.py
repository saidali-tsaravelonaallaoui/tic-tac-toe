import pygame
import sys
from pygame.locals import *
from ia import ia

# Initialisation de pygame
pygame.init()

# Taille de l'écran
screen_width = 600
screen_height = 600

# Création de la surface de l'écran
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe by Allaoui")

line_width = 8
marker = []
clicked = False
pos = []
joueur = 1
gagnant = 0
game_over = False

vert = (0, 255, 0)
rouge = (255, 0, 0)
bleu  = (0, 0, 255)

font = pygame.font.SysFont(None, 40)

# Bouton rejouer
again_rect = Rect(screen_width // 2 - 150, screen_height // 2, 300, 50)

# Dessiner la grille
def draw_grid():
    # Couleur de fond
    bg = (255, 255, 200)
    # Couleur de la grille
    grid = (50, 50, 50)
    # Remplir l'écran avec la couleur de fond
    screen.fill(bg)
    
    # Dessiner les lignes
    for x in range(1, 3):
        # Ligne verticale
        pygame.draw.line(screen, grid, (0, x * 200), (screen_width, x * 200), line_width)
        # Ligne horizontale
        pygame.draw.line(screen, grid, (x * 200, 0), (x * 200, screen_height), line_width)

for x in range(3):
    row = [0] * 3
    marker.append(row)

# Dessiner les marqueurs
def draw_marker():
    x_pos = 0
    for x in marker:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, vert, (x_pos * 200 + 40, y_pos * 200 + 40), (x_pos * 200 + 160, y_pos * 200 + 160), line_width)
                pygame.draw.line(screen, vert, (x_pos * 200 + 40, y_pos * 200 + 160), (x_pos * 200 + 160, y_pos * 200 + 40), line_width)
            if y == -1:
                pygame.draw.circle(screen, rouge, (x_pos * 200 + 100, y_pos * 200 + 100), 70, line_width)
            y_pos += 1
        x_pos += 1
    
# Vérification du gagnant   
def verif_gagnant():
    global gagnant
    global game_over
    
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if sum(marker[i]) == 3 or marker[0][i] + marker[1][i] + marker[2][i] == 3:
            gagnant = 1
            game_over = True
        elif sum(marker[i]) == -3 or marker[0][i] + marker[1][i] + marker[2][i] == -3:
            gagnant = 2
            game_over = True
    
    # Vérification des diagonales
    if marker[0][0] + marker[1][1] + marker[2][2] == 3 or marker[2][0] + marker[1][1] + marker[0][2] == 3:
        gagnant = 1
        game_over = True
    elif marker[0][0] + marker[1][1] + marker[2][2] == -3 or marker[2][0] + marker[1][1] + marker[0][2] == -3:
        gagnant = 2
        game_over = True
    
    # Vérification du match nul
    if all(all(cell != 0 for cell in row) for row in marker) and not game_over:
        gagnant =  "Match Nul !"
        game_over = True
        
# Affichage du gagnant       
def draw_gagnant(gagnant):
    win_text = ""
    if isinstance(gagnant, int):
        win_text = "Le joueur " + str(gagnant) + " a gagné !"
    else:
        win_text = gagnant
        
    # Affichage du match nul    
    nul_text = "Match Nul !"
    nul_img = font.render(nul_text, True, rouge)
    pygame.draw.rect(screen, rouge, (screen_width // 2 - 50, screen_height // 2 - 60, 200, 50))
    screen.blit(nul_img, (screen_width // 2 - 150, screen_height // 2 - 50))
   
   # Affichage du gagnant
    win_img = font.render(win_text, True, bleu)
    pygame.draw.rect(screen, vert, (screen_width // 2 - 150, screen_height // 2 - 60, 300, 50))
    screen.blit(win_img, (screen_width // 2 - 140, screen_height // 2 - 50))
    
    # Bouton rejouer
    again_text = "Cliquez pour rejouer"
    again_img = font.render(again_text, True, bleu)
    pygame.draw.rect(screen, vert, again_rect)
    screen.blit(again_img, (screen_width // 2 - 140, screen_height // 2 + 10))


# Boucle du jeu
run = True
while run:
    draw_grid()
    draw_marker()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 200
                cell_y = pos[1] // 200
                if marker[cell_x][cell_y] == 0:
                    marker[cell_x][cell_y] = joueur
                    joueur *= -1
                    verif_gagnant()

    if joueur == -1 and not game_over:
        position_ia = ia([cell for row in marker for cell in row], -1)
        marker[position_ia // 3][position_ia % 3] = joueur
        joueur *= -1
        verif_gagnant()

    if game_over == True:
        draw_gagnant(gagnant)
        if event.type == MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                joueur = 1
                gagnant = 0
                game_over = False
                marker = [[0] * 3 for _ in range(3)]

    pygame.display.update()

pygame.quit()