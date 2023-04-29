import pandas as pd

data = pd.read_csv('podcasts.csv')

# Eliminar celdas vacias
clean_data = data.dropna()
print(clean_data)

# Reemplazar espacios vacios en una celda especifica





