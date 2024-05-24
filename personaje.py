import pygame 

class Personaje: #ora si papa!!! pygame con clases (POO)
    def __init__(self, x , y, animaciones): # variables x y y pa pocisionar el prota si no pues donde aparece ese men, skin para mostrar imagen es de 
        #tipo lista y sabe que es de tipo lista por que mas adelante a self.skin se le asigna una lista
        self.shape = pygame.Rect(0,0,15,15) # en la veriable self.shape va a haber un rectangulo que aprece en la 
        #posicion 0,0 de tamaño 20px x 20px (eso hace el metodo Rect)
        self.shape.center = (x,y) # la variable ya creada de shape en 0,0 la vamos a poner centradita donde le digamos que es x,y
        
        self.update_time = pygame.time.get_ticks() #la variable actualizacion del time = metodo de python que cuenta cuanto tiempo pasa en 
        #milisegundos desde que inicia pygamen.init
        
        self.animaciones = animaciones
        
        self.frame = 0        #con esta variable se va a iterar las imagenes del movimiento
        self.skin = self.animaciones[self.frame] #self.skin sera igual a la imagen que se le pasae en el archivo main
        
        self.flip = False # variable para controlar a donde mira el personaja invirtiendo la imagen
        
    def draw(self, interfaz):
        
        imagen_flip = pygame.transform.flip(self.skin, self.flip, False) # se le asigana a la variable imagen volteada la misma imagen del personaje
        #pero que segun la variable flip va a estar invertida  o no esto gracias al metodo pygame.transformar.voltear(que imagen?, volteo
        # en el eje x? volteo en el eje y?)
        
        interfaz.blit(imagen_flip, self.shape) #la funcion blit permite dibujar algo sobre la interfaz dicese algo asi:
        # interfaz(osea la pantallita).blit(el metodo que dibuja)(que deibuja?, en que lo dibuaj? [necesita un recatangulo donde dibujar])
                   
                    #YA NO NECESARIO PERO BUENO DE RECORDAR
                    # pygame.draw.rect(interfaz, (255,0,0), self.shape)
                    #bueno a ver creo que : esa funcion dice :
                    #pygame.dibujar.el rectagulito (donde monda dibujo? (una  interfaz o ventanita xd),
                    # de que color e?, y que dibujo? (la forma que ya cree))   ESTO ES SOLO PARA DIBUJAR UN CUADRADO X 

    def move(self, delta_x, delta_y): #funcion para el movimiento va a tomar los valores (cuanto se desplaza en x , cuanto en y)
        self.shape.x = self.shape.x + delta_x  #posicion de la figura en x += el parametro de arriba delta x
        self.shape.y = self.shape.y + delta_y #igaul pero en y
        if delta_x < 0 :
            self.flip = True #si delta x (para metro que se pasa en el archivo main cuando se presiona a o s) es menor a 0 entonces la variable flip
        if delta_x > 0 :  #que sirve para invertir la imagen se hace verdades y el personaje en el juego va a mirar entonces a la izqueirda
            self.flip = False
            
    def update(self): #funcion para actualizar el movimiento del personaje         
        coldown = 70 # con esta variable se va a determinar que tan rapido se cambia de imagen
        self.skin = self.animaciones[self.frame] #esto ya estaba arriba pero bueno
        if pygame.time.get_ticks() - self.update_time >= coldown : # si el tiempo que pasa menos el tiempo registrdo inicialmente es mayor coldow entoces
            self.frame += 1 # frame aumenta y por tanto cambia de imagen
            self.update_time = pygame.time.get_ticks() # updat time sera igual al timepo actual para que de nuevo inicia la cuenta pa cambiar de imagen
        if self.frame == 9: #si frame es igual a 9 (significa que alcanzo la ultima de nueutras diez imagenes) enton
            self.frame = 0 #se reinicia
