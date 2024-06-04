import pygame as pg
import constantes as cons
import random as rn

pg.init()

class Bala(pg.sprite.Sprite):
    def __init__ (self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        imagen_original = image
        self.image = imagen_original
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.delta_x = cons.VELOCIDAD_BALA
        
    def update(self,lista_enemigos):
        daño = 0
        pos_enemigo = None
        self.rect.x += self.delta_x
        if self.rect.left > cons.ANCHO:
            self.kill()
        for enemigo in lista_enemigos :
            if enemigo.rect.colliderect(self.rect):
                daño = 15 + rn.randint(5,15)
                enemigo.vida -= daño
                pos_enemigo = enemigo.rect
                self.kill()
                break
        return daño , pos_enemigo            
        
    def draw(self,internfaz):
        internfaz.blit(self.image,self.rect.centerx,self.rect.centery)
    
