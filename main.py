import sys, pygame
from pygame.locals import *
from random import randint

# -*- coding: utf-8 -*-


WIDTH = 960
HEIGHT = 480




#--------------------------------------------------
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error as message:
             raise SystemExit(message)
        image = image.convert()
        if transparent:
             color = image.get_at((0,0))
             image.set_colorkey(color, RLEACCEL)
        return  image
#--------------------------------------------------






