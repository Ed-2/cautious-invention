import sys
import pygame
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Game')

def draw1(c1,c2):
  pygame.draw.rect(screen, (99,99,99), pygame.Rect(c1, (c2[0]-c1[0], c2[1]-c1[1])))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
