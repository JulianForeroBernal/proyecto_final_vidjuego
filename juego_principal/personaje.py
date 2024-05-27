from typing import Any
import pygame as pg
import constantes as cons
pg.init()
#from pygame.sprite import _Group
#pg.display.set_mode((cons.ANCHO,cons.ALTO))
#INICIALIZACIONES NECESARIAS PARA EL PERSONAJE
sheet_dead = pg.image.load("imagenes/jugador/dead_90x90.png")#.convert_alpha()
sheet_runleft = pg.image.load("imagenes/jugador/run_left.png")#.convert_alpha()
sheet_reload_run_shoot = pg.image.load("imagenes/jugador/reload_run_shoot.png")#.convert_alpha()
animacion_quieto = pg.image.load("imagenes/jugador/idle.png")#.convert_alpha()
animacion_recarga = [] # listo
animacion_derecha = [] #listo
animacion_ataque = [] #listo
animacion_izquierda = [] #listo
animacion_muerte = [] #listo


#SE RECORTA UNO POR UNO CADA FRAME PARA LA ANIMACION DE DISPARO,CORRER, Y DISPARAR
for i in range(0,4):
    for j in range (0,4):
        animation1 = pg.Rect(90*i,90*j,90,90)
        if j == 0 :
            animacion_recarga.append(sheet_reload_run_shoot.subsurface(animation1))
        if j == 1 :
            animacion_derecha.append(sheet_reload_run_shoot.subsurface(animation1))
        if j == 2 :
            animacion_ataque.append(sheet_reload_run_shoot.subsurface(animation1))  

#SE RECRTA LAS IMAGENES DE LA ANIMACION DE CAMINAR A LA IZQUIERDA Y LA DE MUERTE Y SE ALMACENAN EN LAS LISTAS CORRESPONDIENTES                  
for k in range(0,4):
    animation2 = pg.Rect(90*k,0,90,90)
    animacion_izquierda.append(sheet_runleft.subsurface(animation2))
for l in range (0,4) : 
    animation3 = pg.Rect(90*l,0,90,90)
    
class Personaje(pg.sprite.Sprite):
    def __init__(self,posicion):
        pg.sprite.Sprite.__init__(self)
        self.animacion_recarga = animacion_recarga
        self.animacion_derecha = animacion_derecha
        self.animacion_ataque = animacion_ataque
        self.animacion_izquierda = animacion_izquierda
        self.animacion_muerte = animacion_muerte
        self.animacion_quieto = animacion_quieto
        self.image = self.animacion_quieto
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.index = 0
        self.direccion = ""
        self.recarga = False
        self.vida = 3
    def update(self) :
    
        if self.index >= 3:
            self.index = 0
        self.image = self.animacion_quieto
        
        if self.direccion == "derecha":
            self.image = self.animacion_derecha[self.index]
            self.index += 1
        if self.direccion == "izquierda":
            self.image = self.animacion_izquierda[self.index]
            self.index += 1
        if self.direccion == "arriba":
            self.image = self.animacion_derecha[self.index]
            self.index += 1
        if self.direccion == "abajo" : 
            self.image = self.animacion_derecha[self.index]
            self.index += 1
        if self.direccion == "ataque":
            self.image = self.animacion_ataque[self.index]
            self.index += 1
        if self.direccion == "stop" :
            self.image = self.animacion_quieto
            
            
        if self.recarga == True:
            self.image = self.animacion_recarga[self.index]
            self.index += 1
        if self.vida == 0 :
            self.image = self.animacion_muerte[self.index]
            self.index +=1
            
        
    def control_tecla(self, key):
        if key[pg.K_RIGHT]:
            self.rect.x += cons.VELOCIDAD
            self.direccion = "derecha"
        elif key[pg.K_LEFT]:
            self.rect.x -= cons.VELOCIDAD
            self.direccion = "izquierda"
        elif key[pg.K_UP]:
            self.rect.y -= cons.VELOCIDAD
            self.direccion = "arriba"
        elif key[pg.K_DOWN]:
            self.rect.y += cons.VELOCIDAD
            self.direccion = "abajo"
        elif key[pg.K_SPACE]:
            self.direccion = "ataque"
        else:
            if self.direccion == "derecha":
                self.direccion = "stop"
            if self.direccion == "izquierda":
                self.direccion = "stop"
            if self.direccion == "abajo":
                self.direccion = "stop"
            if self.direccion == "arriba":
                self.direccion = "stop"
            if self.direccion == "ataque":
                self.direccion = "stop"
                                       
        
        