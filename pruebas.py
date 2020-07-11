import sys, pygame
from pygame.locals import *
from random import randint


# -*- coding: utf-8 -*-


WIDTH = 960
HEIGHT = 480




def timer_libre(tiempo_elegido):
    tiempo_elegido = 120

    pygame.init()

    music(options())

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)

    clock = pygame.time.Clock()

    counter, text = tiempo_elegido, '{}'.format(tiempo_elegido).rjust(3)
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
                    return #retorna a la funcion mode_libre




            if counter == tiempo_elegido:
                palabras_text = fuente_texto.render('MODO LIBRE', 0, (84, 83, 83), (157, 156, 156))
                x_centrada = 320




        else:
            pygame.draw.circle(screen, (34,50,100), (480, 200), 70, 0)  #circulo azul
            pygame.draw.circle(screen,(247,224,159),(480,200),60, 0)    #circulo blanco
            pygame.draw.rect(screen, (34, 50, 100), [280,385, 400, 75], 0)
            pygame.draw.rect(screen, (157, 156, 156), [290, 392, 380, 60], 0)




            screen.blit(palabras_text, (x_centrada, 400))
            screen.blit(font.render(text, True, (0, 0, 0)), (423, 175))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
#--------------------------------------------------
def music(path):
    pygame.mixer.music.load(path)

    if (path == 'data/base_rap_4.mp3'):
        pygame.mixer.music.play(loops=0, start=9.0)

    if (path != 'data/base_rap_0.mp3'):
        pygame.mixer.music.play(loops=0, start=10.0)

    if (path == 'data/base_rap_0.mp3'):
        pygame.mixer.music.play()
#--------------------------------------------------        
def previsualization_music(path):
    music(path)

    clock = pygame.time.Clock()
    counter = 10
    pygame.time.set_timer(pygame.USEREVENT, 1000)
   

    while True:

        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if e.type == pygame.USEREVENT:
                counter -= 1
                if counter == 0:
                    pygame.mixer.music.stop()
                    return #este return vuelve a la funcion Track_selection

        else:            
            clock.tick(60)
            continue
        break           
#--------------------------------------------------
def timer_120_libre():


    pygame.init()

    music(options())

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
                    return # retorna a la funcion  mode_libre




            if counter == 121:
                palabras_text = fuente_texto.render('MODO LIBRE', 0, (84, 83, 83), (157, 156, 156))
                x_centrada = 320




        else:
            pygame.draw.circle(screen, (34,50,100), (480, 200), 70, 0)  #circulo azul
            pygame.draw.circle(screen,(247,224,159),(480,200),60, 0)    #circulo blanco
            pygame.draw.rect(screen, (34, 50, 100), [280,385, 400, 75], 0)
            pygame.draw.rect(screen, (157, 156, 156), [290, 392, 380, 60], 0)




            screen.blit(palabras_text, (x_centrada, 400))
            screen.blit(font.render(text, True, (0, 0, 0)), (423, 175))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
# --------------------------------------------------
def timer_120_medio():
    pygame.init()

    music(options())

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)
    palabras = reco_palabras('data/palabras.txt')

    clock = pygame.time.Clock()

    counter, text = 121, '121'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Swis721 Blk BT", 80, True)

    while True:

        screen.blit(background_image, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if counter == 121 or counter == 111 or counter == 101 or counter == 91 or counter == 81 or counter == 71:
                rannum = randint(0, 1212)

            if counter == 116 or counter == 106 or counter == 96 or counter == 86 or counter == 76 or counter == 66:
                rannum = randint(0, 1212)

            if counter == 61 or counter == 51 or counter == 41 or counter == 31 or counter == 21 or counter == 11:
                rannum = randint(0, 1212)

            if counter == 56 or counter == 46 or counter == 36 or counter == 26 or counter == 16 or counter == 6:
                rannum = randint(0, 1212)

            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    return #retorna al mode_medio

            if counter == 121:
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
def timer_120_easy():
    pygame.init()

    music(options())


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 60, True)
    palabras = reco_palabras('data/palabras.txt')

    clock = pygame.time.Clock()

    counter, text = 121, '121'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("Swis721 Blk BT", 80, True)

    while True:

        screen.blit(background_image, (0, 0))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if counter == 121 or counter == 111 or counter == 101 or counter == 91 or counter == 81 or counter == 71:
                rannum = randint(0, 1212)

            if counter == 61 or counter == 51 or counter == 41 or counter == 31 or counter == 21 or counter == 11:
                rannum = randint(0, 1212)

            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    return #este return vuelve a la funcion mode_easy




            if counter == 121:
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
def timer_60_libre():


    pygame.init()

    music(options())

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
            pygame.draw.circle(screen, (34,50,100), (480, 200), 70, 0)  #circulo azul
            pygame.draw.circle(screen,(247,224,159),(480,200),60, 0)    #circulo blanco
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

    music(options())

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
def timer_60_easy(base):
    pygame.init()

    music(base)


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
                    return #este return vuelve a la funcion mode_easy




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
    pygame.mixer.music.stop() #para la musica que este sonando, por si acaso se exede del tiempo

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_back_image = load_image('data/button_back.png')
    buttonpressed_back_image = load_image('data/button_back_pressed.png')

    buttonpressed_start_image = load_image('data/button start_pressed.png')
    button_start_image = load_image('data/button_start.png')

    fuente_texto_mode = pygame.font.SysFont("Swis721 Blk BT", 53, True)
    segundos_60 = fuente_texto_mode.render("60 segundos", 0, (84, 83, 83), (157, 156, 156))
    segundos_120 = fuente_texto_mode.render("120 segundos", 0, (84, 83, 83), (157, 156, 156))
    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)


        screen.blit(background_image, (0, 0))
        screen.blit(button_back_image, (50, 330))
        screen.blit(button_start_image,(50,160)) #start de 60 seg
        screen.blit(button_start_image,(530,160)) #start de 120 seg
        pygame.draw.rect(screen, (157, 156, 156), [140, 160, 300, 80], 0)
        screen.blit(segundos_60, (150, 180))
        pygame.draw.rect(screen, (157, 156, 156), [620, 160, 300, 80], 0)
        screen.blit(segundos_120, (630, 180))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (50, 160))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    timer_60_libre()
                    



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (455, 205))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    timer_120_libre()
                                


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_back_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    return  #retorna a la funcion mode_election

        pygame.display.flip()
#--------------------------------------------------
def mode_medio():
    pygame.mixer.music.stop() #para la musica que este sonando, por si acaso se exede del tiempo

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_back_image = load_image('data/button_back.png')
    buttonpressed_back_image = load_image('data/button_back_pressed.png')

    buttonpressed_start_image = load_image('data/button start_pressed.png')
    button_start_image = load_image('data/button_start.png')

    fuente_texto_mode = pygame.font.SysFont("Swis721 Blk BT", 53, True)
    segundos_60 = fuente_texto_mode.render("60 segundos", 0, (84, 83, 83), (157, 156, 156))
    segundos_120 = fuente_texto_mode.render("120 segundos", 0, (84, 83, 83), (157, 156, 156))
    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)


        screen.blit(background_image, (0, 0))
        screen.blit(button_back_image, (50, 330))
        screen.blit(button_start_image,(50,160)) #start de 60 seg
        screen.blit(button_start_image,(530,160)) #start de 120 seg
        pygame.draw.rect(screen, (157, 156, 156), [140, 160, 300, 80], 0)
        screen.blit(segundos_60, (150, 180))
        pygame.draw.rect(screen, (157, 156, 156), [620, 160, 300, 80], 0)
        screen.blit(segundos_120, (630, 180))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (50, 160))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    timer_60_medio()
                    



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (455, 205))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    timer_120_medio()
                                


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_back_image, (50, 330))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    return   #este return vuelve a la funcion mode_election

        pygame.display.flip()
#--------------------------------------------------
def mode_easy():

    pygame.mixer.music.stop() #para la musica que este sonando, por si acaso se exede del tiempo

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')

    button_back_image = load_image('data/button_back.png')
    buttonpressed_back_image = load_image('data/button_back_pressed.png')

    buttonpressed_start_image = load_image('data/button start_pressed.png')
    button_start_image = load_image('data/button_start.png')

    fuente_texto_mode = pygame.font.SysFont("Swis721 Blk BT", 53, True)
    segundos_60 = fuente_texto_mode.render("60 segundos", 0, (84, 83, 83), (157, 156, 156))
    segundos_120 = fuente_texto_mode.render("120 segundos", 0, (84, 83, 83), (157, 156, 156))
    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)


        screen.blit(background_image, (0, 0))
        screen.blit(button_back_image, (50, 330))
        screen.blit(button_start_image,(50,160)) #start de 60 seg
        screen.blit(button_start_image,(530,160)) #start de 120 seg
        pygame.draw.rect(screen, (157, 156, 156), [140, 160, 300, 80], 0)
        screen.blit(segundos_60, (150, 180))
        pygame.draw.rect(screen, (157, 156, 156), [620, 160, 300, 80], 0)
        screen.blit(segundos_120, (630, 180))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (50, 160))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_60
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 130 and 160 < objetivo[1] < 240:
                    return '60'



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # apreto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    screen.blit(buttonpressed_start_image, (530, 160))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto start_120
            if eventos.button == 1:
                objetivo = eventos.pos
                if 530 < objetivo[0] < 610 and 160 < objetivo[1] < 240:
                    return '120'           


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de back cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    screen.blit(buttonpressed_back_image, (50, 330))
                    

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar vuelve al mode_election
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 250 and 330 < objetivo[1] < 430:
                    return   'back'

        pygame.display.flip()
#--------------------------------------------------
def reco_palabras(ruta):
    #funcion que recopila y guarda las palabras
    archivo_palabras = open(ruta, 'r', encoding='UTF8')
    palabras = archivo_palabras.read().splitlines()
    archivo_palabras.close()
    return (palabras)
#--------------------------------------------------
def options():
    #es la ventana en donde se abre el popup de track_election
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')




    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 45, True)
    Track_selection = fuente_texto.render("Track Selection", 0, (84, 83, 83),(157,156,156))
    Track_selection_pressed = fuente_texto.render("Track Selection", 0, (157, 156, 156), (84, 83, 83))




    while True:

        for eventos in pygame.event.get():


            if eventos.type == QUIT:
                 sys.exit(0)

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (157, 156, 156), [50, 53, 300, 50], 0)
        screen.blit(Track_selection,(60,63))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de track selection cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 53 < objetivo[1] < 103:
                    pygame.draw.rect(screen,(84, 83, 83), [50, 53, 300, 50], 0)
                    screen.blit(Track_selection_pressed, (60, 63))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar salen las opciones
            if eventos.button == 1:
                objetivo = eventos.pos
                if 50 < objetivo[0] < 350 and 53 < objetivo[1] < 103:
                    return 


        pygame.display.flip()
#--------------------------------------------------
def track_selection():
    #es el menu popup donde se eligen la base
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("freestyle")
    background_image = load_image('data/fondo.png')
    icono_auriculares = load_image('data/previsualizer_music_icon.png')
    icono_auriculares_pressed = load_image('data/previsualizer_music_icon_pressed.png')

    fuente_texto = pygame.font.SysFont("Swis721 Blk BT", 45, True)
    Track_selection = fuente_texto.render("Track Selection", 0, (84, 83, 83), (157, 156, 156))
    base_rap_0 = fuente_texto.render("Beat default", 0, (84, 83, 83), (157, 156, 156))
    base_rap_0_pressed = fuente_texto.render("Beat default", 0, (157, 156, 156), (84, 83, 83))
    base_rap_1 = fuente_texto.render("No Soul -90s OldSchool", 0, (84, 83, 83), (157, 156, 156))
    base_rap_1_pressed = fuente_texto.render("No Soul -90s OldSchool", 0, (157, 156, 156), (84, 83, 83))
    base_rap_2 = fuente_texto.render("Base de rap FreeStyle ", 0, (84, 83, 83), (157, 156, 156))
    base_rap_2_pressed = fuente_texto.render("Base de rap FreeStyle ", 0, (157, 156, 156), (84, 83, 83))
    base_rap_4 = fuente_texto.render("Beat 4", 0, (84, 83, 83), (157, 156, 156))
    base_rap_4_pressed = fuente_texto.render("Beat 4", 0, (157, 156, 156), (84, 83, 83))



    while True:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (157, 156, 156), [50, 53, 300, 50], 0)
        pygame.draw.rect(screen, (157, 156, 156), [355, 53, 500, 377], 0)
        screen.blit(Track_selection, (60, 63))
        pygame.draw.rect(screen, (84, 83, 83), [355, 53, 500, 3], 0) #linea separatoria horizontal
        screen.blit(base_rap_0, (363, 63))
        pygame.draw.rect(screen, (84, 83, 83), [355, 103, 500, 3], 0) #linea separatoria horizontal
        screen.blit(base_rap_1, (363, 114))
        pygame.draw.rect(screen, (84, 83, 83), [355, 153, 500, 3], 0) #linea separatoria horizontal
        screen.blit(base_rap_2, (363, 164))
        pygame.draw.rect(screen, (84, 83, 83), [355, 203, 500, 3], 0) #linea separatoria horizontal 
        screen.blit(base_rap_4, (363, 214))
        pygame.draw.rect(screen, (84, 83, 83), [355, 253, 500, 3], 0) #linea separatoria horizontal
        screen.blit(base_rap_1, (363, 264)) #base pendiente
        pygame.draw.rect(screen, (84, 83, 83), [355, 303, 500, 3], 0) #linea separatoria horizontal
        screen.blit(base_rap_2, (363, 314)) #base pendiente
        pygame.draw.rect(screen, (84, 83, 83), [355, 353, 500, 3], 0) #linea separatoria horizontal

        pygame.draw.rect(screen, (84, 83, 83), [355, 430, 500, 3], 0) #linea separatoria horizontal
        pygame.draw.rect(screen, (84, 83, 83), [355, 53, 3, 377], 0) #linea vertical de recuadro izquierdo
        pygame.draw.rect(screen, (84, 83, 83), [852, 53, 3, 377], 0) #linea vertical de recuadro derecho



        
        screen.blit(icono_auriculares, (860, 53))
        pygame.draw.rect(screen, (84, 83, 83), [860, 53, 51, 3], 0) #linea recuadro auricular
        screen.blit(icono_auriculares, (860, 103))
        pygame.draw.rect(screen, (84, 83, 83), [860, 103, 51, 3], 0) #linea recuadro auricular
        screen.blit(icono_auriculares, (860, 153))
        pygame.draw.rect(screen, (84, 83, 83), [860, 153, 51, 3], 0) #linea recuadro auricular
        screen.blit(icono_auriculares, (860, 203))
        pygame.draw.rect(screen, (84, 83, 83), [860, 203, 51, 3], 0) #linea recuadro auricular
        screen.blit(icono_auriculares, (860, 253))
        pygame.draw.rect(screen, (84, 83, 83), [860, 253, 51, 3], 0) #linea recuadro auricular
        screen.blit(icono_auriculares, (860, 303))
        pygame.draw.rect(screen, (84, 83, 83), [860, 303, 51, 3], 0) #linea recuadro auricular
        pygame.draw.rect(screen, (84, 83, 83), [860, 353, 51, 3], 0) #linea recuadro auricular
        pygame.draw.rect(screen, (84, 83, 83), [860, 53, 3, 303], 0) #linea de recuadro izquierdo
        pygame.draw.rect(screen, (84, 83, 83), [910, 53, 3, 303], 0) #linea de recuadro derecho


        screen.blit(icono_auriculares, (860, 367))
        pygame.draw.rect(screen, (84, 83, 83), [860, 367, 51, 3], 0) #linea recuadro auricular
        pygame.draw.rect(screen, (84, 83, 83), [860, 417, 51, 3], 0) #linea recuadro auricular
        pygame.draw.rect(screen, (84, 83, 83), [860, 367, 3, 50], 0) #linea de recuadro izquierdo
        pygame.draw.rect(screen, (84, 83, 83), [910, 367, 3, 50], 0) #linea de recuadro derecho
    



    
        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de auris cuando se presiona TECLA 1
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 53 < objetivo[1] < 103:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 53, 500, 50], 0)
                    screen.blit(base_rap_0_pressed, (355, 63)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 1
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 53 < objetivo[1] < 103:
                    return ('data/base_rap_0.mp3')



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 1
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 53 < objetivo[1] < 103:
                    screen.blit(icono_auriculares_pressed, (860,53)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 1
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 53 < objetivo[1] < 103:            
                    return 'PV_1'
                       


 


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de base_rap_1 cuando se presiona TECLA 2
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 103 < objetivo[1] < 153:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 103, 500, 50], 0)
                    screen.blit(base_rap_1_pressed, (355, 113))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 2
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 103 < objetivo[1] < 153:
                    return ('data/base_rap_1.mp3')



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 2
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 103 < objetivo[1] < 153:
                    screen.blit(icono_auriculares_pressed, (860,103)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 2
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 103 < objetivo[1] < 153:
                    return 'PV_2'



 


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de base_rap_2 cuando se presiona TECLA 3
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 153 < objetivo[1] < 203:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 153, 500, 50], 0)
                    screen.blit(base_rap_2_pressed, (355, 163))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 3
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 153 < objetivo[1] < 203:
                    return ('data/base_rap_2.mp3')



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 3
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 153 < objetivo[1] < 203:
                    screen.blit(icono_auriculares_pressed, (860,153)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 3
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 153 < objetivo[1] < 203:
                      return 'PV_3'
                    





        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de base_rap_2 cuando se presiona TECLA 4
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 203 < objetivo[1] < 253:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 203, 500, 50], 0)
                    screen.blit(base_rap_4_pressed, (355, 213))


        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 4
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 203 < objetivo[1] < 253:
                    return ('data/base_rap_3.mp3')
        


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 4
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 203 < objetivo[1] < 253:
                    screen.blit(icono_auriculares_pressed, (860,203)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 4
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 203 < objetivo[1] < 253:
                    return 'PV_4'




        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de base_rap_2 cuando se presiona TECLA 5
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 253 < objetivo[1] < 303:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 203, 500, 50], 0)
                    screen.blit(base_rap_4_pressed, (355, 213)) #CAMBIAR POR NOMBRE DE BASE 5 PRESIONADA


        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 5
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 253 < objetivo[1] < 303:
                    return ('data/base_rap_4.mp3')
        


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 5
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 253 < objetivo[1] < 303:
                    screen.blit(icono_auriculares_pressed, (860,253)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 5
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 253 < objetivo[1] < 303:
                    return 'PV_5'



        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de base_rap_2 cuando se presiona TECLA 6
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 303 < objetivo[1] < 353:
                    pygame.draw.rect(screen, (84, 83, 83), [355, 203, 500, 50], 0)
                    screen.blit(base_rap_4_pressed, (355, 213)) #CAMBIAR POR NOMBRE DE BASE 6 PRESIONADA


        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar guarda la opcion elegida TECLA 6
            if eventos.button == 1:
                objetivo = eventos.pos
                if 353 < objetivo[0] < 857 and 303 < objetivo[1] < 353:
                    return ('data/base_rap_5.mp3')
        


        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color del audio_previsualizaer TECLA 6
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 303 < objetivo[1] < 353:
                    screen.blit(icono_auriculares_pressed, (860,303)) 
                    
        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se suelta audio_previsualizaer TECLA 6
            if eventos.button == 1:
                objetivo = eventos.pos
                if 860 < objetivo[0] < 910 and 303 < objetivo[1] < 353:
                    return 'PV_6'


        pygame.display.flip()
# --------------------------------------------------
def mode_election():
    #se elige el modo de juego, o si se desea salir del mismo

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("freestyle")

    background_image = load_image('data/fondo.png')

    buttonpressed_easy_image = load_image('data/buttonpressed_easy.png')
    button_easy_image = load_image('data/button_easy.png')

    buttonpressed_medio_image = load_image('data/buttonpressed_medio.png')
    button_medio_image = load_image('data/button_medio.png')


    buttonpressed_libre_image = load_image('data/buttonpressed_libre.png')
    button_libre_image = load_image('data/button_libre.png')



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
        screen.blit(button_easy_image, (100, 30))
        screen.blit(button_medio_image,(385, 30))
        screen.blit(button_libre_image,(670,30))
        screen.blit(button_exit_image, (330, 350))



        if eventos.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
            objetivo = pygame.mouse.get_pos()
            if 100 < objetivo[0] < 300 and 30 < objetivo[1] < 130:
                pygame.draw.rect(screen, (157, 156, 156), (210, 220, 500, 75), 0)
                screen.blit(definition_easy, (255, 225))
                screen.blit(definition_easy_2, (215, 255))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # presiono easy se muestra el boton presionado
            if eventos.button == 1:
                objetivo = eventos.pos
                if 100 < objetivo[0] < 300 and 30 < objetivo[1] < 130:
                    screen.blit(buttonpressed_easy_image, (100, 30))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando suelto el boton easy entra en su modo
            if eventos.button == 1:
                objetivo = eventos.pos
                if 100 < objetivo[0] < 300 and 30 < objetivo[1] < 130:
                    return('easy')


        if eventos.type == pygame.MOUSEMOTION:  #cuando paso por encima de medio muestra la desc
                objetivo = pygame.mouse.get_pos()
                if 385 < objetivo[0] < 585 and 30 < objetivo[1] < 130:
                    pygame.draw.rect(screen, (157, 156, 156),(210, 220, 500, 75), 0)
                    screen.blit(definition_medio, (255, 225))
                    screen.blit(definition_medio_2, (215, 255))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  #cuando presiono medio se ve el boton presionado
            if eventos.button == 1:
                objetivo = eventos.pos
                if 358 < objetivo[0] < 585 and 30 < objetivo[1] < 130:
                    screen.blit(buttonpressed_medio_image, (385, 30))

        if eventos.type == pygame.MOUSEBUTTONUP:  #cuando suelto el boton de medio entra en el modo del mismo
            if eventos.button == 1:
                objetivo = eventos.pos
                if 385 < objetivo[0] < 585 and 30 < objetivo[1] < 130:
                    return('medio')


        if eventos.type == pygame.MOUSEMOTION:  # paso por encima de libre muestra la desc
            objetivo = pygame.mouse.get_pos()
            if 670 < objetivo[0] < 870 and 30 < objetivo[1] < 130:
                pygame.draw.rect(screen, (157, 156, 156),(210, 220, 500, 75), 0)
                screen.blit(definition_libre, (255, 225))
                screen.blit(definition_libre_2, (215, 255))

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cuando apreto libre aparece presionado
            if eventos.button == 1:
                objetivo = eventos.pos
                if 670 < objetivo[0] < 870 and 30 < objetivo[1] < 130:
                     screen.blit(buttonpressed_libre_image, (670, 30))

        if eventos.type == pygame.MOUSEBUTTONUP:  # suelto libre entra al modo de juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 670 < objetivo[0] < 870 and 30 < objetivo[1] < 130:
                    return('libre')

        if eventos.type == pygame.MOUSEBUTTONDOWN:  # cambia el color de exit cuando se presiona
            if eventos.button == 1:
                objetivo = eventos.pos
                if 330 < objetivo[0] < 630 and 350 < objetivo[1] < 450:
                    screen.blit(buttonpressed_exit_image, (330, 350))

        if eventos.type == pygame.MOUSEBUTTONUP:  # cuando se deja de presionar sale del juego
            if eventos.button == 1:
                objetivo = eventos.pos
                if 330 < objetivo[0] < 630 and 350 < objetivo[1] < 450:
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
    while True:
        mode = mode_election()


        if mode == 'easy':
            while True:    
                easy = mode_easy()

                if easy == 'back': #si preciona la opcion de back 
                    break
                
                options()
                
                if easy == '60': #si preciona la opcion de 60 
                    while True:
                       
                          #entra en track selection
                        base = track_selection()
                        
                        if base == 'PV_1': #si preciona Previsualization 1
                            previsualization_music('data/base_rap_0.mp3')
                        if base == 'PV_2': #si preciona Previsualization 2
                            previsualization_music('data/base_rap_1.mp3')   
                        if base == 'PV_3': #si preciona Previsualization 3
                            previsualization_music('data/base_rap_2.mp3')
                        if base == 'PV_4': #si preciona Previsualization 2
                            previsualization_music('data/base_rap_3.mp3')   
                        if base == 'PV_5': #si preciona Previsualization 3
                            previsualization_music('data/base_rap_4.mp3')    
                        if base == 'PV_6': #si preciona Previsualization 3
                            previsualization_music('data/base_rap_5.mp3')   
                        #falta la del usuario       


                        if base != 'PV_1' and base != 'PV_2' and base != 'PV_3'and base != 'PV_4' and base != 'PV_5'and base != 'PV_6' and base != 'PV_7':
                            timer_60_easy(base) #cuando hay una base pone el beat y salen las plabras 
                            break

                if easy == '120': #si preciona la opcion de 1200 
                    timer_120_easy()

                


        if mode == 'medio':
            mode_medio()


        if mode == 'libre':    
            mode_libre()

    return 0
#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()

