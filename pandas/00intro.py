import pandas as pd
mydataset={
    'autos': ['BMW', 'VOLVO','FORD'],
    'PASSING' : [ 3,7,3 ]
}

print(pd.__version__)

myvar=pd.DataFrame(mydataset)
print(myvar)

