import pygame
class vie:
  max_health = 100
  health = 20
  ratio = health / max_health

  pygame.draw.rect(screen, "red", (250, 250, 300, 40))
  pygame.draw.rect(screen, "green", (250, 250, 300 * ratio, 40))
