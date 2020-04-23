import sys, pygame
from pygame.locals import *
from tkinter import *


WIDTH = 960
HEIGHT = 480

#--------------------------------------------------

#--------------------------------------------------

#--------------------------------------------------
def seleccion():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    background_image = load_image('data/fondo.png')

    buttonpressed_easy_image = load_image('data/buttonpressed_easy.png')

    button_easy_image = load_image('data/button_easy.png')

    buttonpressed_medio_image = load_image('data/buttonpressed_medio.png')

    button_medio_image = load_image('data/button_medio.png')

    buttonpressed_libre_image = load_image('data/buttonpressed_libre.png')

    button_libre_image = load_image('data/button_libre.png')

    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                 sys.exit(0)





        screen.blit(background_image,(0,0))
        screen.blit(button_easy_image, (100, 100))
        screen.blit(button_medio_image,(385, 100))
        screen.blit(button_libre_image,(670,100))


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de easy cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 300:
                    if objetivo[0] > 100:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_easy_image, (100, 100))

        if eventos.type == pygame.MOUSEBUTTONUP:
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 300:
                    if objetivo[0] > 100:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                print("explicacion")



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de medio cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 585:
                    if objetivo[0] > 385:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_medio_image, (385, 100))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cambia el color de medio cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 685:
                    if objetivo[0] > 385:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                print("explicacion")


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de libre cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 870:
                    if objetivo[0] > 670:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_libre_image, (670, 100))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cambia el color de libre cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 870:
                    if objetivo[0] > 670:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                print("explicacion")


        pygame.display.flip()
#--------------------------------------------------
def menu():

    evento_play = False

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    background_image = load_image('data/fondo.png')

    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')

    button_exit_image = load_image('data/button_EXIT.png')

    buttonpressed_play_image = load_image('data/buttonpressed_PLAY.png')

    button_play_image = load_image('data/button_PLAY.png')

    while evento_play  == False:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)





        screen.blit(background_image,(0,0))
        screen.blit(button_exit_image, (50, 330))
        screen.blit(button_play_image, (610, 330))


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 350:
                    if objetivo[0] > 50:
                        if objetivo[1] < 430:
                            if objetivo[1] > 330:
                                screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 350:
                    if objetivo[0] > 50:
                        if objetivo[1] < 430:
                            if objetivo[1] > 330:
                                sys.exit(0)

        if eventos.type == pygame.MOUSEBUTTONDOWN:  ##cambia el color de play cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 910:
                    if objetivo[0] > 610:
                        if objetivo[1] < 430:
                            if objetivo[1] > 330:
                                screen.blit(buttonpressed_play_image, (610, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  ##cambia el color de play cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 910:
                    if objetivo[0] > 610:
                        if objetivo[1] < 430:
                            if objetivo[1] > 330:
                                evento_play = True

        pygame.display.flip()
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
    menu()
    seleccion()


    return 0
#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()
