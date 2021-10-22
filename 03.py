#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10
#Español: Escribe un programa de Numpy para crear una matriz 3x3 con valores entre un rango de 2 a 10

import numpy as np
x =  np.arange(2, 11).reshape(3,3)
print(x)