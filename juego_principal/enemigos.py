import pygame as pg

pg.init()

class Enemigo(pg.sprite.Sprite):
    def __init__ (self,imagen_quieto,imagen_enemigo,imagen_muerte, x, y):
        pg.sprite.Sprite.__init__(self)
        self.animacion_enemigo = imagen_enemigo
        self.animacion_muerte = imagen_muerte
        self.image = imagen_quieto
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.index = 0
        self.vida = 100
        self.vivo = True
        
    def update(self):
        if self.index >= 7:
            self.index = 0
        self.image = self.animacion_enemigo[self.index]
        self.index +=1
        if self.vida <= 0 :
            self.image = self.animacion_muerte[self.index]
            self.index +=1 
            self.vida = 0
            self.vivo = False
            
    def draw(self,interfaz):
        interfaz.blit(self.image,self.rect)

        