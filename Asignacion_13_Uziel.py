import random,math,os,sys,pygame

class Vertice:
    def __init__(self,Numero,CoordX,CoordY,AnguloX):
        self.Numero=Numero
        self.CoordX=CoordX
        self.CoordY=CoordY
        self.AnguloX=AnguloX
    '''-----------------------------------------------------------------------------
    Nombre del método: InfoVertice
    Objetivo/propósito: Mostrar la información del vértice
    Parámetros de entrada: Ninguno
    Parámetros de salida: Ninguno
    Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
    -----------------------------------------------------------------------------'''
    def InfoVertice(self):
        CoordV=(self.CoordX,self.CoordY)
        print("Punto #",self.Numero,CoordV,end=" ")
        print("\tAngulo respecto al eje X y al punto menor:",self.AnguloX)
    '''-----------------------------------------------------------------------------
    Nombre del método: PuntoMenor
    Objetivo/propósito: Buscar el punto menor respecto a las ordenadas (Eje Y)
    Parámetros de entrada: Lista "Puntos" de objetos tipo 'Vertice'
    Parámetros de salida: Tupla "PMenor" con las coordenadas
    Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
    -----------------------------------------------------------------------------'''
    def PuntoMenor(self,Puntos):
        PMenor=(self.CoordX,self.CoordY)
        MenorY=self.CoordY
        MenorX=self.CoordX
        for i in range(1,len(Puntos)):
            if Puntos[i].CoordY<=MenorY:
                if Puntos[i].CoordY==MenorY:
                    if Puntos[i].CoordX<MenorX:
                        MenorY=Puntos[i].CoordY
                        MenorX=Puntos[i].CoordX
                        PMenor=(Puntos[i].CoordX,Puntos[i].CoordY)
                else:
                    MenorY=Puntos[i].CoordY
                    MenorX=Puntos[i].CoordX
                    PMenor=(Puntos[i].CoordX,Puntos[i].CoordY)
        return PMenor

    def ExtremosX(self,Puntos):
    	ExtremoIzquierdo=(self.CoordX,self.CoordY)
    	ExtremoDerecho=(Puntos[1].CoordX,Puntos[1].CoordY)
    	ExtMenorX=self.CoordX
    	ExtMenorY=self.CoordY
    	ExtMayorX=Puntos[1].CoordX
    	ExtMayorY=Puntos[1].CoordY
    	for i in range(1,len(Puntos)):
    		if Puntos[i].CoordX<=ExtMenorX:
    			if Puntos[i].CoordX==ExtMenorX:
    				if Puntos[i].CoordY<ExtMenorY:
    					ExtMenorX=Puntos[i].CoordX
    					ExtMenorY=Puntos[i].CoordY
    					ExtremoIzquierdo=(ExtMenorX,ExtMenorY)
    			else:
    				ExtMenorX=Puntos[i].CoordX
    				ExtMenorY=Puntos[i].CoordY
    				ExtremoIzquierdo=(ExtMenorX,ExtMenorY)
    		elif Puntos[i].CoordX>=ExtMayorX:
    			if Puntos[i].CoordX==ExtMayorX:
    				if Puntos[i].CoordY<ExtMayorY:
    					ExtMayorX=Puntos[i].CoordX
    					ExtMayorY=Puntos[i].CoordY
    					ExtremoDerecho=(ExtMayorX,ExtMayorY)
    			else:
    				ExtMayorX=Puntos[i].CoordX
    				ExtMayorY=Puntos[i].CoordY
    				ExtremoDerecho=(ExtMayorX,ExtMayorY)
    	return ExtremoIzquierdo,ExtremoDerecho

    def PuntosMenoresAB(self,Puntos,ExtIzq,ExtDer):
    	AuxMenores=[]
    	'''for i in range(0,len(Puntos)):
    		if Puntos[i].CoordX'''
    '''-----------------------------------------------------------------------------
    Nombre del método: CalcularAngulo
    Objetivo/propósito: Calcular el ángulo respecto al punto menor y el Eje X
    Parámetros de entrada: Objeto 'Vertice' "PMenor", lista "Angulos" de cada
                           'Vertice'
    Parámetros de salida: Lista "Angulos" de cada 'Vertice' en grados sexagesimales
    Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
    -----------------------------------------------------------------------------'''
    def CalcularAngulo(self,PMenor,Angulos):
        x=self.CoordX-PMenor.CoordX
        y=self.CoordY-PMenor.CoordY
        self.AnguloX=math.degrees(math.atan2(y,x)) #Modificación y cálculo del atributo AnguloX
        Angulos.append(self.AnguloX)
    '''-----------------------------------------------------------------------------
    Nombre del método: OrdenarAngularmente
    Objetivo/propósito: Ordenar los puntos de manera ascendente por su ángulo
    Parámetros de entrada: Lista "Puntos "de objetos tipo 'Vertice', lista "Angulos"
                           de cada 'Vertice'
    Parámetros de salida: Lista "Angulos" y "Puntos" ordenadas ascendentemente por
                          ángulos
    Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
    -----------------------------------------------------------------------------'''
    def OrdenarAngularmente(self,Puntos,Angulos):
        Angulos.append(self.AnguloX) #Inserción del ángulo del punto menor
        for Vertex in Puntos:
            if Vertex.CoordX!=self.CoordX and Vertex.CoordY!=self.CoordY: Vertex.CalcularAngulo(self,Angulos)
        Angulos.sort()
        Puntos.sort(key=lambda Vrx:Vrx.AnguloX)
        for N in range(0,len(Puntos)): Puntos[N].Numero=N

    def Izquierda(self,Extraido,PSig):
        #(x2-x1)(y3-y1)-(y2-y1)(x3-x1)
        Resultado=((Extraido.CoordX-self.CoordX)*(PSig.CoordY-self.CoordY))-((Extraido.CoordY-self.CoordY)*(PSig.CoordX-self.CoordX))
        if Resultado>0: return True
        else: return False

    def GrahamScan(self,Puntos,Angulos,CoHu):
        Pos=-1
        PMenor=Puntos[0].PuntoMenor(Puntos)
        #print("El punto menor respecto a las ordenadas es:",PMenor)
        Pos=BusquedaSecuencial(Puntos,Pos,PMenor)
        if Pos!=-1: Puntos[Pos].OrdenarAngularmente(Puntos,Angulos)
        #print("Angulos en orden ascendente:",Angulos)
        for P in range(0,3): CoHu.append(Puntos[P])
        i=3
        while i<len(Puntos):
            Extraido=CoHu.pop()
            Res=CoHu[len(CoHu)-1].Izquierda(Extraido,Puntos[i])
            if Res==True:
                CoHu.append(Extraido)
                CoHu.append(Puntos[i])
                i+=1

    def Quickhull(self,Puntos,CoHu):
    	MenorEjeX,MayorEjeX=Puntos[0].ExtremosX(Puntos)
    	MinYRecta=Puntos[0].PuntoMenor(Puntos)
'''-------------------------------------------------------------------------------------------
Nombre de la función: CoordAleatorias
Objetivo/propósito: Generar coordenadas de manera aleatoria
Parámetros de entrada: "Lista" de números enteros, límite inferior "Min" del rango, límite
                       superior "Max" del rango, "Cantidad" de números a generar
Parámetros de salida: "Lista" de coordenadas (para X o Y) llena
Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
-------------------------------------------------------------------------------------------'''
def CoordAleatorias(Lista,Min,Max,Cantidad):
    for i in range(0,Cantidad):
        Numero=random.randint(Min,Max) #Generación de un número entre los valores dados
        Lista.append(Numero) #Inserción del número en la lista
'''-------------------------------------------------------------------------------------------
Nombre de la función: GenerarPuntos
Objetivo/propósito: Generar objetos de tipo 'Vertice' y agregarlos a la lista "Puntos"
Parámetros de entrada: Listas de coordenadas "CoordX" y "CoordY", lista "Puntos" vacia,
                       "Cantidad" de objetos a generar
Parámetros de salida: Lista "Puntos" llena de objetos tipo 'Vertice'
Desarrolló: Uziel Moreno Andrade, 28-Marzo-2021
-------------------------------------------------------------------------------------------'''
def GenerarPuntos(CoordX,CoordY,Puntos,Cantidad):
    for i in range(0,Cantidad):
        Punto=Vertice(i,CoordX[i],CoordY[i],0) #Llamado al constructor del objeto
        Puntos.append(Punto) #Inserción del objeto en la lista
'''-------------------------------------------------------------------------------------------
Nombre de la función: BusquedaSecuencial
Objetivo/propósito: Buscar un número determinado en el arreglo mediante busqueda secuencial
Parámetros de entrada: Lista "Puntos" de objetos 'Vertice', posición "Pos" del objeto,
                       objeto "PMenor" de tipo 'Vertice' a buscar
Parámetros de salida: Posición "Pos" del objeto (si es que lo encontró)
Desarrolló: Uziel Moreno Andrade, 17-Enero-2021
-------------------------------------------------------------------------------------------'''
def BusquedaSecuencial(Puntos,Pos,PMenor):
    Pos=-1 #Se le asigna un valor para indicar no encontrado
    contador=0
    while contador<len(Puntos) and Pos==-1:
        if Puntos[contador].CoordX==PMenor[0] and Puntos[contador].CoordY==PMenor[1]:
            Pos=contador #Se guarda la posición donde se encontró el objeto
        contador+=1
    return Pos

def Pinta(dimensiones,Negro,Blanco,CoHu):
    index=0
    sig=1
    pygame.init()
    Pantalla=pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Convex-Hull")
    hecho=False
    reloj=pygame.time.Clock()
    while not hecho:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT: hecho=True
        if sig==len(CoHu): sig=0
        if index<len(CoHu):
            NewXOrigin=CoHu[index].CoordX+350
            NewYOrigin=CoHu[index].CoordY+300
            NewXDestination=CoHu[sig].CoordX+350
            NewYDestination=CoHu[sig].CoordY+300
            Pantalla.fill(Blanco)
            pygame.draw.line(Pantalla,Negro,[NewXOrigin,NewYOrigin],[NewXDestination,NewYDestination],2)
            pygame.display.flip()
            reloj.tick(60)
            index+=1
            sig+=1
        #else: hecho=True
    input("Pulse una tecla para continuar...\n")
    pygame.quit()
    
'''-----------------------------------------------------------------------------
Nombre de la función: Menu
Objetivo/propósito: Mostrar las opciones disponibles del programa y seleccionar una de ellas
Parámetros de entrada: Ninguno
Parámetros de salida: Opción seleccionada en el entero "X"
Desarrolló: Uziel Moreno Andrade, 14-Febrero-2021
-----------------------------------------------------------------------------'''
def Menu():
    print("\n----- Convex Hull -----")
    print("\nSeleccione la operación a realizar:")
    print("1) Generar vertices aleatoriamente")
    print("2) Mostrar datos de los puntos")
    print("3) Algoritmo de Graham")
    print("4) Algoritmo Quickhull")
    print("5) Eliminar todos los puntos")
    print("6) Salir")
    X=int(input("Opción>> "))
    return X

def Main():
    dimensiones=(700,700)
    Negro=(0,0,0)
    Blanco=(255,255,255)
    CoordX=[]
    CoordY=[]
    Puntos=[]
    Angulos=[]
    CoHu=[]
    NumPuntosCH=[]
    while True:
        if len(Puntos)==0: print("¡ADVERTENCIA! No hay puntos generados. Seleccione la opción 1.")
        Opcion=Menu()
        if Opcion==1: #Generar vertices aleatoriamente
            MinX=int(input("Digite el punto mínimo en X:"))
            MaxX=int(input("Digite el punto máximo en X:"))
            MinY=int(input("Digite el punto mínimo en Y:"))
            MaxY=int(input("Digite el punto máximo en Y:"))
            CantPuntos=int(input("Digite la cantidad de puntos a generar:"))
            CoordAleatorias(CoordX,MinX,MaxX,CantPuntos)
            CoordAleatorias(CoordY,MinY,MaxY,CantPuntos)
            GenerarPuntos(CoordX,CoordY,Puntos,CantPuntos)
        elif Opcion==2: #Mostrar datos de los puntos
            print("Coordenadas del eje X:",CoordX)
            print("Coordenadas del eje Y",CoordY)
            print("Puntos generados:")
            for Vertex in Puntos: Vertex.InfoVertice()
        elif Opcion==3: #Algoritmo de Graham (Graham's scan)
            Puntos[0].GrahamScan(Puntos,Angulos,CoHu)
            for Vertex in CoHu: NumPuntosCH.append(Vertex.Numero)
            print("Solución en lista ->",NumPuntosCH)
            print("\nInformación de cada vertice de la envolvente convexa:")
            for Vertex in CoHu: Vertex.InfoVertice()
            Pinta(dimensiones,Negro,Blanco,CoHu)
        elif Opcion==4:
        	MenorEjeX,MayorEjeX=Puntos[0].ExtremosX(Puntos)
        	print("Extremo menor en el eje X",MenorEjeX)
        	print("Extremo menor en el eje X",MayorEjeX)
        elif Opcion==5: #Eliminar todos los puntos
            CoordX.clear()
            CoordY.clear()
            Puntos.clear()
            Angulos.clear()
            CoHu.clear()
            os.system('cls')
        elif Opcion==6: break #Salir
        else:
            print("¡Opción no válida! Intente nuevamente con alguna de las opciones en pantalla\n")
            input("Pulse una tecla para continuar...\n")
            os.system('cls')

Main()
'''
pygame.init()
Negro=(0,0,0)
Blanco=(255,255,255)
x0=0+350
y0=0+300
x1=100+350
y1=100+300
dimensiones=(700,600)
Pantalla=pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Convex-Hull")
hecho=False
reloj=pygame.time.Clock()
while not hecho:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT: hecho=True
    Pantalla.fill(Blanco)
    pygame.draw.line(Pantalla,Negro,[x0,y0],[x1,y1],5)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()'''