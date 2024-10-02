#!/usr/bin/python3

import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
NOIR = (200, 0, 0)
BLANC = (255, 255, 255)

# Définition de la taille de l'écran
LARGEUR = 1500
HAUTEUR = 500

# Création de l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Fred-Pong")

# Définition des raquettes et de la balle
raquette_largeur = 15
raquette_hauteur = 70
balle_taille = 15

joueur = pygame.Rect(50, HAUTEUR//2 - raquette_hauteur//2, raquette_largeur, raquette_hauteur)
ordinateur = pygame.Rect(LARGEUR - 50 - raquette_largeur, HAUTEUR//2 - raquette_hauteur//2, raquette_largeur, raquette_hauteur)
balle = pygame.Rect(LARGEUR//2 - balle_taille//2, HAUTEUR//2 - balle_taille//2, balle_taille, balle_taille)

# Vitesse de la balle
balle_vitesse_x = 7 * random.choice((1, -1))
balle_vitesse_y = 7 * random.choice((1, -1))

# Vitesse des raquettes
vitesse_raquette = 10

# Boucle principale du jeu
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Mouvement du joueur
    touches = pygame.key.get_pressed()
    if touches[pygame.K_UP] and joueur.top > 0:
        joueur.y -= vitesse_raquette
    if touches[pygame.K_DOWN] and joueur.bottom < HAUTEUR:
        joueur.y += vitesse_raquette

    # Mouvement de l'ordinateur
    if ordinateur.top < balle.y:
        ordinateur.y += vitesse_raquette
    if ordinateur.bottom > balle.y:
        ordinateur.y -= vitesse_raquette

    # Mouvement de la balle
    balle.x += balle_vitesse_x
    balle.y += balle_vitesse_y

    # Collision avec les bords
    if balle.top <= 0 or balle.bottom >= HAUTEUR:
        balle_vitesse_y *= -1
    if balle.left <= 0 or balle.right >= LARGEUR:
        balle.center = (LARGEUR//2, HAUTEUR//2)
        balle_vitesse_x *= random.choice((1, -1))
        balle_vitesse_y *= random.choice((1, -1))

    # Collision avec les raquettes
    if balle.colliderect(joueur) or balle.colliderect(ordinateur):
        balle_vitesse_x *= -1

    # Dessin des éléments
    ecran.fill(NOIR)
    pygame.draw.rect(ecran, BLANC, joueur)
    pygame.draw.rect(ecran, BLANC, ordinateur)
    pygame.draw.ellipse(ecran, BLANC, balle)
    pygame.draw.aaline(ecran, BLANC, (LARGEUR//2, 0), (LARGEUR//2, HAUTEUR))

    # Mise à jour de l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()