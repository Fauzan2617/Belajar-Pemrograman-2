import pandas as df
import os

os.listdir('sample_data')

data_koleksi = df.read_csv('sample_data/california_housing_train.csv')
df.head()