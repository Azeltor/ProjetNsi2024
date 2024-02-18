import pygame, sys, os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

#Création de la fenêtre puvant être modifiée
pygame.display.set_caption('Test Jeu')
screen = pygame.display.set_mode((screen_width - 10, screen_height - 50),
                                 pygame.RESIZABLE)

#Icone de jeu et Fond du menu
Imagefond = pygame.image.load('Projet/asset/Bg.jpg')
Imagefond = pygame.transform.scale(Imagefond, (screen_width, screen_height))
QuitterNoir = pygame.image.load(
    'asset\Bouton_Quitter_Noir-removebg-preview.png')
QuitterOrange = pygame.image.load(
    'asset\Bouton_Quitter_Orange-removebg-preview.png')
OptionOrange = pygame.image.load(
    'asset\Bouton_Options_Orange-removebg-preview.png')
OptionsNoir = pygame.image.load(
    'asset\Bouton_Options_Noir-removebg-preview.png')
PlayNoir = pygame.image.load('asset\Bouton_Jouer_Noir-removebg-preview.png')
PlayOrange = pygame.image.load(
    'asset\Bouton_Jouer_Orange-removebg-preview.png')
Iconeimg = pygame.image.load('asset\icone.png')

#Time fps
fps = 60
timer = pygame.time.Clock()

#Bouton


class Bouton:

  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()  # Rectangle autour de l'image
    self.rect.topleft = (x - width / 2, y)

  def draw(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))


# Créer des instances de bouton
Play = Bouton(screen_width / 2, screen_height / 2, PlayNoir, 1)  #Bouton play
Option = Bouton(screen_width / 2, screen_height / 2 - 150, OptionsNoir,
                1)  #Bouton Option
Icone = Bouton(screen_width - 100, screen_height / 100, Iconeimg,
               1)  #Bouton pour mettre en fullscreen
Quitter = Bouton(screen_width / 2, screen_height / 2 - 300, QuitterNoir,
                 1)  #Bouton pour quitter


def check_play_button(mouse_pos):
  """Vérifie si le bouton de lecture a été cliqué."""
  if Play.rect.collidepoint(mouse_pos):
    # Si le clic est dans la zone du bouton, quitter le jeu
    pygame.quit()
  if Icone.rect.collidepoint(mouse_pos):
    pygame.display.toggle_fullscreen()
  if Option.rect.collidepoint(mouse_pos):
    pygame.quit()
  if Quitter.rect.collidepoint(mouse_pos):
    pygame.quit()


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
    elif event.type == pygame.MOUSEBUTTONUP:  # Si un clic de souris est détecté
      if event.button == 1:  # Si le clic est le bouton gauche de la souris
        check_play_button(
            event.pos)  # Vérifie si le bouton de lecture a été cliqué

  # Dessiner les boutons
  Play.draw(screen)
  Icone.draw(screen)
  Option.draw(screen)
  Quitter.draw(screen)

  pygame.display.update()

pygame.quit()  # Ferme la fenêtre