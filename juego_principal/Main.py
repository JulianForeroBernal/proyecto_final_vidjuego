import pygame as pg
import sys
import constantes as cons
from personaje import Personaje

pg.init() #inicializador de pygame
ventana = pg.display.set_mode((cons.ANCHO,cons.ALTO))
pg.display.set_caption("ONCE PODEROSOS FPS")
#DECLARACION DE VARIABLES PREVIAS AL CICLO
clock = pg.time.Clock()
jugador = Personaje((0,200))  #instancia personaje
grupo_sprites = pg.sprite.Group()
grupo_sprites.add(jugador)



run = True




while run:
    clock.tick(cons.FPS) 
    ventana.fill(cons.NEGRO)
    pg.display.update()
    grupo_sprites.draw(ventana)
    grupo_sprites.update()
    pg.display.flip()
    
    key = pg.key.get_pressed()
    jugador.control_tecla(key)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
            
            
            
            
            
            
            
            
            
pg.quit()
sys.exit()