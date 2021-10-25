#Write a NumPy program to convert an array to a float type.
#Español: Escribe un programa de NumPy que convierta un arreglo a tipo flotante

import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
x = np.asfarray(a)
print("Array converted to a float type:")
print(x)