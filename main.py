import sys, pygame
from pygame.locals import *
from tkinter import *


WIDTH = 960
HEIGHT = 480

#--------------------------------------------------

#--------------------------------------------------

#--------------------------------------------------

#--------------------------------------------------

#--------------------------------------------------


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
def main():


    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    button_image = load_image('data/button.png')

    background_image = load_image('data/fondo.png')

    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)





        screen.blit(background_image,(0,0))
        screen.blit(button_image, (50, 330))
        screen.blit(button_image, (610, 330))



        pygame.display.flip()
    return 0
#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()
