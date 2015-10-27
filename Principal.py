
'''
Created on 27 de set. de 2015

@author: Mary
'''

import pygame
import sys



from pygame.locals import *
from pygame.constants import  *
from pygame.event import Event

#from SecuenciasNumericas import secuencias

#from pygame.tests.base_test import pygame_quit
pygame.init()

x=1200
y=845

#hija =secuencias()

mostrar=1
arrastre=0
soltar=0

class interfaz():
    def __init__(self):
        
        #interfaces Generales
        self.bienvenida=pygame.image.load("imagenes/bienvenida.png")
        self.menu=pygame.image.load("imagenes/menu.png")
        self.final=pygame.image.load("imagenes/final.png")
        self.creditos=pygame.image.load("imagenes/creditos.png")
        self.casita=pygame.image.load("imagenes/casita.png")
        
        
        #niveles
        self.nivel1=pygame.image.load("imagenes/nivel1.png")
        self.nivel2=pygame.image.load("imagenes/nivel2.png")
        self.nivel3=pygame.image.load("imagenes/nivel3.png")
        self.nivel4=pygame.image.load("imagenes/nivel4.png")
        self.nivel5=pygame.image.load("imagenes/nivel5.png")
        self.nivel6=pygame.image.load("imagenes/nivel6.png")
        self.nivel7=pygame.image.load("imagenes/nivel7.png")
        
        
        #numeros para el arrastre
        self.cuatro=pygame.image.load("imagenes/cuatro.png")
        self.dos=pygame.image.load("imagenes/dos.png") 
        self.no=pygame.image.load("imagenes/no.png")
        self.si=pygame.image.load("imagenes/si.png") 
        
        
        #botones 
        self.entrar1=pygame.image.load("imagenes/entrar1.png")
        self.entrar2=pygame.image.load("imagenes/entrar2.png")
        self.siguiente1=pygame.image.load("imagenes/siguiente1.png")
        self.siguiente2=pygame.image.load("imagenes/siguiente2.png")
        self.finalizar1=pygame.image.load("imagenes/finalizar1.png")
        self.finalizar2=pygame.image.load("imagenes/finalizar2.png")
        
        #interfaces de ayuda
        self.ayuda=pygame.image.load("imagenes/ayuda.png")
        self.ayudas=pygame.image.load("imagenes/ayudas.png")
        self.ayuda1=pygame.image.load("imagenes/ayuda1.png")
        self.ayuda2=pygame.image.load("imagenes/ayuda2.png") 
        self.ayuda3=pygame.image.load("imagenes/ayuda3.png")
        self.ayuda4=pygame.image.load("imagenes/ayuda4.png")
        self.ayuda5=pygame.image.load("imagenes/ayuda5.png")
        self.ayuda6=pygame.image.load("imagenes/ayuda6.png")
        self.ayuda7=pygame.image.load("imagenes/ayuda7.png")
        
        #interfaces dobles
        self.nivel1_2=pygame.image.load("imagenes/nivel1_2.png")
        self.nivel1_4=pygame.image.load("imagenes/nivel1_4.png")
        self.nivel1_24=pygame.image.load("imagenes/nivel1_24.png")
        
        verdadero=pygame.image.load("imagenes/verdadero.png")
        falso=pygame.image.load("imagenes/falso.png")
        
        
       
    
    def interfaz_principal(self,ubicacion): 
        
        ubicacion.blit(self.bienvenida,(0,0))
        self.bienvenida=pygame.transform.scale(self.bienvenida,(x,y))

    def posicion_elementos1(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 480 and x_mouse <= 720) and (y_mouse > 724 and y_mouse < 796) :
            ubicacion.fill((255,255,255))
            
            mostrar=2
            
    def interfaz2(self,ubicacion):
        self.menu=pygame.transform.scale(self.menu,(x,y))
        ubicacion.blit(self.menu,(0,0))
        
        
    def posision_elementos2(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 469 and x_mouse <=741) and (y_mouse > 284 and y_mouse < 356):
           
            mostrar = 3
        elif (x_mouse > 471 and x_mouse <= 741) and (y_mouse > 437 and y_mouse < 479) :
            
            mostrar = 11
            
        elif (x_mouse > 575 and x_mouse <= 639) and (y_mouse > 615 and y_mouse < 689) :
             
            mostrar = 17
            
        elif (x_mouse > 465 and x_mouse <= 738) and (y_mouse > 520 and y_mouse < 594) :
        
            mostrar = 18 
            
        
    def interfaz_ayuda(self, ubicacion):
        ubicacion.blit(self.ayuda,(0,0))
        
        
    def posicion_ayuda(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 372 and x_mouse <= 573) and (y_mouse > 704 and y_mouse < 770) :
            
            mostrar = 2
            
        elif (x_mouse > 734 and x_mouse <= 937) and (y_mouse > 704 and y_mouse < 770) :
            
            mostrar = 12
            
   
        
            
    def interfaz_ayudas(self, ubicacion):
        ubicacion.blit(self.ayudas,(0,0))
        
        
    def posicion_ayudas(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 144 and x_mouse <= 351) and (y_mouse > 712 and y_mouse < 780) :
            
            mostrar = 2
            
           
    def interfaz_creditos(self,ubicacion):
        ubicacion.blit(self.creditos,(0,0))
        
        
    def posicion_creditos(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
            
        if (x_mouse > 28 and x_mouse <= 265) and (y_mouse > 791 and y_mouse < 843) :
            
            mostrar = 2
            
      
        
    def posicion_salir(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 575 and x_mouse <= 626) and (y_mouse > 615 and y_mouse < 692) :
            
            sys.exit(0)
            ubicacion.fill((255,255,255))
            
            mostrar = 17
        
    
    def interfaz_casita_menu(self,ubicacion):
        ubicacion.blit(self.casita,(560,5))
        
        
    def posicion_casita_menu(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
    
            
    #Niveles
    

    
    def interfaz_nivel1(self,ubicacion):
        ubicacion.blit(self.nivel1,(0,0))
        
      
#         ubicacion.blit(self.cuatro,(450,580))
#         ubicacion.blit(self.dos,(700,580))
        self.nivel1=pygame.transform.scale(self.nivel1,(x,y))

    def posicion_nivel1(self,ubicacion):
        global arrastre, mostrar  
        x_mouse, y_mouse = pygame.mouse.get_pos()
   
        if (x_mouse > 939 and x_mouse <= 1149) and (y_mouse > 736 and y_mouse < 780):  
            
            mostrar=5
            
        #AYUDA
        if (x_mouse > 55 and x_mouse <= 179) and (y_mouse > 738 and y_mouse < 775) : 
            mostrar=4
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
    def interfaz_ayuda1(self,ubicacion):
        ubicacion.blit(self.ayuda1,(210,150))
        
    def posicion_ayuda1(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            
            mostrar =3 
            
            
    """def evento_clic_cuatro(self,ubicacion):
        global arrastre, mostrar, soltar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if(x_mouse > 450 and x_mouse <= 510) and (y_mouse > 490 and y_mouse < 640) :
            
            arrastre=1
            ubicacion.fill((255,255,255))
        
        elif (x_mouse > 720 and x_mouse <= 900) and (y_mouse > 280 and y_mouse < 562) and arrastre==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.cuatro,(780,370))
            #ubicacion.blit(self.dos,(370,280))
            
            arrastre=0
            mostrar=0
            
            
        elif (y_mouse > 540 or y_mouse < 254) or (x_mouse > 939 or x_mouse <= 685) and arrastre==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.cuatro,(780,370))
            ubicacion.blit(self.dos,(370,280))
            
            arrastre=0
            mostrar=16
        
        if (x_mouse > 939 and x_mouse <= 1149) and (y_mouse > 736 and y_mouse < 780):
            mostrar=16
        if (x_mouse > 55 and x_mouse <= 179) and (y_mouse > 738 and y_mouse < 775) : 
            mostrar=4
        
    def movimiento_numeros_cuatro(self,ubicacion):
        global arrastre, mostrar, soltar

        x_mouse, y_mouse = pygame.mouse.get_pos()
        x_mouse=x_mouse-50
        y_mouse = y_mouse - 45
        ubicacion.blit(self.nivel1,(0,0))
        
        ubicacion.blit(self.cuatro,(x_mouse,y_mouse))
        #ubicacion.blit(self.dos,(x_mouse,y_mouse))
        ubicacion.blit(self.dos,(700,580))
        arrastre=1
        #soltar=0
        
    def evento_clic_dos(self,ubicacion):
        global arrastre, mostrar, soltar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        #numero dos 
        if(x_mouse > 598 and x_mouse <= 750) and (y_mouse > 580 and y_mouse < 630) :
              
            soltar=1
            ubicacion.fill((255,255,255))
          
        elif (x_mouse > 270 and x_mouse <= 540) and (y_mouse > 280 and y_mouse < 562) and soltar==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.dos,(370,280))
            #ubicacion.blit(self.cuatro,(780,370))
            soltar=0
            #mostrar=16
            
            
        elif (y_mouse > 540 or y_mouse < 254) or (x_mouse > 520 or x_mouse <= 280) and soltar==1:
            ubicacion.blit(self.nivel1,(0,0))
            ubicacion.blit(self.dos,(370,280))
            soltar=0
            
        
        
    def movimiento_numeros_dos(self,ubicacion):
        global arrastre, mostrar, soltar

        x_mouse, y_mouse = pygame.mouse.get_pos()
        x_mouse=x_mouse-50
        y_mouse = y_mouse - 30
        ubicacion.blit(self.nivel1,(0,0))
        
        #ubicacion.blit(self.cuatro,(x_mouse,y_mouse))
        ubicacion.blit(self.dos,(x_mouse,y_mouse))
        ubicacion.blit(self.cuatro,(780,370))
        arrastre=1
        soltar=0
 

"""

    def interfaz_nivel2(self,ubicacion):
        ubicacion.blit(self.nivel2,(0,0))
    
        
        self.nivel2=pygame.transform.scale(self.nivel2,(x,y))
        #self.verdadero=pygame.transform.scale(self.verdadero,(100,100))
            #ventana.blit(verdadero,(775,245))
        
        
    def posicion_nivel2(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 882 and x_mouse <= 1099) and (y_mouse > 765 and y_mouse < 826) :
            #ubicacion.fill((255,255,255))
            mostrar = 6
            
        if (x_mouse > 990 and x_mouse <= 1108) and (y_mouse > 113 and y_mouse <= 156) : 
              

            mostrar=14
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
            
            
    def interfaz_ayuda2(self,ubicacion):
        ubicacion.blit(self.ayuda2,(210,150))
        
        
    def posicion_ayuda2(self,ubicacion):
        global mostrar
        #cerrar la ventana de ayuda para volver al nivel
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            #muestra la interfaz del nivel anterior
            mostrar =5
        
            
    def interfaz_nivel3(self, ubicacion):
        ubicacion.blit(self.nivel3,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel3=pygame.transform.scale(self.nivel3,(x,y))
        
    def posicion_nivel3(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 960 and x_mouse <= 1153) and (y_mouse > 749 and y_mouse < 803) :
            
            
            mostrar =7
            
        if (x_mouse > 992 and x_mouse <= 1107) and (y_mouse > 122 and y_mouse < 152) : 
            
            mostrar=15
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
            
    def interfaz_ayuda3(self,ubicacion):
        ubicacion.blit(self.ayuda3,(210,150))
        
    def posicion_ayuda3(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            mostrar =6
            
            
    def interfaz_nivel4(self, ubicacion):
        ubicacion.blit(self.nivel4,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel4=pygame.transform.scale(self.nivel4,(x,y))
        
    def posicion_nivel4(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 960 and x_mouse <= 1172) and (y_mouse > 752 and y_mouse < 816) :
            
            mostrar = 8
            
        if (x_mouse > 992 and x_mouse <= 1107) and (y_mouse > 122 and y_mouse < 152) : 
            
            mostrar=19
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
        
    def interfaz_ayuda4(self,ubicacion):
        ubicacion.blit(self.ayuda4,(210,150))
        
    def posicion_ayuda4(self,ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            mostrar =7
    
    
    """def interfazayuda(self, ubicacion):
        ubicacion.blit(self.ayuda,(400,300))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        #self.nivel4=pygame.transform.scale(self.nivel4,(x,y))
        
    def posicion_ayuda(self, ubicacion):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 1164 and x_mouse <= 1196) and (y_mouse > 303 and y_mouse < 341) :
            
            
            ocultar = 6
    """   
     
    def interfaz_nivel5(self, ubicacion):
        ubicacion.blit(self.nivel5,(0,0))
        
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel5=pygame.transform.scale(self.nivel5,(x,y))
        
    def posicion_nivel5(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 922 and x_mouse <= 1110) and (y_mouse > 753 and y_mouse < 805) :
            ubicacion.fill((255,255,255))
            
            mostrar= 9 
            
        if (x_mouse > 90 and x_mouse <= 160) and (y_mouse > 790 and y_mouse <= 803) : 
            
            mostrar= 20
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
            
    def interfaz_ayuda5(self,ubicacion):
        ubicacion.blit(self.ayuda5,(210,150))
        
    def posicion_ayuda5(self,ubicacion):
        global mostrar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            mostrar =8
        
            
    def interfaz_nivel6(self, ubicacion):
        ubicacion.blit(self.nivel6,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel6=pygame.transform.scale(self.nivel6,(x,y))
        
    def posicion_nivel6(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 937 and x_mouse <= 1132) and (y_mouse > 783 and y_mouse < 841) :
            ubicacion.fill((255,255,255))
            
            mostrar = 10 
            
        if (x_mouse > 1051 and x_mouse <= 1126) and (y_mouse > 94 and y_mouse <= 127) : 
            
            mostrar= 21
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
        
            
    def interfaz_ayuda6(self,ubicacion):
        ubicacion.blit(self.ayuda6,(210,150))
        
    def posicion_ayuda6(self,ubicacion):
        global mostrar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            mostrar =9
       
            
    def interfaz_nivel7(self, ubicacion):
        ubicacion.blit(self.nivel7,(0,0))
        #ubicacion.blit(self.siguiente1,(220,510))
        #ubicacion.blit(self.siguiente2,(220,510))
        self.nivel6=pygame.transform.scale(self.nivel6,(x,y))
        
    def posicion_nivel7(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 938 and x_mouse <= 1131) and (y_mouse > 783 and y_mouse < 842) :
            ubicacion.fill((255,255,255))
            
            mostrar= 13
            
        if (x_mouse > 76 and x_mouse <= 165) and (y_mouse > 824 and y_mouse < 840) :
            
            mostrar= 22
            
        if (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
            mostrar=2
            
            
    def interfaz_ayuda7(self,ubicacion):
        ubicacion.blit(self.ayuda7,(210,150))
        
    def posicion_ayuda7(self,ubicacion):
        global mostrar
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 971 and x_mouse <= 1004) and (y_mouse > 157 and y_mouse < 200) :
            #ubicacion.fill((255,255,255))
            mostrar =10
            
            
    def interfaz_final(self, ubicacion):
        ubicacion.blit(self.final,(0,0))
        #ubicacion.blit(self.finalizar1,(220,510))
        #ubicacion.blit(self.finalizar2,(220,510))
        self.final=pygame.transform.scale(self.final,(x,y))
        
    def posicion_final(self, ubicacion):
        global mostrar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 496  and x_mouse <= 733) and (y_mouse > 709 and y_mouse < 754) :
            
            
            mostrar = 2
            
           
condicion=0
condicion2=0
condicion3=0
condicion4=0
condicion5=0
condicion6=0
condicion7=0
            
        
def main():
    
    global mostrar,s
    global condicion,condicion2,condicion3,condicion4,condicion5,condicion6, condicion7
   
    x_mouse, y_mouse = pygame.mouse.get_pos()
    ventana = pygame.display.set_mode((x,y))
    
    
    pygame.display.set_caption("SECUENNUMS")
  
    principal=interfaz()
    
    
    si=pygame.image.load("imagenes/si.png")
    no=pygame.image.load("imagenes/no.png")
    verdadero=pygame.image.load("imagenes/verdadero.png")
    falso=pygame.image.load("imagenes/falso.png")
        
    
    #boton1=entrar1,entrar2
    
    #cursor1=cursor()
    
    while True:  
        
        for evento in pygame.event.get():
            
            if evento.type == QUIT:
                
                sys.exit()
                #cursor1.update()
                
            elif evento.type == MOUSEBUTTONDOWN:
                if(mostrar==1):
                    principal.posicion_elementos1(ventana)
                elif(mostrar==2):
                    principal.posision_elementos2(ventana)
                elif(mostrar==3):
                    principal.posicion_nivel1(ventana)
                    #principal.evento_clic_cuatro(ventana)
                    #principal.evento_clic_dos(ventana)
                    
                    
                elif(mostrar==4):
                    principal.posicion_ayuda1(ventana)
                elif(mostrar==5):
                    principal.posicion_nivel2(ventana)
                elif(mostrar==6):
                    principal.posicion_nivel3(ventana)
                
                elif(mostrar==7):
                    principal.posicion_nivel4(ventana)
                elif(mostrar==8):
                    principal.posicion_nivel5(ventana)
                    #if (x_mouse > 452 and x_mouse <= 500) and (y_mouse > 587 and y_mouse < 618) :
                        #ventana.blit(cuatro(358,475))
                elif(mostrar==9):
                    principal.posicion_nivel6(ventana)
                elif(mostrar==10):
                    principal.posicion_nivel7(ventana)

                
                elif(mostrar==11):
                    principal.posicion_ayuda(ventana)
                elif(mostrar==12):
                    principal.posicion_ayudas(ventana)
                elif(mostrar==13):
                    principal.posicion_final(ventana)
                elif(mostrar==14):
                    principal.posicion_ayuda2(ventana)
                elif(mostrar==15):
                    principal.posicion_ayuda3(ventana)
                elif(mostrar==16) and (arrastre==1):
                    principal.posicion_nivel1(ventana)
                elif(mostrar==17):
                    principal.posicion_salir(ventana)
                elif(mostrar==18):
                    principal.posicion_creditos(ventana)
                elif(mostrar==19):
                    principal.posicion_ayuda4(ventana)
                elif(mostrar==20):
                    principal.posicion_ayuda5(ventana)
                elif(mostrar==21):
                    principal.posicion_ayuda6(ventana)
                elif(mostrar==22):
                    principal.posicion_ayuda7(ventana)
                elif(mostrar==23):
                    principal.posicion_casita_menu(ventana)
                    
                    
               
                    
                
                
                """elif(ocultar==7):
                    principal.posicion_ayuda(ventana)
                """
                
                
            elif evento.type == KEYDOWN:
                
                if evento.key == K_ESCAPE:
                    
                    sys.exit(0)        
        x_mouse, y_mouse=pygame.mouse.get_pos()
        salida=str(x_mouse)+"----"+str(y_mouse)
        fuente_sistema=pygame.font.SysFont("comicsansms",50)
        mi_texto=fuente_sistema.render(salida,True,(0,255,0))    
                                      
        if(mostrar==1):
            principal.interfaz_principal(ventana)
            ventana.blit(mi_texto,(50,50))
            #principal.cursor(ventana)
            #boton1.update(ventana,cursor1)
            #print (x_mouse, y_mouse)
        elif (mostrar==2):
            principal.interfaz2(ventana)
            ventana.blit(mi_texto,(50,50))    
        
        elif(mostrar==3): 
            principal.interfaz_nivel1(ventana) 
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
            
            for evento in pygame.event.get():
             
                if evento.type == QUIT:
                 
                     sys.exit()
                   
                 
                elif evento.type == MOUSEBUTTONDOWN:
                     #mostrar1 lo correcto. 2 lo incorrecto y la tercera es el siguiente boton

                    if (x_mouse > 503 and x_mouse <= 563) and (y_mouse > 592 and y_mouse < 655) and condicion7==0:
                    
                        condicion7=1
                        
                    if (x_mouse > 694 and x_mouse <= 737) and (y_mouse > 584 and y_mouse < 646) and condicion7==0:
                        
                        condicion7=2
                        
                    elif (x_mouse > 939 and x_mouse <= 1149) and (y_mouse > 736 and y_mouse < 780):  
            
                        mostrar=5
            
        #AYUDA
                    elif (x_mouse > 55 and x_mouse <= 179) and (y_mouse > 738 and y_mouse < 775) : 
                        mostrar=4
            
                    elif (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
                        mostrar=2
                   
                   
                elif evento.type == KEYDOWN:
                 
                    if evento.key == K_ESCAPE:
                     
                        sys.exit(0)        
          
          
            if (condicion7==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(490,570))
                
                
            if (condicion7==2):
               
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(683,570))
            
           
            
        elif(mostrar==4):
            principal.interfaz_ayuda1(ventana)
            ventana.blit(mi_texto,(50,50))
            
        elif(mostrar==5):
            principal.interfaz_nivel2(ventana) 
            ventana.blit(mi_texto,(50,50)) 
            principal.interfaz_casita_menu(ventana)
            
            
            for evento in pygame.event.get():
             
                if evento.type == QUIT:
                 
                     sys.exit()
                   
                 
                elif evento.type == MOUSEBUTTONDOWN:
                     #mostrar1 lo correcto. 2 lo incorrecto y la tercera es el siguiente boton

                    if (x_mouse > 376 and x_mouse <= 480) and (y_mouse > 241 and y_mouse < 326) and condicion==0:
                    
                        condicion=2
                        
                    if (x_mouse > 775 and x_mouse <= 856) and (y_mouse > 240 and y_mouse < 324) and condicion==0:
                        
                        condicion=1
                        
                    if (x_mouse > 327 and x_mouse <= 410) and (y_mouse > 340 and y_mouse < 419) and condicion2==0:
                    
                        condicion2=1
                        
                    if (x_mouse > 834 and x_mouse <= 912) and (y_mouse > 339 and y_mouse < 419) and condicion2==0:
                        
                        condicion2=2
                        
                    if (x_mouse > 264 and x_mouse <= 353) and (y_mouse > 435 and y_mouse < 516) and condicion3==0:
                    
                        condicion3=1
                        
                    if (x_mouse > 898 and x_mouse <= 980) and (y_mouse > 432 and y_mouse < 517) and condicion3==0:
                        
                        condicion3=2
                        
                    if (x_mouse > 189 and x_mouse <= 286) and (y_mouse > 531 and y_mouse < 617) and condicion4==0:
                    
                        condicion4=1
                        
                    if (x_mouse > 958 and x_mouse <= 1044) and (y_mouse > 534 and y_mouse < 617) and condicion4==0:
                        
                        condicion4=2
                        
                    elif (x_mouse > 882 and x_mouse <= 1099) and (y_mouse > 765 and y_mouse < 826) :
            #ubicacion.fill((255,255,255))
                        mostrar = 6
                    elif (x_mouse > 990 and x_mouse <= 1108) and (y_mouse > 113 and y_mouse <= 156) : 
              

                        mostrar=14
            
                    elif (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
                        mostrar=2
#                     

               
                elif evento.type == KEYDOWN:
                 
                    if evento.key == K_ESCAPE:
                     
                        sys.exit(0)        
          
          
            if (condicion==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(775,245))
                
                
               

            if (condicion==2):
               
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(400,250))
                
                
            if (condicion2==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(330,335))
                
            if (condicion2==2):
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(827,335))
                
            if (condicion3==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(275,435))
                
            if (condicion3==2):
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(895,435))
                
            if (condicion4==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(200,530))
                
            if (condicion4==2):
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(955,530))
          
           
            
        elif(mostrar==6):
            principal.interfaz_nivel3(ventana)
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
            for evento in pygame.event.get():
             
                if evento.type == QUIT:
                 
                     sys.exit()
                   
                 
                elif evento.type == MOUSEBUTTONDOWN:
                     #mostrar1 lo correcto. 2 lo incorrecto y la tercera es el siguiente boton

                    if (x_mouse > 470 and x_mouse <= 543) and (y_mouse > 541 and y_mouse < 607) and condicion5==0:
                    
                        condicion5=1
                        
                    if (x_mouse > 659 and x_mouse <= 709) and (y_mouse > 541 and y_mouse < 613) and condicion5==0:
                        
                        condicion5=2
                        
                        
                    elif (x_mouse > 960 and x_mouse <= 1153) and (y_mouse > 749 and y_mouse < 803) :
            
            
                        mostrar =7
            
                    elif (x_mouse > 992 and x_mouse <= 1107) and (y_mouse > 122 and y_mouse < 152) : 
            
                        mostrar=15
            
                    elif (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
                        mostrar=2
                        
                   
                elif evento.type == KEYDOWN:
                 
                    if evento.key == K_ESCAPE:
                     
                        sys.exit(0)        
          
          
            if (condicion5==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(490,570))
                
                
            if (condicion5==2):
               
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(683,570))
                
                
         
        elif(mostrar==7):
            principal.interfaz_nivel4(ventana)
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
            for evento in pygame.event.get():
             
                if evento.type == QUIT:
                 
                     sys.exit()
                   
                 
                elif evento.type == MOUSEBUTTONDOWN:
                     #mostrar1 lo correcto. 2 lo incorrecto y la tercera es el siguiente boton

                    if (x_mouse > 510 and x_mouse <= 577) and (y_mouse > 577 and y_mouse < 645) and condicion6==0:
                    
                        condicion6=2
                        
                    if (x_mouse > 695 and x_mouse <= 739) and (y_mouse > 586 and y_mouse < 650) and condicion6==0:
                        
                        condicion6=1
                        
                        
                        
                    elif (x_mouse > 960 and x_mouse <= 1172) and (y_mouse > 752 and y_mouse < 816) :
            
                        mostrar = 8
            
                    elif (x_mouse > 992 and x_mouse <= 1107) and (y_mouse > 122 and y_mouse < 152) : 
            
                        mostrar=19
            
                    elif (x_mouse > 562 and x_mouse <= 611) and (y_mouse > 7 and y_mouse < 68):  
            
                            mostrar=2
                            
                            
    
            
                   
                elif evento.type == KEYDOWN:
                 
                    if evento.key == K_ESCAPE:
                     
                        sys.exit(0)        
          
          
            if (condicion6==1):
                si=pygame.transform.scale(si,(80,80))
                ventana.blit(si,(683,570))
                
                
            if (condicion6==2):
               
                no=pygame.transform.scale(no,(80,80))
                ventana.blit(no,(490,570))
                
                
            
        
        elif(mostrar==8):
            principal.interfaz_nivel5(ventana)
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
        elif(mostrar==9):
            principal.interfaz_nivel6(ventana)
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
        elif(mostrar==10):
            principal.interfaz_nivel7(ventana)
            ventana.blit(mi_texto,(50,50))
            principal.interfaz_casita_menu(ventana)
            
        elif(mostrar==11):
            principal.interfaz_ayuda(ventana)
            ventana.blit(mi_texto,(50,50))
        
        elif(mostrar==12):
            principal.interfaz_ayudas(ventana)
            ventana.blit(mi_texto,(50,50))
            
        elif(mostrar==13):
            principal.interfaz_final(ventana)
            ventana.blit(mi_texto,(50,50))
            
        elif(mostrar==14):
            principal.interfaz_ayuda2(ventana)
            
        elif(mostrar==15):
            principal.interfaz_ayuda3(ventana)
            
        elif(mostrar==18):
            principal.interfaz_creditos(ventana)
            ventana.blit(mi_texto,(50,50))
        
        elif(mostrar==19):
            principal.interfaz_ayuda4(ventana)
            ventana.blit(mi_texto,(50,50))
            
        elif(mostrar==20):
            principal.interfaz_ayuda5(ventana)
            ventana.blit(mi_texto,(50,50))
            
        elif(mostrar==21):
            principal.interfaz_ayuda6(ventana)
            ventana.blit(mi_texto,(50,50)) 
            
        elif(mostrar==22):
            principal.interfaz_ayuda7(ventana)
            ventana.blit(mi_texto,(50,50))   
        elif(mostrar==23):
            principal.interfaz_casita_menu(ventana)       
        
        """elif(ocultar==7):
            principal.interfazayuda(ventana)
            
            """
#         if arrastre==1:
#             principal.movimiento_numeros_cuatro(ventana)
#         elif arrastre==0:
#             principal.posicion_nivel1(ventana)
#         if soltar==1:
#             principal.movimiento_numeros_dos(ventana)
#         elif soltar==0:
#             principal.posicion_nivel1(ventana)
#         
       

        pygame.display.update()
        x_mouse, y_mouse = pygame.mouse.get_pos()
        print(x_mouse, y_mouse)
if __name__ == "__main__":
    
    main()     
