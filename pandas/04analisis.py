import pandas as pd

df=pd.read_csv('podcasts.csv')

print(df.head(10))
print(df.tail(10))

print(df.info())