import numpy as np

a=np.array([[1,2,3,4,5,],[6,7,8,9,10]])

print(a.shape)

b = np.array([1,2,3,4,5], ndmin=5)

print(b)
print(b.shape)