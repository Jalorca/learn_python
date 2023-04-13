import numpy as np
#Arreglo con n dimensiones
a0s=np.array(1)
a1d=np.array([1,2,3])
a2d=np.array([[1,2,3], [4,5,6]])
a3d=np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

#Crear un array con n dimensiones
array = np.array([1,2,3,4], ndmin=5)

print(array)

print("Numero de dimensiones: ", array.ndim)