# Modules / Libraries
import sys
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN

pygame.init()




# Constants
cornerradius = 20
items = ("Rock","Paper","Scissors")

screen = pygame.display.set_mode((800, 800))
pygameclock = pygame.time.Clock()




# Variables
sections = ([],[],[])
images = []
change = True
selection = None
mouse = (-1,-1)




# Functions
def atob(a,b):
  return (b[0]-a[0], b[1]-a[1])

def draw2(c1,c2, colour, cr):
  size = atob(c1, c2)
  pygame.draw.rect(screen, colour, pygame.Rect(atob((0,-cr), c1), atob((0,2*cr), size)))
  pygame.draw.rect(screen, colour, pygame.Rect(atob((-cr,0), c1), atob((2*cr,0), size)))
  pygame.draw.circle(screen, colour, atob((-cr,-cr), c1), cr)
  pygame.draw.circle(screen, colour, atob((cr,cr), c2), cr)
  pygame.draw.circle(screen, colour, atob((-cr,cr), (c1[0], c2[1])), cr)
  pygame.draw.circle(screen, colour, atob((cr,-cr), (c2[0], c1[1])), cr)

def draw1(c1,c2, colour):
  draw2(c1,c2, colour, cornerradius)

def newsection(c1, c2, colour, layer, uponclick):
  x = (c1,c2,colour, uponclick)
  sections[layer].append(x)
  return x

def oncoord(coord):
  for i in range(len(sections)-1,-1,-1):
    layer = sections[i]
    for j in range(len(layer)-1,-1,-1):
      section = layer[j]
      t1 = coord[0] - (section[0][0] + cornerradius)
      t2 = (section[1][0] - cornerradius) - coord[0]
      x = min(t1,t2)
      t1 = coord[1] - (section[0][1] + cornerradius)
      t2 = (section[1][1] - cornerradius) - coord[1]
      y = min(t1,t2)
      if (x >= 0 and y >=0) or (x >= 0 and y >= -cornerradius) or (x >= -cornerradius and y >= 0) or (x**2 + y**2 <= cornerradius**2):
        if section[3]:
          return section,i
        else:
          return None,None
  return None,None

def itemclick(i):
  def thing():
    print("player clicked the "+items[i])
  return thing





# Execute
pygame.display.set_caption('Game')

newsection((25,575), (775,775), (222,222,222), 0, None)

for i in range(len(items)):
  corner = (100+225*i,600)
  newsection(corner, (250+225*i,750), (177,177,177), 1, itemclick(i))
  image = pygame.image.load("assets/"+items[i]+".png")
  image = pygame.transform.scale(image, (150,150))
  image = image.convert_alpha()
  images.append((corner, image))



while True:
  pygameclock.tick(60)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
      if selection and event.button == 1:
        selection[3]()
  
  newmouse = pygame.mouse.get_pos()
  if newmouse[0] != mouse[0] or newmouse[1] != mouse[1]:
    mouse = newmouse
    change = True
    section,l = oncoord(mouse)
    if section:
      selection = ((section[0][0]-5, section[0][1]-5), (section[1][0]+5, section[1][1]+5), l, section[3])
    else:
      selection = None

  if change:
    screen.fill((255,255,255))
    change = False
    for i in range(len(sections)):
      layer = sections[i]
      if selection and selection[2] == i:
        draw2(selection[0], selection[1], (0,0,0), cornerradius+5)
      for section in layer:
        draw1(section[0], section[1], section[2])
    for image in images:
      screen.blit(image[1], image[0])

    pygame.display.update()