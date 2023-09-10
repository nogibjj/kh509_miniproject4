import pandas as pd
from stat1 import calc_desc_stat, boxplot_of_col
import os

data = {'Height': [5.1, 6.2, 5.1, 5.2]}

testing_df = pd.DataFrame(data)
#out=calc_desc_stat(testing_df['Height'])

def test_stats():
    out=calc_desc_stat(testing_df['Height'])
    assert(out[1]) == 5.40
    assert(out[3]) == 5.10
    assert(out[7]) == 6.20
    assert(out[2]) == 0.54

def does_graph_save():
    boxplot_of_col(testing_df,'Height')
    assert os.path.isfile("boxplot.png")