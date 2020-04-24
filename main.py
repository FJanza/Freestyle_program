import sys, pygame
from pygame.locals import *
import time





WIDTH = 960
HEIGHT = 480

#--------------------------------------------------

#--------------------------------------------------
def options():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    button_texto_image = load_image('data/button_texto.png')
    button_exit_image = load_image('data/button_EXIT.png')
    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')





    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 45, True)
    Track_selection = fuente_texto.render("Track Selection", 0, (84, 83, 83),(157,156,156))
    Time_selection = fuente_texto.render("Time Selection", 0, (84,83,83),(157,156,156))





    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(button_texto_image,(50,50))
        screen.blit(Track_selection,(60,63))
        screen.blit(button_texto_image, (50, 150))
        screen.blit(Time_selection,(60,163))
        screen.blit(button_exit_image, (50, 330))

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
                                return



        pygame.display.flip()
#--------------------------------------------------
def mode_election():


    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    background_image = load_image('data/fondo.png')

    buttonpressed_easy_image = load_image('data/buttonpressed_easy.png')
    button_easy_image = load_image('data/button_easy.png')
    easy_description_image = load_image('data/easy_description.png')


    buttonpressed_medio_image = load_image('data/buttonpressed_medio.png')
    button_medio_image = load_image('data/button_medio.png')
    medio_description_image = load_image('data/medio_description.png')


    buttonpressed_libre_image = load_image('data/buttonpressed_libre.png')
    button_libre_image = load_image('data/button_libre.png')
    libre_description_image = load_image('data/libre_description.png')


    buttonpressed_start_image = load_image('data/buttonpressed_start .png')
    button_start_image = load_image('data/button_start.png')

    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                 sys.exit(0)





        screen.blit(background_image,(0,0))
        screen.blit(button_easy_image, (100, 100))
        screen.blit(button_medio_image,(385, 100))
        screen.blit(button_libre_image,(670,100))
        screen.blit(button_start_image,(455,405))



        if eventos.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
            objetivo = pygame.mouse.get_pos()
            if objetivo[0] < 300:
                if objetivo[0] > 100:
                    if objetivo[1] < 200:
                        if objetivo[1] > 100:
                            screen.blit(easy_description_image, (215, 255))
        if eventos.type == pygame.MOUSEBUTTONDOWN:  # presiono easy
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 300:
                    if objetivo[0] > 100:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_easy_image, (100, 100))
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando paso por encima de easy muestra la desc
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 300:
                    if objetivo[0] > 100:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                return("easy")

        if eventos.type == pygame.MOUSEMOTION:  #cuando paso por encima de medio muestra la desc
                objetivo = pygame.mouse.get_pos()
                if objetivo[0] < 585:
                    if objetivo[0] > 385:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(medio_description_image, (215, 255))
        if eventos.type == pygame.MOUSEBUTTONDOWN:  # presiono medio
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 585:
                    if objetivo[0] > 385:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_medio_image, (385, 100))
        if eventos.type == pygame.MOUSEBUTTONUP:  # presiono medio
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 585:
                    if objetivo[0] > 385:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                return("medio")

        if eventos.type == pygame.MOUSEMOTION:  # paso por encima de libre muestra la desc
            objetivo = pygame.mouse.get_pos()
            if objetivo[0] < 870:
                if objetivo[0] > 670:
                    if objetivo[1] < 200:
                        if objetivo[1] > 100:
                            screen.blit(libre_description_image, (215, 255))
        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto libre
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 870:
                    if objetivo[0] > 670:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                screen.blit(buttonpressed_libre_image, (670, 100))
        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto libre
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 870:
                    if objetivo[0] > 670:
                        if objetivo[1] < 200:
                            if objetivo[1] > 100:
                                return("libre")

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 505:
                    if objetivo[0] > 455:
                        if objetivo[1] < 455:
                            if objetivo[1] > 405:
                                screen.blit(buttonpressed_start_image, (455, 405))
        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if objetivo[0] < 505:
                    if objetivo[0] > 455:
                        if objetivo[1] < 455:
                            if objetivo[1] > 405:
                                options()
                                return mode_election()






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
                if objetivo[0] < 810:
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
    mode_election()

    modo = mode_election()


    if modo == "easy":
         print("easy")

    elif modo == "medio":
         print("medio")

    elif modo == "libre":
         print("libre")



    return 0
#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()

