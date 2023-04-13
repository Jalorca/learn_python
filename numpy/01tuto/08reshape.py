import numpy as np
# 1-D Arrays a n-D Arrays
a= np.array([1,2,3,4,5,6,7,8,9,10,11,12])

na= a.reshape(4,3)
print(na)

n2a=a.reshape(2,2,3)
print(n2a)
# El metodo reshape retorna una vista.
print(n2a.base)
###--------

b = np.array([1,2,3,4,5,6,7,8])
nb=b.reshape(2,2,-1)
print(nb)

#n-D Arrays a 1-D Array

c=np.array([[1,2,3,4,5],[6,7,8,9,10]])

nc=c.reshape(-1)

print(nc)