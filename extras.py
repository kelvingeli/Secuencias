'''
Created on 27 de set. de 2015

@author: Mary
'''
'''
        
#class cursor(pygame.Rect):
    
    #def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    #def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
#class boton(pygame.sprite.Sprite):
    #def __init__(self,imagen1,imagen2,x=50, y=285):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    
    def update(self,ventana,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        #(x=503, y=225)
        ventana.blit(self.imagen_actual,self.rect)
    '''
      
      
     """elif (y_mouse > 540 or y_mouse < 254) or (x_mouse > 939 or x_mouse <= 685) and arrastre==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.cuatro,(780,370))
            arrastre=0"""      