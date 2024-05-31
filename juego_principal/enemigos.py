import pygame as pg
import constantes as cons
from bala import Bala
pg.init()

class Enemigo(pg.sprite.Sprite):
    def __init__ (self, imagen, x, y):
        pg.sprite.Sprite.__init__(self)
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.center = (x,y)
    def draw(self,interfaz):
        interfaz.blit(self.imagen,self.rect)
    def update(self):
        if self.rect.colliderect(Bala.rect):
            self.kill()
        