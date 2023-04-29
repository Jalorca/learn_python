import pandas as pd
# Data frame es una estructura de datos similar a un array de 2 dimensiones, o una tabla con filas y columnas
data ={
    'Lenguaje': ['Python', 'R', 'Bash Shell'],
    'Prioridad' : [5,3,4]
}

# Cargar data en un objeto datframe
df = pd.DataFrame(data)
print(df)

# Retornar una fila
print(df.loc[0])

# Definir indices del data framer
df = pd.DataFrame(data, index=['s1','s2','s3'])
print(df)