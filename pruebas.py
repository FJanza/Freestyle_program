import sys, pygame
from pygame.locals import *
from random import randint, uniform, random


# -*- coding: utf-8 -*-


WIDTH = 960
HEIGHT = 480


#--------------------------------------------------
def timer_60_libre():
    pygame.init()


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)

    clock = pygame.time.Clock()

    counter, text = 61, '61'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Swis721 Blk BT", 80, True)

    while True:

        screen.blit(background_image, (0, 0))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    return mode_libre()




            if counter == 61:
                palabras_text = fuente_texto.render('MODO LIBRE', 0, (84, 83, 83), (157, 156, 156))
                x_centrada = 320




        else:
            pygame.draw.circle(screen, (34,50,100), (480, 200), 70, 0)
            pygame.draw.circle(screen,(247,224,159),(480,200),60, 0)
            pygame.draw.rect(screen, (34, 50, 100), [280,385, 400, 75], 0)
            pygame.draw.rect(screen, (157, 156, 156), [290, 392, 380, 60], 0)




            screen.blit(palabras_text, (x_centrada, 400))
            screen.blit(font.render(text, True, (0, 0, 0)), (423, 175))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
# --------------------------------------------------
def timer_60_medio():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)
    palabras = reco_palabras('data/palabras.txt')

    clock = pygame.time.Clock()

    counter, text = 61, '61'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Swis721 Blk BT", 80, True)

    while True:

        screen.blit(background_image, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if counter == 61 or counter == 51 or counter == 41 or counter == 31 or counter == 21 or counter == 11:
                rannum = randint(0, 1212)

            if counter == 56 or counter == 46 or counter == 36 or counter == 26 or counter == 16 or counter == 6:
                rannum = randint(0, 1212)

            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    return mode_medio()

            if counter == 61:
                palabras_text = fuente_texto.render('YA ARRANCA', 0, (84, 83, 83), (157, 156, 156))
                x_centrada = 320
            if counter % 5 == 0:
                x_centrada = 480 - (((len(palabras[rannum])) / 2) * 25)
                palabras_text = fuente_texto.render(palabras[rannum], 0, (84, 83, 83), (157, 156, 156))




        else:
            pygame.draw.circle(screen, (34, 50, 100), (480, 200), 70, 0)
            pygame.draw.circle(screen, (247, 224, 159), (480, 200), 60, 0)
            pygame.draw.rect(screen, (34, 50, 100), [280, 385, 400, 75], 0)
            pygame.draw.rect(screen, (157, 156, 156), [290, 392, 380, 60], 0)

            screen.blit(palabras_text, (x_centrada, 400))
            screen.blit(font.render(text, True, (0, 0, 0)), (423, 175))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
#--------------------------------------------------
def timer_60_easy():
    pygame.init()


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)
    palabras = reco_palabras('data/palabras.txt')

    clock = pygame.time.Clock()

    counter, text = 61, '61'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Swis721 Blk BT", 80, True)

    while True:

        screen.blit(background_image, (0, 0))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if counter == 61 or counter == 51 or counter == 41 or counter == 31 or counter == 21 or counter == 11:
                rannum = randint(0, 1212)

            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    return mode_easy()




            if counter == 61:
                palabras_text = fuente_texto.render('YA ARRANCA', 0, (84, 83, 83), (157, 156, 156))
                x_centrada = 320
            if counter % 10 == 0:
                x_centrada = 480 - (((len(palabras[rannum])) / 2) * 25)
                palabras_text = fuente_texto.render(palabras[rannum], 0, (84, 83, 83), (157, 156, 156))




        else:
            pygame.draw.circle(screen, (34,50,100), (480, 200), 70, 0)
            pygame.draw.circle(screen,(247,224,159),(480,200),60, 0)
            pygame.draw.rect(screen, (34, 50, 100), [280,385, 400, 75], 0)
            pygame.draw.rect(screen, (157, 156, 156), [290, 392, 380, 60], 0)




            screen.blit(palabras_text, (x_centrada, 400))
            screen.blit(font.render(text, True, (0, 0, 0)), (423, 175))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
#--------------------------------------------------
def mode_libre():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_exit_image = load_image('data/button_EXIT.png')
    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')

    buttonpressed_start_image = load_image('data/buttonpressed_start .png')
    button_start_image = load_image('data/button_start .png')


    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(button_exit_image, (50, 330))
        screen.blit(button_start_image,(455,205))



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    screen.blit(buttonpressed_start_image, (455, 205))
                    timer_60_libre()

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    return mode_libre()


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    return mode_election()

        pygame.display.flip()
#--------------------------------------------------
def mode_medio():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_exit_image = load_image('data/button_EXIT.png')
    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')

    buttonpressed_start_image = load_image('data/buttonpressed_start .png')
    button_start_image = load_image('data/button_start .png')


    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(button_exit_image, (50, 330))
        screen.blit(button_start_image,(455,205))



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    screen.blit(buttonpressed_start_image, (455, 205))
                    timer_60_medio()

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    return mode_medio()


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    return mode_election()

        pygame.display.flip()
#--------------------------------------------------
def mode_easy():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_exit_image = load_image('data/button_EXIT.png')
    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')

    buttonpressed_start_image = load_image('data/buttonpressed_start .png')
    button_start_image = load_image('data/button_start .png')


    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(button_exit_image, (50, 330))
        screen.blit(button_start_image,(455,205))



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    screen.blit(buttonpressed_start_image, (455, 205))
                    timer_60_easy()

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 205 < objetivo[1] < 455:
                    return mode_easy()


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    return mode_election()

        pygame.display.flip()
#--------------------------------------------------
def reco_palabras(ruta):
    archivo_palabras = open(ruta, 'r', encoding='UTF8')
    palabras = archivo_palabras.read().splitlines()
    archivo_palabras.close()
    return (palabras)
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
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    return



        pygame.display.flip()
#--------------------------------------------------
def mode_election():


    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    background_image = load_image('data/fondo.png')

    buttonpressed_easy_image = load_image('data/buttonpressed_easy.png')
    button_easy_image = load_image('data/button_easy.png')

    buttonpressed_medio_image = load_image('data/buttonpressed_medio.png')
    button_medio_image = load_image('data/button_medio.png')


    buttonpressed_libre_image = load_image('data/buttonpressed_libre.png')
    button_libre_image = load_image('data/button_libre.png')


    buttonpressed_options_image = load_image('data/buttonpressed_options .png')
    button_options_image = load_image('data/button_options.png')

    button_exit_image = load_image('data/button_EXIT.png')
    buttonpressed_exit_image = load_image('data/buttonpressed_EXIT.png')

    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 45, True)

    definition_easy = fuente_texto.render("En este modo de juego ", 0, (84, 83, 83), (157, 156, 156))
    definition_easy_2 = fuente_texto.render("habra palabras cada 10 seg", 0, (84, 83, 83), (157, 156, 156))

    definition_medio = fuente_texto.render("En este modo de juego ", 0, (84, 83, 83), (157, 156, 156))
    definition_medio_2 = fuente_texto.render("habra palabras cada 5 seg", 0, (84, 83, 83), (157, 156, 156))

    definition_libre = fuente_texto.render("En este modo de juego", 0, (84, 83, 83), (157, 156, 156))
    definition_libre_2 = fuente_texto.render("no hay palabras solo base", 0, (84, 83, 83), (157, 156, 156))

    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                 sys.exit(0)





        screen.blit(background_image,(0,0))
        screen.blit(button_easy_image, (100, 100))
        screen.blit(button_medio_image,(385, 100))
        screen.blit(button_libre_image,(670,100))
        screen.blit(button_options_image,(455,405))
        screen.blit(button_exit_image, (50, 330))


        if eventos.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
            objetivo = pygame.mouse.get_pos()
            if 100 < objetivo[0] < 300 and 100 < objetivo[1] < 200:
                pygame.draw.rect(screen, (157, 156, 156), pygame.Rect((210, 250, 500, 75)), 0)
                screen.blit(definition_easy, (255, 255))
                screen.blit(definition_easy_2, (215, 285))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # presiono easy
            if eventos.button == 1:
                objetivo = eventos.pos
                if 100 < objetivo[0] < 300 and 100 < objetivo[1] < 200:
                    screen.blit(buttonpressed_easy_image, (100, 100))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando paso por encima de easy muestra la desc
            if eventos.button == 1:
                objetivo = eventos.pos
                if 100 < objetivo[0] < 300 and 100 < objetivo[1] < 200:
                    mode_easy()


        if eventos.type == pygame.MOUSEMOTION:  #cuando paso por encima de medio muestra la desc
                objetivo = pygame.mouse.get_pos()
                if 385 < objetivo[0] < 585 and 100 < objetivo[1] < 200:
                    pygame.draw.rect(screen, (157, 156, 156), pygame.Rect((210, 250, 500, 75)), 0)
                    screen.blit(definition_medio, (255, 255))
                    screen.blit(definition_medio_2, (215, 285))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # presiono medio
            if eventos.button == 1:
                objetivo = eventos.pos
                if 358 < objetivo[0] < 585 and 100 < objetivo[1] < 200:
                    screen.blit(buttonpressed_medio_image, (385, 100))

        if eventos.type == pygame.MOUSEBUTTONUP:  # presiono medio
            if eventos.button == 1:
                objetivo = eventos.pos
                if 385 < objetivo[0] < 585 and 100 < objetivo[1] < 200:
                    mode_medio()


        if eventos.type == pygame.MOUSEMOTION:  # paso por encima de libre muestra la desc
            objetivo = pygame.mouse.get_pos()
            if 670 < objetivo[0] < 870 and 100 < objetivo[1] < 200:
                pygame.draw.rect(screen, (157, 156, 156), pygame.Rect((210, 250, 500, 75)), 0)
                screen.blit(definition_libre, (255, 255))
                screen.blit(definition_libre_2, (215, 285))

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
                if 670 < objetivo[0] < 870 and 100 < objetivo[1] < 200:
                    mode_libre()


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto options
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 405 < objetivo[1] < 455:
                    screen.blit(buttonpressed_options_image, (455, 405))

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto options
            if eventos.button == 1:
                objetivo = eventos.pos
                if 455 < objetivo[0] < 505 and 405 < objetivo[1] < 455:
                    options()
                    return mode_election()

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    sys.exit(0)



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
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_exit_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 330 < objetivo[1] < 430:
                    sys.exit(0)

        if eventos.type == pygame.MOUSEBUTTONDOWN:  ##cambia el color de play cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 610 < objetivo[0] < 810 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_play_image, (610, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  ##cambia el color de play cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 610 < objetivo[0] < 910 and 330 < objetivo[1] < 430:
                    if objetivo[0] > 610:
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
    mode_election()
    return 0
#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()

