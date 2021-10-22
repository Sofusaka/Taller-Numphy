#Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
#Español: Escribe un programa de Numpy para convertir una lista numerica de valores a un arreglo unidimensional de NumPy

import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)