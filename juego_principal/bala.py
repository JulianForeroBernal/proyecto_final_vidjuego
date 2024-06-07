import pygame as pg
import constantes as cons
import random as rn

pg.init()
sonido_daño = pg.mixer.Sound("sonidos/hurt.wav")
class Bala(pg.sprite.Sprite):
    def __init__ (self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        imagen_original = image
        self.image = imagen_original
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.delta_x = cons.VELOCIDAD_BALA
        
        
    def update(self,lista_enemigos,jugador,lista_obstaculo):
        daño = 0
        pos_enemigo = None
        if jugador.direccion == "derecha" or jugador.direccion == "stop_derecha" or jugador.direccion == "arriba" or jugador.direccion == "abajo":
            self.rect.x += self.delta_x 
        if jugador.direccion == "izquierda" or jugador.direccion == "stop_izquierda":
            self.rect.x -= self.delta_x 
        if self.rect.left > cons.ANCHO :
            self.kill()
        if self.rect.left < 0 :
            self.kill()
        for enemigo in lista_enemigos :
            if enemigo.rect.colliderect(self.rect) and enemigo.vivo == True:
                sonido_daño.play()
                daño = 15 + rn.randint(5,15)
                enemigo.vida -= daño
                pos_enemigo = enemigo.rect
                self.kill()
                break
        for obstaculo in lista_obstaculo:
            if obstaculo[1].colliderect(self.rect):
                self.kill()
        return daño , pos_enemigo 
                  
        
    def draw(self,internfaz):
        internfaz.blit(self.image,self.rect.centerx,self.rect.centery)
    
