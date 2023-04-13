import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Cortar array [inicio:final:paso]
print(a[1:3])
print(a[-3:-1])
print(a[1:8:2])

# Cortar en array de 2 dimensiones [dimension, inicio:final:paso]
print(b[1,1:4])

# Rescatar el tercer elemento de ambos array. [dimension:dimension final, indice]
print(b[0:2,2])

# Rescatar porciones de ambos array
print(b[0:2,1:4])

