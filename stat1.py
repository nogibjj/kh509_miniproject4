import pandas as pd 

df1 = pd.read_csv('iris.csv')

def calculate_mean(dataset_col):
    out=dataset_col.mean()
    return out

print(calculate_mean(df1['petal.length']))