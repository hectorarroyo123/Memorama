import time
import os
import random
matrix=[]
matrix2=[]
def matriz():	
	for i in range(4):          #crea la matriz
		a =[]
		for j in range(4):      
			a.append(" ")
		matrix.append(a)

def matriz2():
	for i in range(4):    
		a =[]
		for j in range(4):      
			a.append("X")
		matrix2.append(a)

def acomodo(): #acomoda la matriz para que se vea ordenada
	for h in range(4):
		for k in range(4):
			print(matrix[h][k], end = " ")
		print()	
		
def acomodomatrix2():
	for h in range(4):
		for k in range(4):
			print(matrix2[h][k], end = " ")
		print()	


def matrixrandom(): #acomoda las figuras en la matriz de forma aleatoria
	figuras=["♥","♥","♦","♦","♣","♣","♪","♪","•","•","♫","♫","☼","☼","¤","¤"]
	random.shuffle(figuras)
	x=0
	y=0
	for i in figuras:
		matrix[x][y]=i
		x+=1
		if x==4:
			y+=1
			x=0


def condiciones():	#encontrando al par
	x1=0
	x2=0
	y1=0
	y2=0
	cont=0
	pos1=int(input("Ingrese primera posicion: "))
	pos2=int(input("Ingrese segunda posicion: "))
	for i in range(pos1-1):
		x1+=1
		if x1==4:
			x2+=1
			x1=0
	for i in range(pos2-1):
		y1+=1
		if y1==4:
			y2+=1
			y1=0

	if matrix[x2][x1] == matrix[y2][y1]:
		cont+=1
		print("Encontraste un par")
		matrix[x2][x1]="/"
		matrix[y2][y1]="/"
		matrix2[x2][x1]="/"
		matrix2[y2][y1]="/"

	else:
		print("Fallaste, intenta de nuevo")

def Instrucciones():
	input("Presione Enter despues de leer cada instruccion")
	os.system('cls')
	input("Selecciona dos posiciones donde esta cada par")
	os.system('cls')
	input("Se mostrara el tablero con las figuras al inicio de juego durante 5 segundos")
	os.system('cls')
	input("Ingresa primero la posicion 1 presionar enter y luego posicion 2")
	os.system('cls')
	input("Ejemplo... pos1: 3 enter , pos2: 4 enter")
	os.system('cls')
	input("NO REPETIR CASILLAS VACIAS O ENCONTRADAS")
	os.system('cls')

def comparacionfinal():
	if matrix==matrix2:
		final=True
		input("♥♦♣♠FELICIDADES, GANASTE♥♦♣♠")


final=False
while True:
	Instrucciones()
	matriz()
	matriz2()
	matrixrandom()	
	while final!=True:
		acomodo()
		time.sleep(5)
		os.system('cls')
		acomodomatrix2()
		condiciones()
		comparacionfinal()









	
