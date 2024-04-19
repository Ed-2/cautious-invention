import sys
import pygame
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Game')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
