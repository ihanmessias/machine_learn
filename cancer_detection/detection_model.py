# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# inserting dataframe
df = pd.read_csv('./data.csv')

# capture dimention
df.shape
# checking missing values and remove columns
df.isnull().sum()
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
# descriptive statistics
df.describe().T
# diagnosis values
sns.countplot(data=df, x='diagnosis', label='count')

