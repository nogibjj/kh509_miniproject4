import pandas as pd 
import matplotlib.pyplot as plt

df1 = pd.read_csv('iris.csv')

def calc_desc_stat(dataset_col):
    out=dataset_col.describe()
    return out

print(calc_desc_stat(df1['petal.length']))

def boxplot_of_col(dataset_col):
    boxplot = dataset_col.boxplot()
    return boxplot
