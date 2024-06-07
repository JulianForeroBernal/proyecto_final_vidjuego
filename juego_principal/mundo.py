import constantes as cons

obstaculos = [5,54,41,0,4,1,50,45,40,53,55]

class Mundo (): 
    def __init__(self):        
        self.map_tiles = []
        self.obstaculos = []
    def prosse_data (self, data, tile_list):
        self.level_lenght = len(data)
        for y, row in enumerate(data):                             #data =[  
            for x , tile in enumerate(row):                       #[1,1,1,1,1,12],    
                image = tile_list[tile]                           #[17,3,3,3,3,12], 
                image_rect = image.get_rect()                     #17,3,3,3,3,12], 
                image_x = x*cons.TILE_SIZE                        #[17,3,3,3,3,12], 
                image_y = y*cons.TILE_SIZE                        #[17,1,1,1,1,12] ]
                image_rect.center = (image_x,image_y)           #y enumera las listas row gurda en si la lista [] x guarda          
                tile_data = [image,image_rect,image_x,image_y]  #la posision de la lista y tile guarda el numero de las lista        
                self.map_tiles.append(tile_data)
            # tile_list son todas las imagenes de los cuadritos del mapa [el numero de la iteracion]
            # image_x ordena las imagenes en el eje x de la misama manera image_y en el eje y
                if tile in obstaculos :
                    self.obstaculos.append(tile_data)
    def draw (self, interfaz):
        for tile in self.map_tiles:
            interfaz.blit(tile[0],tile[1])
    
    
   
     
    
