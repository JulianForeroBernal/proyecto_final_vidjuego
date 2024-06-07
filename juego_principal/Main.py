import pygame as pg
import sys
import constantes as cons
from personaje import Personaje
from arma import Arma
from enemigos import Enemigo
from textos import TextoDaño
from items import Items
from mundo import Mundo
from puertas import Puerta

pg.init() #inicializador de pygame
pg.mixer.init()

#AJUSTES VENTANA 
ventana = pg.display.set_mode((cons.ANCHO,cons.ALTO))
pg.display.set_caption("JUEGO")

#FUNCION PARA DIBUJAR TEXTOS 
def dibujar_textos(texto,font,color,x,y):
    img = font.render(texto,True,color)
    ventana.blit(img,(x,y))

#FUNCION PARA DIBUJAR CUADRICULO 

def dibujar_cuadricula ():
    for x in range (30): 
        pg.draw.line( ventana, cons.BLANCO, (x*cons.TILE_SIZE, 0), (x*cons.TILE_SIZE, cons.ALTO))
        pg.draw.line (ventana, cons.BLANCO, (0, x*cons.TILE_SIZE), (cons.ANCHO, x*cons.TILE_SIZE)) 

#DECLARACION DE VARIABLES PARA CONTROL DEL CICLO
clock = pg.time.Clock() # variable reloj para el control de fps

#FUENTES
fuente_puntuacion = pg.font.Font("imagenes/fuentes/fuente.ttf", 35) 
fuente_daño = pg.font.Font("imagenes/fuentes/fuente.ttf", 20) 
fuente_nivel_2 = pg.font.Font("imagenes/fuentes/fuente.ttf", 60)
fuente_inico = pg.font.Font("imagenes/fuentes/fuente.ttf", 20)
funte_titulo = pg.font.Font("imagenes/fuentes/fuente.ttf", 75)
grupo_sprites_textos = pg.sprite.Group()

#BOTONES
boton_jugar = pg.Rect(cons.ANCHO/2 -100 , cons.ALTO/2 - 50,200,50)
boton_salir = pg.Rect(cons.ANCHO/2 -100 , cons.ALTO/2 + 50,200,50)

texto_boton_jugar = fuente_inico.render("jugar",True,cons.NEGRO)
texto_boton_salir = fuente_inico.render("salir",True,cons.NEGRO)

#imagenes corazones
corazon_lleno = pg.image.load("imagenes/jugador/items/corazon_lleno.png")
corazon_lleno = pg.transform.scale(corazon_lleno,(corazon_lleno.get_width()*cons.ESCALA_CORAZONES, corazon_lleno.get_height()*cons.ESCALA_CORAZONES))
corazon_vacio = pg.image.load("imagenes/jugador/items/corazon_vacio.png")
corazon_vacio = pg.transform.scale(corazon_vacio,(corazon_vacio.get_width()*cons.ESCALA_CORAZONES, corazon_vacio.get_height()*cons.ESCALA_CORAZONES))

#instancias jugador
jugador = Personaje((30,680))  #instancia personaje
grupo_sprites_player = pg.sprite.Group()
grupo_sprites_player.add(jugador)
def corazones_jugador():
    for i in range (0,4):
        if jugador.vida >= ((i+1)*25):
            ventana.blit(corazon_lleno,(20+i*45,25))
        elif jugador.vida % 25 > 0 :
            ventana.blit(corazon_vacio,(20+i*45,25))


#instansia arma
imagen_arma = pg.image.load("imagenes/jugador/arma.png")
imagen_arma= pg.transform.scale(imagen_arma,(imagen_arma.get_width()*0.5, imagen_arma.get_height()*0.5))
cont_seg = pg.time.Clock()
#instancias bala
imagen_bala = pg.image.load("imagenes/jugador/bala.png")
arma = Arma(imagen_arma,imagen_bala) 
grupo_sprites_balas = pg.sprite.Group()

#AJUSTES INICIALES ENEMIGOS
imagen_enemigo = []
imagen_enemigo_caminar = []
imagen_enemigo_muerte = []
imagen_enemigo_ataque = []
imagen_quieto_enemigo_1 = pg.image.load("imagenes/enemigos/negro_chiquito_1.png")
imagen_quieto_enemigo_1 = pg.transform.scale(imagen_quieto_enemigo_1,(imagen_quieto_enemigo_1.get_width()*2.5, imagen_quieto_enemigo_1.get_height()*2.5))
for i in range (0,8):
    aux_imagen = pg.image.load(f"imagenes/enemigos/negro_chiquito_{i+1}.png")
    aux_imagen = pg.transform.scale(aux_imagen,(aux_imagen.get_width()*2.5, aux_imagen.get_height()*2.5))
    imagen_enemigo.append(aux_imagen)
for j in range (0,8):
    aux_imagen_2 = pg.image.load(f"imagenes/enemigos/sheet_caminar_{j+1}.png")
    aux_imagen_2 = pg.transform.scale(aux_imagen_2,(aux_imagen_2.get_width()*2.5, aux_imagen_2.get_height()*2.5))
    imagen_enemigo_caminar.append(aux_imagen_2)
for k in range (0,8):
    aux_imagen_3 = pg.image.load(f"imagenes/enemigos/sheet_muerte_{i+1}.png")
    aux_imagen_3 = pg.transform.scale(aux_imagen_3,(aux_imagen_3.get_width()*2.5, aux_imagen_3.get_height()*2.5))
    imagen_enemigo_muerte.append(aux_imagen_3)
for l in range (0,8):
    aux_imagen_4 = pg.image.load(f"imagenes/enemigos/sheet_ataque_{l+1}.png")
    aux_imagen_4 = pg.transform.scale(aux_imagen_4,(aux_imagen_4.get_width()*2.5, aux_imagen_4.get_height()*2.5))
    imagen_enemigo_ataque.append(aux_imagen_4) 
enemigo = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,1024,248) #top-right
enemigo_2 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,1000,740) #down_right_2
enemigo_3 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,185,330) #top_left
enemigo_4 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,450,740) #1
enemigo_5 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,850,740) #2
enemigo_6 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar,930,248) #top-right
lista_enemigos = [enemigo,enemigo_2, enemigo_3, enemigo_4, enemigo_5, enemigo_6]
grupo_sprites_enemis = pg.sprite.Group()
grupo_sprites_enemis.add(enemigo)
grupo_sprites_enemis.add(enemigo_2)
grupo_sprites_enemis.add(enemigo_3)
grupo_sprites_enemis.add(enemigo_4)
grupo_sprites_enemis.add(enemigo_5)
grupo_sprites_enemis.add(enemigo_6)
#AJUTES INICIALELS ITEMS 
sheet_coin = pg.image.load("imagenes/jugador/items/coin_.png")
animacion_moneda = []
for i in range (0,11):
    animacion_aux = pg.Rect(cons.PIXELES_FRAME_MONEDA*i,0,cons.PIXELES_FRAME_MONEDA,cons.PIXELES_FRAME_MONEDA)
    animacion_moneda.append(sheet_coin.subsurface(animacion_aux))

animacion_pocion = pg.image.load("imagenes/jugador/items/pocion.png")
animacion_pocion = pg.transform.scale(animacion_pocion,(animacion_pocion.get_width()*0.5,animacion_pocion.get_height()*0.5),)

coi_1 = Items(250,80,animacion_moneda,1) #highest
coi_2 = Items(250,330,animacion_moneda,1) #2
coi_3 = Items(1100,245,animacion_moneda,1)
coi_4 = Items(942,611,animacion_moneda,1)
poscion_1 = Items (288,330,[animacion_pocion],2)
poscion_2 = Items (620,444,[animacion_pocion],2)
poscion_3 = Items (770,88,[animacion_pocion],2)

grupo_sprites_items = pg.sprite.Group()
grupo_sprites_items.add(coi_1)
grupo_sprites_items.add(coi_2)
grupo_sprites_items.add(coi_3)
grupo_sprites_items.add(coi_4)

grupo_sprites_items.add(poscion_1)
grupo_sprites_items.add(poscion_2)
grupo_sprites_items.add(poscion_3)

#AJUSTES PARA EL MAPA
datos_mapa = [
    
    [54,41,	41,	41,	41,	41,	41,	41,	41,	41,	41,	41,	53,	11,	11,	11,	11,	54,	41,	41,	41,	41,	41,	41,	41,	41,	41,	41,	41,	55,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [54,41,	41,	41,	41,	41,	41,	41,	55,	11,	11,	11,	0,	11,	11,	11,	11,	1,	1,	1,	1,	1,	1,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	1,	1,	1,	1,	1,	1,	1,	1,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	4,	4,	4,	4,	4,	4,	11,	11,	11,	11,	50,	41,	41,	41,	55,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	50,	41,	41,	41,	41,	41,	41,	41,	55,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	40,	41,	41,	41,	45,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	0,],
    [54,41,	41,	41,	41,	41,	41,	41,	41,	55,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	5,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	0,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	1,	1,	1,	1,	1,	1,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [5,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	11,	0,],
    [1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,],  

]

tile_list = []
for x in range (100):
    tile_image = pg.image.load(f"imagenes/mapa/_tile ({x+1}).png")
    tile_image = pg.transform.scale(tile_image,(cons.TILE_SIZE,cons.TILE_SIZE))
    tile_list.append(tile_image)
mapa = Mundo()
mapa.prosse_data(datos_mapa,tile_list)
lista_obstaculos = mapa.obstaculos

imagen_puerta_1 = pg.image.load("imagenes/mapa/_tile (67).png")
imagen_puerta_1 = pg.transform.scale(imagen_puerta_1,(imagen_puerta_1.get_width()*5,imagen_puerta_1.get_height()*4))
imagen_puerta_2 = pg.image.load("imagenes/mapa/_tile (68).png")
imagen_puerta_2 = pg.transform.scale(imagen_puerta_2,(imagen_puerta_2.get_width()*4.9,imagen_puerta_2.get_height()*4))
puerta_1 = Puerta(imagen_puerta_1,550,30)
puerta_2 = Puerta(imagen_puerta_2,640,30)

grupo_sprites_puertas = pg.sprite.Group()
grupo_sprites_puertas.add(puerta_1)
grupo_sprites_puertas.add(puerta_2)

nivel_1 = True #variable control del nivel

def nivel_2 ():
    pantalla_nivel_2 = pg.image.load("imagenes/mapa/pantalla_negra.jpg")
    pantalla_nivel_2 = pg.transform.scale(pantalla_nivel_2, (pantalla_nivel_2.get_width()*10, pantalla_nivel_2.get_height()*10))
    if jugador.rect.bottom < 0 :
        grupo_sprites_balas.empty()
        grupo_sprites_player.empty()
        grupo_sprites_items.empty()
        grupo_sprites_textos.empty()
        grupo_sprites_puertas.empty()
        grupo_sprites_enemis.empty()
        ventana.blit(pantalla_nivel_2,(0,0))
        dibujar_textos("¡NIVEL 2!", fuente_nivel_2, cons.ROJO,500,350)
def game_over():
    if jugador.vida == 0 :
        grupo_sprites_balas.empty()
        grupo_sprites_player.empty()
        grupo_sprites_items.empty()
        grupo_sprites_textos.empty()
        grupo_sprites_puertas.empty()
        grupo_sprites_enemis.empty()
        ventana.fill(cons.ROJO_OSCURO)
        dibujar_textos("GAME OVER :(", fuente_nivel_2, cons.AMARILLO_PALIDO,500,350)
        
def pantalla_inicio ():
    ventana.fill(cons.MORADO)
    dibujar_textos("JUEGO",funte_titulo,cons.BLANCO,cons.ANCHO/2-100,cons.ALTO/2-200)
    pg.draw.rect(ventana,cons.AMARILLO_PALIDO,boton_jugar)
    pg.draw.rect(ventana,cons.AMARILLO_PALIDO,boton_salir)
    ventana.blit(texto_boton_jugar,(boton_jugar.x+85,boton_jugar.y+15)) 
    ventana.blit(texto_boton_salir,(boton_salir.x+85,boton_salir.y+15))    
    pg.display.update()
#CICLO DE JUEGO

#SONIDOS
pg.mixer.music.load("sonidos/Music/Goblins_Dance_(Battle).wav")
pg.mixer.music.play(-1)
sonido_bala = pg.mixer.Sound("sonidos/shoot.mp3")
run = True
mostar_inicio = True
while run:
    if mostar_inicio:
        pantalla_inicio()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostar_inicio = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if boton_salir.collidepoint(event.pos):
                    run = False
    else:
    
        clock.tick(cons.FPS) #control fps    
        dibujar_cuadricula()
        mapa.draw(ventana)
        
        #UPDATES
        nivel_2()
        if jugador.rect.bottom < 0 :
            nivel_1 = False
        #update jugador
        grupo_sprites_player.update(lista_enemigos,lista_obstaculos)
        if jugador.vivo == True:
            if nivel_1 == True:
                corazones_jugador()    #dibujar corazones
        key = pg.key.get_pressed()
        jugador.control_tecla(key)
        game_over()
        #update balas
        bala = arma.update(jugador)
        
        if bala:
            grupo_sprites_balas.add(bala)
            sonido_bala.play()
        for bala in grupo_sprites_balas:
            damage , pos_daño = bala.update(lista_enemigos,jugador,lista_obstaculos)
            if damage != 0:
                daño_texto = TextoDaño(pos_daño.centerx,pos_daño.centery,str(damage),fuente_daño,cons.ROJO)
                grupo_sprites_textos.add(daño_texto)  
                
        #update enemigos   
        grupo_sprites_enemis.update(jugador,lista_obstaculos)
                
        #update items
        grupo_sprites_items.update(jugador)
        
        #update textos
        grupo_sprites_textos.update()
        
        #update puertas
        grupo_sprites_puertas.update(jugador)
            
        #DRAW´S    
        
        #dibuja texto puntuacion
        if jugador.vivo == True:
            if nivel_1 == True:
                dibujar_textos(f"Puntuacion: {jugador.puntuacion}",fuente_puntuacion,cons.AMARILLO,1000,30)
        
        #dibujar jugador        
        grupo_sprites_player.draw(ventana)

        #dibujar el arma
        if jugador.vivo == True:
            arma.draw(ventana)
        
        #dibujar balas
        grupo_sprites_balas.draw(ventana)
        
        #dibujar enemigos
        grupo_sprites_enemis.draw(ventana)
        
        #dibujar textos
        grupo_sprites_textos.draw(ventana)
        
        #dibujar items
        grupo_sprites_items.draw(ventana)
        
        #dibuja puertas
        grupo_sprites_puertas.draw(ventana)
        #VENTANA    
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False         
            
pg.quit()
sys.exit()