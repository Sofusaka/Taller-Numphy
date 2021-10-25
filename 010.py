#Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.
#Español: Escribe un programa de NumPy para crear una matriz de 8x8 y llenarla con un patron de tablero de ajedrez

import numpy as np

print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1 #esta es para alternar los impares
x[::2,1::2] = 1 #esta es para alternar los pares. Da saltos de dos en dos y comienza en la casilla inicial. La seg seccion dice que inicia en la posicion 1 y da saltos de dos en dos hasta el final
print(x)