import pygame as pg
import sys
import constantes as cons
from personaje import Personaje
from arma import Arma
from enemigos import Enemigo


pg.init() #inicializador de pygame
ventana = pg.display.set_mode((cons.ANCHO,cons.ALTO))
fondo = pg.image.load("imagenes/ambiente/mapa.jpg")
fondo = pg.transform.scale(fondo.convert(),(cons.ANCHO,cons.ALTO))
pg.display.set_caption("DOCE PODEROSOS FPS")
#DECLARACION DE VARIABLES PREVIAS AL CICLO
clock = pg.time.Clock()
jugador = Personaje((40,550))  #instancia personaje
#instansia arma
imagen_arma = pg.image.load("imagenes/jugador/arma.png")
imagen_arma= pg.transform.scale(imagen_arma,(imagen_arma.get_width()*0.7, imagen_arma.get_height()*0.7))
imagen_bala = pg.image.load("imagenes/jugador/bala.png")
arma = Arma(imagen_arma,imagen_bala) 
#instancias bala
grupo_sprites = pg.sprite.Group()
grupo_sprites.add(jugador)
#inicializaciones enemigos
imagen_enemigo = pg.image.load("imagenes/enemigos/negro_chiquito_1.png")
imagen_enemigo = pg.transform.scale(imagen_enemigo,(imagen_enemigo.get_width()*2.5, imagen_enemigo.get_height()*2.5))
enemigo = Enemigo(imagen_enemigo,1000,220)



run = True




while run:
    clock.tick(cons.FPS) 
    ventana.fill(cons.NEGRO)
    ventana.blit(fondo,(0,0))
    pg.display.update()
    grupo_sprites.draw(ventana)
    grupo_sprites.update()
    #dibujar el arma
    arma.draw(ventana)
    bala = arma.update(jugador)
    if bala:
        grupo_sprites.add(bala)
    #dibujar enemigo
    enemigo.draw(ventana)
    pg.display.flip()
    key = pg.key.get_pressed()
    jugador.control_tecla(key)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
            
            
            
            
            
            
            
            
            
pg.quit()
sys.exit()