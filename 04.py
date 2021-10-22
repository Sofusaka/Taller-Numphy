#Write a NumPy program to create a null vector of size 10 and update sixth value to 11.
#Español: Escribe un programa de Numpy para crear un vector nulo de 10 espacios y actualiza el valor 6 a 11

import numpy as np
x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)