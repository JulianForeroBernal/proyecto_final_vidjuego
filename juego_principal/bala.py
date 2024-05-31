import pygame as pg
import constantes as cons
pg.init()

class Bala(pg.sprite.Sprite):
    def __init__ (self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        imagen_original = image
        self.image = imagen_original
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.delta_x = cons.VELOCIDAD_BALA
        
    def update(self):
        self.rect.x += self.delta_x
        if self.rect.left > cons.ANCHO:
            self.kill()
            
        
    def drawing(self,internfaz):
        internfaz.blit(self.image,self.rect.centerx,self.rect.centery)
    
