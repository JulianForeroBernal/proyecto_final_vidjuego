import pygame as pg
import constantes as cons
pg.init()
#from pygame.sprite import _Group
#pg.display.set_mode((cons.ANCHO,cons.ALTO))
#INICIALIZACIONES NECESARIAS PARA EL PERSONAJE
sheet_dead = pg.image.load("imagenes/jugador/Biker_death.png")#.convert_alpha()
sheet_dead = pg.transform.scale(sheet_dead,(sheet_dead.get_width()*cons.ESCALA_PLAYER,sheet_dead.get_height()*cons.ESCALA_PLAYER))
sheet_runleft = pg.image.load("imagenes/jugador/Biker_run_left.png")#.convert_alpha()
sheet_runleft = pg.transform.scale(sheet_runleft,(sheet_runleft.get_width()*cons.ESCALA_PLAYER,sheet_runleft.get_height()*cons.ESCALA_PLAYER))
sheet_run= pg.image.load("imagenes/jugador/Biker_run.png")#.convert_alpha()
sheet_run = pg.transform.scale(sheet_run,(sheet_run.get_width()*cons.ESCALA_PLAYER,sheet_run.get_height()*cons.ESCALA_PLAYER))
animacion_quieto = pg.image.load("imagenes/jugador/Biker_idle.png")#.convert_alpha()
animacion_quieto= pg.transform.scale(animacion_quieto,(animacion_quieto.get_width()*cons.ESCALA_PLAYER,animacion_quieto.get_height()*cons.ESCALA_PLAYER))
animacion_derecha = [] #listo
animacion_izquierda = [] #listo
animacion_muerte = [] #listo


#SE RECORTA UNO POR UNO CADA FRAME PARA LA ANIMACION DE DISPARO,CORRER, Y DISPARAR
for j in range(0,6):
    animation1 = pg.Rect(cons.PIXELES_FRAME*j,0,cons.PIXELES_FRAME,cons.PIXELES_FRAME)
    animacion_derecha.append(sheet_run.subsurface(animation1))


#SE RECRTA LAS IMAGENES DE LA ANIMACION DE CAMINAR A LA IZQUIERDA Y LA DE MUERTE Y SE ALMACENAN EN LAS LISTAS CORRESPONDIENTES                  
for k in range(0,6):
    animation2 = pg.Rect(cons.PIXELES_FRAME*k,0,cons.PIXELES_FRAME,cons.PIXELES_FRAME)
    animacion_izquierda.append(sheet_runleft.subsurface(animation2))
for l in range (0,6) : 
    animation3 = pg.Rect(cons.PIXELES_FRAME*l,0,cons.PIXELES_FRAME,cons.PIXELES_FRAME)
    
class Personaje(pg.sprite.Sprite):
    def __init__(self,posicion):
        pg.sprite.Sprite.__init__(self)
        self.animacion_derecha = animacion_derecha
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
        self.shape = pg.Rect(0,0,cons.PIXELES_FRAME,cons.PIXELES_FRAME)
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
        if self.direccion == "stop_izquierda" :
            self.image = pg.transform.flip(self.animacion_quieto,True,False)
            
            
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

        else:
            if self.direccion == "derecha":
                self.direccion = "stop"
            if self.direccion == "izquierda":
                self.direccion = "stop_izquierda"
            if self.direccion == "abajo":
                self.direccion = "stop"
            if self.direccion == "arriba":
                self.direccion = "stop"
            if self.direccion == "ataque":
                self.direccion = "stop"
                                 
        
        