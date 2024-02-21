'''Fichier Pour La Conception Du Menu'''
import pygame, os
SonMenu = 'Son\somambiant.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SonMenu)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.04)
from classes.Bouton import Button
import time


'''Création Fenêtre Pour menu'''
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
Musique1 = pygame.image.load('Graphisme\Boutons\Anote_Musique_On.png')
Musique2 = pygame.image.load('Graphisme\Boutons\Anote_Musique_Off.png')


#Time fps
fps = 60
timer = pygame.time.Clock()

# Créer des instances de bouton
QuitterN = Button(screen_width / 2, screen_height / 2, QuitterNoir, 1)  #Bouton quitter
OptionN = Button(screen_width / 2, screen_height / 2 - 150, OptionsNoir,1)  #Bouton Option
Icone = Button(screen_width - 100, screen_height / 100, Iconeimg,1)  #Bouton pour mettre en fullscreen
PlayN = Button(screen_width / 2, screen_height / 2-300, PlayNoir,1)  #Bouton pour jouer
QuitterO = Button(screen_width / 2, screen_height / 2 - 25, QuitterOrange, 1)
OptionO = Button(screen_width / 2, screen_height / 2-175, OptionOrange, 1)
PlayO = Button(screen_width / 2, screen_height / 2-325, PlayOrange, 1)
MusiqueOn = Button(screen_width - screen_width + 210, screen_height /100 , Musique1, 0.15)
MusiqueOff = Button(screen_width - screen_width + 350, screen_height / 100, Musique2, 0.15)

Quitter = (QuitterN,QuitterO)
Jouer = (PlayN,PlayO)
Option = (OptionN,OptionO)
Musique = (MusiqueOn, MusiqueOff)
#Action en cas de clic

music_enabled = True



# Boucle De jeu
running = True
def Menu():
while running:
    # Arrière Plan
    timer.tick(fps)
    screen.blit(Imagefond, (0, 0))
    # Dessiner les boutons
    Jouer[0].draw(screen)
    Icone.draw(screen)
    Option[0].draw(screen)
    Quitter[0].draw(screen)
    Jouer[1].draw(screen)
    Icone.draw(screen)
    Option[1].draw(screen)
    Quitter[1].draw(screen)
    if music_enabled:
          Musique[0].draw(screen)
    else:
          Musique[1].draw(screen)

    for event in pygame.event.get():  # Récupère les actions du joueur
      if event.type == pygame.QUIT:  # Si le joueur veut quitter la fenêtre
        running = False
        print('Le jeu se ferme')
      if Jouer[0].est_dans(): #Si le curseur est dans le bouton noir
        Jouer[0].rect.topleft = (-500,Jouer[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
        Jouer[1].rect.topleft = (Jouer[1].coordonnee[0] - Jouer[1].width/2,Jouer[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
      if Jouer[1].clique(screen): #Si on clique gauche dans la zone du bouton
        pygame.quit()
      if Jouer[0].est_dans() == False and Jouer[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
        Jouer[0].rect.topleft = (Jouer[0].coordonnee[0] - Jouer[0].width/2,Jouer[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
        Jouer[1].rect.topleft = (-800 ,Jouer[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
      if Option[0].est_dans(): #Si le curseur est dans le bouton noir
        Option[0].rect.topleft = (-500,Option[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
        Option[1].rect.topleft = (Option[1].coordonnee[0] - Option[1].width/2,Option[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
      if Option[1].clique(screen): #Si on clique gauche dans la zone du bouton
        pygame.quit()
      if Option[0].est_dans() == False and Option[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
        Option[0].rect.topleft = (Option[0].coordonnee[0] - Option[0].width/2,Option[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
        Option[1].rect.topleft = (-800 ,Option[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
      if Quitter[0].est_dans(): #Si le curseur est dans le bouton noir
        Quitter[0].rect.topleft = (-500,Quitter[0].coordonnee[1]) #Met le bouton Noir en dehors de la résolution
        Quitter[1].rect.topleft = (Quitter[1].coordonnee[0] - Quitter[1].width/2,Quitter[1].coordonnee[1]) #Met le bouton Orange à la place du bouton Noir
      if Quitter[1].clique(screen): #Si on clique gauche dans la zone du bouton
        pygame.quit() #Quitte la fenêtre
      if Quitter[0].est_dans() == False and Quitter[1].est_dans() == False: #Si on est ni dans le bouton Noir ni dans le bouton Orange
        Quitter[0].rect.topleft = (Quitter[0].coordonnee[0] - Quitter[0].width/2,Quitter[0].coordonnee[1]) #Remet le bouton Noir à ses coordonnées d'origine
        Quitter[1].rect.topleft = (-800 ,Quitter[0].coordonnee[1]) #Met le bouton Orange en dehors de la résolution
      if Icone.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONUP:  # Si un clic de souris est détecté
        if event.button == 1:
          pygame.display.toggle_fullscreen()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if Musique[0].est_dans() and Musique[0].clique(screen):
          pygame.mixer.music.pause()
          music_enabled = False
          Musique[0].rect.topleft = (-2000, Musique[0].coordonnee[1])
          Musique[1].rect.topleft = (Musique[1].coordonnee[0] - Musique[1].width / 2-67, Musique[1].coordonnee[1])
      elif Musique[1].est_dans() and Musique[1].clique(screen):
          pygame.mixer.music.unpause()
          music_enabled = True
          Musique[1].rect.topleft = (-2000, Musique[1].coordonnee[1])
          Musique[0].rect.topleft = (Musique[0].coordonnee[0] - Musique[0].width / 2, Musique[0].coordonnee[1])


  pygame.display.update()

pygame.quit()  # Ferme la fenêtre


