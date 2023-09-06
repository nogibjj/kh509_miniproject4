from stat1 import calculate_mean
import pandas as pd

data = {'Height': [5.1, 6.2, 5.1, 5.2]}

testing_df = pd.DataFrame(data)


def test_mean():
    assert calculate_mean(testing_df['Height']) == 5.4