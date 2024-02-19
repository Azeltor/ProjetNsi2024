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