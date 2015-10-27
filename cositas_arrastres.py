'''
Created on 07/11/2015

@author: Emanuel
'''


import pygame
import sys

from pygame.locals import *
from pygame.constants import  *
from pygame.event import Event
#from pygame.tests.base_test import pygame_quit
x=1200
y=845
arrastre=0


pygame.init()

mostrar=1
condicion=0

        
       
class secuencias():
    def __init__ (self):
        self.entrar1=pygame.image.load("imagenes/entrar1.png")
        self.entrar2=pygame.image.load("imagenes/entrar2.png")
        self.nivel1=pygame.image.load("imagenes/nivel1.png")
        self.nivel2=pygame.image.load("imagenes/nivel2.png")
        self.nivel3=pygame.image.load("imagenes/nivel3.png")
        self.nivel4=pygame.image.load("imagenes/nivel4.png")
        self.nivel5=pygame.image.load("imagenes/nivel5.png")
        self.cuatro=pygame.image.load("imagenes/cuatro.png")
        self.dos=pygame.image.load("imagenes/dos.png")   
        self.siguiente1=pygame.image.load("imagenes/siguiente1.png")
        self.siguiente2=pygame.image.load("imagenes/siguiente2.png")
        self.final=pygame.image.load("imagenes/final.png")
        self.finalizar1=pygame.image.load("imagenes/finalizar1.png")
        self.finalizar2=pygame.image.load("imagenes/finalizar2.png")
       
        
        
        
    def interfaz_nivel1(self,ubicacion):
        ubicacion.blit(self.nivel1,(0,0))
        #AQUI 
        #ubicacion.blit(self.siguiente1,(580,580))
        #ubicacion.blit(self.siguiente1,(300,470))
        ubicacion.blit(self.cuatro,(450,580))
        self.nivel1=pygame.transform.scale(self.nivel1,(x,y))

        #ubicacion.blit(self.siguiente2,(220,510))
       
        
    def posicion_nivel1(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        #AQUI
        #if (x_mouse > 588 and x_mouse <= 846) and (y_mouse > 590 and y_mouse < 980) and mostrar==0 :
            #ubicacion.fill((255,255,255))
            
            #mostrar=2     
        if (x_mouse > 939 and x_mouse <= 1143) and (y_mouse > 736 and y_mouse < 782) :
            ubicacion.fill((255,255,255))
            
            mostrar=2   
           
    def interfaz_nivel2(self,ubicacion):
        ubicacion.blit(self.nivel2,(0,0))
        
        self.nivel2=pygame.transform.scale(self.nivel2,(x,y))
        
        
    def posicion_nivel2(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 880 and x_mouse <= 1099) and (y_mouse > 765 and y_mouse < 826) :
            #ubicacion.fill((255,255,255))
            mostrar = 3
            
    def interfaz_nivel3(self, ubicacion):
        ubicacion.blit(self.nivel3,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel3=pygame.transform.scale(self.nivel3,(x,y))
        
    def posicion_nivel3(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 935 and x_mouse <= 1148) and (y_mouse > 733 and y_mouse < 800) :
            ubicacion.fill((255,255,255))
            
            mostrar =4
            
    def interfaz_nivel4(self, ubicacion):
        ubicacion.blit(self.nivel4,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel4=pygame.transform.scale(self.nivel4,(x,y))
        
    def posicion_nivel4(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 959 and x_mouse <= 1172) and (y_mouse > 748 and y_mouse < 813) :
            ubicacion.fill((255,255,255))
            
            mostrar =5
    
    def interfaz_nivel5(self, ubicacion):
        ubicacion.blit(self.nivel5,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel5=pygame.transform.scale(self.nivel5,(x,y))
        
    def posicion_nivel5(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 932 and x_mouse <= 1131) and (y_mouse > 734 and y_mouse < 790) :
            ubicacion.fill((255,255,255))
            
            mostrar =6
            
    def interfaz_final(self, ubicacion):
        ubicacion.blit(self.final,(0,0))
        ubicacion.blit(self.finalizar1,(220,510))
        ubicacion.blit(self.finalizar2,(220,510))
        
    def posicion_final(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 220 and x_mouse <= 510) and (y_mouse > 515 and y_mouse < 600) :
            sys.exit(0)
            ubicacion.fill((255,255,255))
            
            mostrar =6      
    
    def evento_clic(self,ubicacion):
        global arrastre, mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if(x_mouse > 450 and x_mouse <= 510) and (y_mouse > 490 and y_mouse < 640) :
            
            arrastre=1
            ubicacion.fill((255,255,255))
        
        elif (x_mouse > 720 and x_mouse <= 900) and (y_mouse > 280 and y_mouse < 562) and arrastre==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.cuatro,(780,370))
            
            arrastre=0
            mostrar=0
        
            
        
        elif (y_mouse > 540 or y_mouse < 254) or (x_mouse > 939 or x_mouse <= 685) and arrastre==1:
            ubicacion.blit(self.cuatro,(780,370))
            arrastre=0
            mostrar=1
            ubicacion.blit(self.nivel1,(0,0))
        
        

    def movimiento_numeros(self,ubicacion):
        

        x_mouse, y_mouse = pygame.mouse.get_pos()
        x_mouse=x_mouse-50
        y_mouse = y_mouse - 45
        ubicacion.blit(self.nivel1,(0,0))
        
        ubicacion.blit(self.cuatro,(x_mouse,y_mouse))
      

def main():
    global mostrar,condicion, arrastre
   
    x_mouse, y_mouse = pygame.mouse.get_pos()
    
    ventana = pygame.display.set_mode((x,y))
    
    pygame.display.set_caption("Secuencias Numericas")
  
    secundaria=secuencias()
 
    
    
    #boton1=entrar1,entrar2
    
    #cursor1=cursor()
    
    while True:  
        
        for evento in pygame.event.get():
            
            if evento.type == QUIT:
                
                sys.exit()
                #cursor1.update()
                
            elif evento.type == MOUSEBUTTONDOWN:
                if(mostrar==1):
                    secundaria.posicion_nivel1(ventana)
                    secundaria.evento_clic(ventana)
                elif(mostrar==2):
                    secundaria.posicion_nivel2(ventana)
                elif(mostrar==3):
                    secundaria.posicion_nivel3(ventana)
                elif(mostrar==4):
                    secundaria.posicion_nivel4(ventana)
                elif (mostrar==5):
                    secundaria.posicion_nivel5(ventana)
                elif (mostrar==6):
                    secundaria.posicion_final(ventana)
                        #elif (mostrar==6):
                 # secundaria.posicion_final(ventana)
                 
            
            
                
            elif evento.type == KEYDOWN:
                
                if evento.key == K_ESCAPE:
                    
                    sys.exit(0) 
                         
            
        x_mouse, y_mouse = pygame.mouse.get_pos()
        salida=str(x_mouse)+"----"+str(y_mouse)
        fuente_sistema=pygame.font.SysFont("comicsansms",50)
        mi_texto=fuente_sistema.render(salida,True,(0,255,0))
                                     
        if(mostrar==1):
            secundaria.interfaz_nivel1(ventana)
            ventana.blit(mi_texto,(50,50))
            
            #principal.cursor(ventana)
            #boton1.update(ventana,cursor1)
            #print (x_mouse, y_mouse)
        elif (mostrar==2):
            secundaria.interfaz_nivel2(ventana)
            ventana.blit(mi_texto,(50,50))
        elif(mostrar==3):
            secundaria.interfaz_nivel3(ventana)
            ventana.blit(mi_texto,(50,50))
            
            #principal.cursor(ventana)
            #boton1.update(ventana,cursor1)
            #print (x_mouse, y_mouse)
        elif (mostrar==4):
            secundaria.interfaz_nivel4(ventana)
            ventana.blit(mi_texto,(50,50))
        
        elif(mostrar==5):
            secundaria.interfaz_nivel5(ventana)
            ventana.blit(mi_texto,(50,50))
            #principal.cursor(ventana)
            #boton1.update(ventana,cursor1)
            #print (x_mouse, y_mouse)
        elif (mostrar==6):
            secundaria.interfaz_final(ventana)
            ventana.blit(mi_texto,(50,50))
        
        if arrastre==1:
            secundaria.movimiento_numeros(ventana)
            
        

        pygame.display.update()
        
        """if(x_mouse > 450 and x_mouse <= 510) and (y_mouse > 490 and y_mouse < 640) :
            
                arrastre=1
                ubicacion.fill((255,255,255))
        
            if (x_mouse > 720 and x_mouse <= 900) and (y_mouse > 280 and y_mouse < 562) and arrastre==1:
                ubicacion.blit(self.nivel1,(0,0))
                ubicacion.blit(self.cuatro,(780,370))
            
                arrastre=0
                mostrar=0
        
            
        
            elif (y_mouse > 540 or y_mouse < 254) or (x_mouse > 939 or x_mouse <= 685) and arrastre==1:
                ubicacion.blit(self.nivel1,(0,0))
                ubicacion.blit(self.cuatro,(780,370))
                arrastre=0
                
                """
        
if __name__ == "__main__":
    
    main()    

