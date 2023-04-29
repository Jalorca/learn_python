import pandas as pd
a = [1,2,4]
x = pd.Series(a)
print(x)

#Labels
#Si no se definen los labels, toman por defecto los valores 0,1,..
print(x[0])

#Crear labels
y = pd.Series(a,index=['x','y','z'])
print(y)

#Keay/Value para crear una serie
cal = {'d1':420,'d2':400,'d3':380}
z = pd.Series(cal)
print(z)

# Seleccionar que elementos incluir en la serie
w = ( pd.Series(cal, index=['d1','d2']))
print(w)