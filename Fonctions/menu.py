'''Fichier Pour La Conception Du Menu'''
import sys
sys.path.append('classes')

'''Création Fenêtre Pour menu'''
from Bouton import Button
import pygame, os
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
pygame.display.set_caption('Test Jeu')
screen = pygame.display.set_mode((screen_width - 10, screen_height - 50),pygame.RESIZABLE)

'''Chargement Des Images'''
Imagefond = pygame.image.load('Graphisme\Background\Bg.jpg')
Imagefond = pygame.transform.scale(Imagefond, (screen_width, screen_height))
QuitterNoir = pygame.image.load('Graphisme\Boutons\Bouton_Quitter_Noir-removebg-preview.png')
QuitterOrange = pygame.image.load('Graphisme\Boutons\Bouton_Quitter_Orange-removebg-preview.png')
OptionOrange = pygame.image.load('Graphisme\Boutons\Bouton_Options_Orange-removebg-preview.png')
OptionsNoir = pygame.image.load('Graphisme\Boutons\Bouton_Options_Noir-removebg-preview.png')
PlayNoir = pygame.image.load('Graphisme\Boutons\Bouton_Jouer_Noir-removebg-preview.png')
PlayOrange = pygame.image.load('Graphisme\Boutons\Bouton_Jouer_Orange-removebg-preview.png')
Iconeimg = pygame.image.load('Graphisme\Boutons\icone.png')

#Time fps
fps = 60
timer = pygame.time.Clock()

# Créer des instances de bouton
Quitter = Button(screen_width / 2, screen_height / 2, QuitterNoir, 1)  #Bouton quitter
Option = Button(screen_width / 2, screen_height / 2 - 150, OptionsNoir,1)  #Bouton Option
Icone = Button(screen_width - 100, screen_height / 100, Iconeimg,1)  #Bouton pour mettre en fullscreen
Play = Button(screen_width / 2, screen_height / 2-300, PlayNoir,1)  #Bouton pour jouer
QuitterO = Button(screen_width / 2, screen_height / 2, QuitterOrange, 1)
OptionO = Button(screen_width / 2, screen_height / 2-150, OptionOrange, 1)
playO = Button(screen_width / 2, screen_height / 2-300, PlayOrange, 1)
#Action en cas de clic


# Boucle De jeu
running = True
while running:
  # Arrière Plan
  timer.tick(fps)
  screen.blit(Imagefond, (0, 0))

  for event in pygame.event.get():  # Récupère les actions du joueur
    if event.type == pygame.QUIT:  # Si le joueur veut quitter la fenêtre
      running = False
      print('Le jeu se ferme')
    if Quitter.draw(screen):
       pygame.quit()
    if Icone.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:  # Si un clic de souris est détecté
      if event.button == 1:
        pygame.display.toggle_fullscreen()
  # Dessiner les boutons
  Play.draw(screen)
  Icone.draw(screen)
  Option.draw(screen)
  Quitter.draw(screen)

  pygame.display.update()

pygame.quit()  # Ferme la fenêtre