import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
c = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
#Acceso a array de 1 dimension
print(a[0])
print(a[1]+a[2])

#Acceso a array de 2 dimensiones
print("El 3 elemento de la primera fila:", b[0,2])
print("El 2 elemento de la segunda fila:", b[1,1])

#Acceso a array de 3 dimensiones
print("""El tercer elemento que se encuentra 
en el primer array de la primera dimension, 
en el segundo array en la segunda dimension: """,c[0,1,2])

