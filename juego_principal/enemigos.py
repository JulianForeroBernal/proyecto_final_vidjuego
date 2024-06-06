import pygame as pg
import constantes as cons

pg.init()

class Enemigo(pg.sprite.Sprite):
    def __init__ (self,imagen_quieto,imagen_enemigo,imagen_muerte,imagen_enemigo_ataque, x, y):
        pg.sprite.Sprite.__init__(self)
        self.animacion_enemigo = imagen_enemigo
        self.animacion_muerte = imagen_muerte
        self.animacion_enemigo_ataque = imagen_enemigo_ataque
        self.image = imagen_quieto
        self.update_time = pg.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.index = 0
        self.vida = 100
        self.vivo = True
        
    def update(self,jugador):
        if self.index >= 7:
            self.index = 0
        self.image = self.animacion_enemigo[self.index]
        if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
            self.index +=1
            self.update_time = pg.time.get_ticks()
        if self.vida <= 0 :
            self.image = self.animacion_muerte[self.index]
            self.index +=1 
            self.vida = 0
            self.vivo = False
        if jugador.rect.colliderect(self.rect) and self.vivo == True and jugador.vivo == True:
            if self.index >= 7:
                self.index = 0
            self.image = self.animacion_enemigo_ataque[self.index]
            jugador.vida -= 1
            if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
                self.index +=1
                self.update_time = pg.time.get_ticks()
                
            
            
            
    def draw(self,interfaz):
        interfaz.blit(self.image,self.rect)

        