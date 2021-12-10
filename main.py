from io import StringIO
import sys, pygame
from pygame.locals import *
from random import randint

# -*- coding: utf-8 -*-


WIDTH = 960
HEIGHT = 570

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Freestyle')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
font = pygame.font.SysFont(None, 40)









#--------------------------------------------------
def music(path):
    pygame.mixer.music.load(path)

    if (path == 'data/base_rap_1.mp3'):
        pygame.mixer.music.play(loops=0, start=9.0)

    if (path != 'data/base_rap_0.mp3'):
        pygame.mixer.music.play(loops=0, start=10.0)

    if (path == 'data/base_rap_0.mp3'):
        pygame.mixer.music.play()

    return
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
                    return 

        else:            
            clock.tick(60)
            continue
        break   
#--------------------------------------------------
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#--------------------------------------------------
def selector_de_niveles():
    click = False
    definition1 = False
    definition2 = False
    definition3 = False

    while True:
 
        
        background_image = load_image('data/fondo_rojo.png')
        screen.blit(background_image,(0,0))

        mx, my = pygame.mouse.get_pos() 

        exit_game_box  = pygame.Rect(605, 55, 200, 50)
        exit_game_border = pygame.Rect(600, 50, 210, 60)

        description_box  = pygame.Rect(405, 205, 400, 250)
        description_border = pygame.Rect(400, 200, 410, 260)

        title_box = pygame.Rect(105, 55, 200, 50)
        title_border = pygame.Rect(100, 50, 210, 60)

        button_1 = pygame.Rect(105, 205, 200, 50)
        button_border_1 = pygame.Rect(100, 200, 210, 60)

        button_2 = pygame.Rect(105, 305, 200, 50)
        button_border_2 = pygame.Rect(100, 300, 210, 60)

        button_3 = pygame.Rect(105, 405, 200, 50)
        button_border_3 = pygame.Rect(100, 400, 210, 60)

        if button_1.collidepoint((mx, my)):
            if click:
                return("easy")

        if button_2.collidepoint((mx, my)):
            if click:
                return("hard")

        if button_3.collidepoint((mx, my)):
            if click:
                return("xtreme")

        if exit_game_box.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()  


        pygame.draw.rect(screen, (247, 236, 191), exit_game_border) 
        pygame.draw.rect(screen, (32, 51, 73), exit_game_box)
        draw_text('EXIT GAME', font, (247, 236, 191), screen, 625, 65)

        pygame.draw.rect(screen, (247, 236, 191), description_border) 
        pygame.draw.rect(screen, (32, 51, 73), description_box)

        pygame.draw.rect(screen, (247, 236, 191), title_border) 
        pygame.draw.rect(screen, (32, 51, 73), title_box)
        draw_text('NIVELES', font, (247, 236, 191), screen, 145, 65)

        pygame.draw.rect(screen, (247, 236, 191), button_border_1) 
        pygame.draw.rect(screen, (32, 51, 73), button_1)
        draw_text('EASY', font, (247, 236, 191), screen, 165, 215)

        pygame.draw.rect(screen, (247, 236, 191), button_border_2) 
        pygame.draw.rect(screen, (32, 51, 73), button_2)
        draw_text('HARD', font, (247, 236, 191), screen, 160, 315)

        pygame.draw.rect(screen, (247, 236, 191), button_border_3) 
        pygame.draw.rect(screen, (32, 51, 73), button_3)
        draw_text('XTREME', font, (247, 236, 191), screen, 150, 415)


        if definition1:
            pygame.draw.rect(screen, (32, 51, 73), description_box)
            draw_text('Palabras cada 10 segundos', font, (247, 236, 191), screen, 420, 220)
        

        if definition2:
            pygame.draw.rect(screen, (32, 51, 73), description_box)
            draw_text('Palabras cada 5 segundos', font, (247, 236, 191), screen, 420, 220)


        if definition3:
            pygame.draw.rect(screen, (32, 51, 73), description_box)
            draw_text('Palabras cada 3 segundos', font, (247, 236, 191), screen, 420, 220)



        click = False
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()    

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


            if event.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
                objetivo = pygame.mouse.get_pos()
                if 105 < objetivo[0] < 305 and 200 < objetivo[1] < 250:
                    definition1 = True  
                else:
                    definition1 = False


            if event.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
                objetivo = pygame.mouse.get_pos()
                if 105 < objetivo[0] < 305 and 300 < objetivo[1] < 350:
                    definition2 = True  
                else:
                    definition2 = False  


            if event.type == pygame.MOUSEMOTION:  # cuando paso por encima de easy muestra la desc
                objetivo = pygame.mouse.get_pos()
                if 105 < objetivo[0] < 305 and 400 < objetivo[1] < 450:
                    definition3 = True  
                else:
                    definition3 = False  
 
        pygame.display.update()
        mainClock.tick(60)
#--------------------------------------------------
def juego(tiempo_palabras):

    

    word_box = pygame.Rect(170, 390, 620, 90)
    word_box_border = pygame.Rect(160, 380, 640, 110)

    background_image = load_image('data/fondo_rojo.png')
    screen.blit(background_image,(0,0))

    clock = pygame.time.Clock()

    counter, text = 61, '61'.rjust(3)

    pygame.time.set_timer(pygame.USEREVENT, 1000)

    font = pygame.font.SysFont("Swis721 Blk BT", 100, True)
    font_timer = pygame.font.SysFont("Swis721 Blk BT", 200, True)

    palabras = reco_palabras('data/palabras.txt')

    palabras_text = 'YA ARRANCA'
    
    x_centrada = 250

    base = track_selection()

    if base != 'libre':
        music(base)

    tiempo = True

    while True:

        
        screen.blit(background_image, (0, 0))


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)


            if counter % tiempo_palabras == 1:
                rannum = randint(0, 1212)

            if e.type == pygame.USEREVENT and tiempo == True:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0:
                    tiempo = False
     
            if counter % tiempo_palabras == 0:
                x_centrada = 480 - (((len(palabras[rannum])) / 2) * 40)
                palabras_text = palabras[rannum].capitalize()




        else:
            
            if counter > 0:
                pygame.draw.circle(screen, (247, 236, 191), (480, 230), 130, 0)
                pygame.draw.circle(screen,(32, 51, 73),(480,230),120, 0)

                pygame.draw.rect(screen, (247, 236, 191), word_box_border)
                pygame.draw.rect(screen, (32, 51, 73), word_box)

                pygame.draw.polygon(screen,(247, 236, 191), points=[(160,380), (160,489), (100,380)]) #triangulo blanco izq
                pygame.draw.polygon(screen,(32, 51, 73), points=[(170,390), (170,480), (120,390)]) #triangulo azul izq

                pygame.draw.polygon(screen,(247, 236, 191), points=[(800,380), (800,489), (860,489)]) #triangulo blanco izq
                pygame.draw.polygon(screen,(32, 51, 73), points=[(790,390), (790,479), (840,479)]) #triangulo azul izq

                draw_text(palabras_text, font, (247, 236, 191), screen, x_centrada, 400)
                screen.blit(font_timer.render(text, True, (247, 236, 191)), (337, 170)) #numeros del contador






            if counter == 0:
                return



            
            pygame.display.flip()
            clock.tick(60)
            continue
        break
#--------------------------------------------------
def pantalla_back():
    click = False
    font = pygame.font.SysFont("Swis721 Blk BT", 100, True)

    word_box = pygame.Rect(170, 390, 620, 90)
    word_box_border = pygame.Rect(160, 380, 640, 110)

    button_exit =  pygame.Rect(395, 145, 168, 168)

    while True:
 
        
        background_image = load_image('data/fondo_rojo.png')
        screen.blit(background_image,(0,0))

        mx, my = pygame.mouse.get_pos() 


        if button_exit.collidepoint((mx, my)):
            if click:
                return

        


        pygame.draw.circle(screen, (247, 236, 191), (480, 230), 130, 0)
        pygame.draw.circle(screen,(32, 51, 73),(480,230),120, 0)
        pygame.draw.rect(screen, (32, 51, 73), button_exit)
        draw_text('BACK', font, (247, 236, 191), screen, 365, 200)

       

        click = False
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()    

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
#--------------------------------------------------
def track_selection():

    BUTTON_WIDTH = 350
    BORDER_WIDTH = BUTTON_WIDTH + 10

    BUTTON_HEIGHT = 50
    BORDER_HEIGHT = BUTTON_HEIGHT + 10


    COLUMNA_N1 = 50

    COLUMNA_N2 = 500

    click = False

    while True:
        
        
        PV_IMG = load_image('data/previsualizer_music_icon.png')
        


        background_image = load_image('data/fondo_rojo.png')
        screen.blit(background_image,(0,0))

        mx, my = pygame.mouse.get_pos() 

        

        Track_selection = pygame.Rect(COLUMNA_N1, 30, BUTTON_WIDTH, BUTTON_HEIGHT)
        Track_selection_border = pygame.Rect(COLUMNA_N1 - 5, 25, BORDER_WIDTH, BORDER_HEIGHT)

        #primer columna
        button_1 = pygame.Rect(COLUMNA_N1, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_1 = pygame.Rect(COLUMNA_N1 - 5, 115, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_1 = pygame.Rect(BUTTON_WIDTH+65, 115, 60, 60)


        button_2 = pygame.Rect(COLUMNA_N1, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_2 = pygame.Rect(COLUMNA_N1 - 5, 195, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_2 = pygame.Rect(BUTTON_WIDTH+65, 195, 60, 60)

        button_3 = pygame.Rect(COLUMNA_N1, 280, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_3 = pygame.Rect(COLUMNA_N1 - 5, 275, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_3 = pygame.Rect(BUTTON_WIDTH+65, 275, 60, 60)


        button_4 = pygame.Rect(COLUMNA_N1, 360, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_4 = pygame.Rect(COLUMNA_N1 - 5, 355, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_4 = pygame.Rect(BUTTON_WIDTH+65, 355, 60, 60)

        #segundo columna
        
        button_5 = pygame.Rect(COLUMNA_N2 , 120, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_5 = pygame.Rect(COLUMNA_N2  - 5, 115, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_5 = pygame.Rect(COLUMNA_N2 + BUTTON_WIDTH + 15, 115, 60, 60)

        button_6 = pygame.Rect(COLUMNA_N2 , 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_6 = pygame.Rect(COLUMNA_N2  - 5, 195, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_6 = pygame.Rect(COLUMNA_N2 + BUTTON_WIDTH + 15, 195, 60, 60)

        button_7 = pygame.Rect(COLUMNA_N2 , 280, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_7 = pygame.Rect(COLUMNA_N2  - 5, 275, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_7 = pygame.Rect(COLUMNA_N2 + BUTTON_WIDTH + 15, 275, 60, 60)

        button_8 = pygame.Rect(COLUMNA_N2 , 360, BUTTON_WIDTH, BUTTON_HEIGHT)
        button_border_8 = pygame.Rect(COLUMNA_N2  - 5, 355, BORDER_WIDTH, BORDER_HEIGHT)
        PV_border_8 = pygame.Rect(COLUMNA_N2 + BUTTON_WIDTH + 15, 355, 60, 60)


        



        if button_1.collidepoint((mx, my)):
            if click:
                return('data/base_rap_1.mp3')

        if PV_border_1.collidepoint((mx, my)):
            if click:
                previsualization_music('data/base_rap_1.mp3')


        if button_2.collidepoint((mx, my)):
            if click:
                return('data/base_rap_2.mp3')

        if PV_border_2.collidepoint((mx, my)):
            if click:
                previsualization_music('data/base_rap_2.mp3')


        if button_3.collidepoint((mx, my)):
            if click:
                return('data/base_rap_3.mp3')

        if PV_border_3.collidepoint((mx, my)):
            if click:
                previsualization_music('data/base_rap_3.mp3')


        if button_4.collidepoint((mx, my)):
            if click:
                return('data/base_rap_4.mp3')

        if PV_border_4.collidepoint((mx, my)):
            if click:
                previsualization_music('data/base_rap_4.mp3')



        if button_5.collidepoint((mx, my)):
            if click:
                return('libre')

        












        #primera columna 


       
        pygame.draw.rect(screen, (247, 236, 191), Track_selection_border) 
        pygame.draw.rect(screen, (32, 51, 73), Track_selection)
        draw_text('TRACK SELECTION', font, (247, 236, 191), screen, 60, 43)




        pygame.draw.rect(screen, (247, 236, 191), button_border_1) 
        pygame.draw.rect(screen, (32, 51, 73), button_1)
        draw_text('Base de freestyle n°1', font, (247, 236, 191), screen, 60, 133)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_1) 
        screen.blit(PV_IMG,(BUTTON_WIDTH+70,120))



 
        pygame.draw.rect(screen, (247, 236, 191), button_border_2) 
        pygame.draw.rect(screen, (32, 51, 73), button_2)
        draw_text('Base de freestyle n°2', font, (247, 236, 191), screen, 60, 213)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_2) 
        screen.blit(PV_IMG,(BUTTON_WIDTH+70,200))




        pygame.draw.rect(screen, (247, 236, 191), button_border_3) 
        pygame.draw.rect(screen, (32, 51, 73), button_3)
        draw_text('Base de freestyle n°3', font, (247, 236, 191), screen, 60, 293)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_3) 
        screen.blit(PV_IMG,(BUTTON_WIDTH+70,280))



 
        pygame.draw.rect(screen, (247, 236, 191), button_border_4) 
        pygame.draw.rect(screen, (32, 51, 73), button_4)
        draw_text('Base de freestyle n°4', font, (247, 236, 191), screen, 60, 373)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_4) 
        screen.blit(PV_IMG,(BUTTON_WIDTH+70,360))
        



        #segunda columna 

        pygame.draw.rect(screen, (247, 236, 191), button_border_5) 
        pygame.draw.rect(screen, (32, 51, 73), button_5)
        draw_text('Base de freestyle n°5', font, (247, 236, 191), screen, 510, 133)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_5) 
        screen.blit(PV_IMG,(800+70,120))


        pygame.draw.rect(screen, (247, 236, 191), button_border_6) 
        pygame.draw.rect(screen, (32, 51, 73), button_6)
        draw_text('Base de freestyle n°6', font, (247, 236, 191), screen, 510, 213)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_6) 
        screen.blit(PV_IMG,(800+70,200))




        pygame.draw.rect(screen, (247, 236, 191), button_border_7) 
        pygame.draw.rect(screen, (32, 51, 73), button_7)
        draw_text('Base de freestyle n°7', font, (247, 236, 191), screen, 510, 293)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_7) 
        screen.blit(PV_IMG,(800+70,280))



 
        pygame.draw.rect(screen, (247, 236, 191), button_border_8) 
        pygame.draw.rect(screen, (32, 51, 73), button_8)
        draw_text('SIN BASE', font, (247, 236, 191), screen, 510, 373)
        pygame.draw.rect(screen, (247, 236, 191), PV_border_8) 
        screen.blit(PV_IMG,(800+70,360))
        
        




        click = False
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
#--------------------------------------------------
def pantalla_inicio():

    click = False

    while True:
 
        
        background_image = load_image('data/fondo.png')
        screen.blit(background_image,(0,0))

        mx, my = pygame.mouse.get_pos() 
 
        button_1 = pygame.Rect(180, 480, 200, 50)
        button_border_1 = pygame.Rect(175, 475, 210, 60)

        button_2 = pygame.Rect(580, 480, 200, 50)
        button_border_2 = pygame.Rect(575, 475, 210, 60)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        if button_2.collidepoint((mx, my)):
            if click:
                return

       
        pygame.draw.rect(screen, (247, 236, 191), button_border_1) 
        pygame.draw.rect(screen, (32, 51, 73), button_1)
        draw_text('SALIR', font, (247, 236, 191), screen, 235, 490)

        pygame.draw.rect(screen, (247, 236, 191), button_border_2) 
        pygame.draw.rect(screen, (32, 51, 73), button_2)
        draw_text('JUGAR', font, (247, 236, 191), screen, 630, 490)


        click = False
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
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
def reco_palabras(ruta):
    #funcion que recopila las palabras de un txt y las devulve en una lista
    archivo_palabras = open(ruta, 'r', encoding='UTF8')
    palabras = archivo_palabras.read().splitlines()
    archivo_palabras.close()
    return (palabras)
#--------------------------------------------------
def main():
    pantalla_inicio() 
    
    nivel = 1

    while nivel != 0:

        nivel = selector_de_niveles()

        if(nivel == "easy"):
            juego(10)
            pantalla_back()
        
        if(nivel == "hard"):
            juego(5)
            pantalla_back()
        
        if(nivel == "xtreme"):
            juego(3)
            pantalla_back()
#--------------------------------------------------

        


#--------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()  

