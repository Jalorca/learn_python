import pandas as pd

DL = pd.read_csv('podcasts.csv')

print(DL.to_string)
#print(DL)

# Maxima cantidad de filas que muestra print
print(pd.options.display.max_rows)