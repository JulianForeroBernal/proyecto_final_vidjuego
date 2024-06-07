
import pygame as pg
pg.init()
pg.mixer.init()
sonido_puerta = pg.mixer.Sound("sonidos/door.wav")
class Puerta(pg.sprite.Sprite):
    def __init__(self,imagen_puerta,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = imagen_puerta
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self,jugador):
        if self.rect.colliderect(jugador.rect):
            if jugador.puntuacion < 100:
                jugador.rect.top = self.rect.bottom
            if jugador.puntuacion == 100:
                sonido_puerta.play()
                self.kill()