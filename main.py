import sys
import pygame
from pygame.locals import QUIT

pygame.init()

cornerradius = 10

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Game')

def atob(a,b):
  return (b[0]-a[0], b[1]-a[1])

def draw1(c1,c2):
  size = atob(c1, c2)
  pygame.draw.rect(screen, (99,99,99), pygame.Rect(atob((0,-cornerradius), c1), atob((0,-2*cornerradius), size)))
  pygame.draw.rect(screen, (99,99,99), pygame.Rect(atob((-cornerradius,0), c1), atob((-2*cornerradius,0), size)))
  pygame.draw.circle(screen, (99,99,99), atob((-cornerradius,-cornerradius), c1), cornerradius)
  pygame.draw.circle(screen, (99,99,99), atob((cornerradius,cornerradius), c2), cornerradius)
  pygame.draw.circle(screen, (99,99,99), atob((-cornerradius,cornerradius), (c1[0], c2[1])), cornerradius)
  pygame.draw.circle(screen, (99,99,99), atob((cornerradius,-cornerradius), (c2[0], c1[1])), cornerradius)

draw1((50,400), (550, 550))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
