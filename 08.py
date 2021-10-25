#Write a NumPy program to create a 2d array with 1 on the border and 0 inside
#Español: Escribe un programa de NumPy para crear un arreglo 2D donde los bordes seran 1 y el centro 0

import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0  #el primer 1 indica el orden en donde se van a empezar a reemplazar, y el numero negativo indica el numero 
                  #en donde se va a parar (uno antes de terminar). La primera es columna y la segunda fila
print(x)          