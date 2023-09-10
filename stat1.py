import pandas as pd 
import matplotlib.pyplot as plt

df1 = pd.read_csv('iris.csv')

def calc_desc_stat(dataset_col):
    out=dataset_col.describe()
    return out

print(calc_desc_stat(df1['petal.length']))
#print(df1.columns)
def boxplot_of_col(df_wanted, col):
    df_wanted.boxplot(column=col)
    plt.show()
    plt.savefig("boxplot.png")


boxplot_of_col(df1,'petal.length')