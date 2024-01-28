# >-< importing libraries >-< #
import pandas as pd
import plotly.express as px

# >-< inserting dataframe >-< #
df = pd.read_csv('./data.csv')

# >-< capture dimention >-< #
l, c = df.shape
print(f'linhas: {l} | colunas: {c}')

# >-< checking missing values >-< #
df.isnull().sum()

# >-< remove columns >-< #
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
df.columns

# >-< descriptive statistics >-< #
df.describe().T

# >-< check diagnostic values >-<
df.diagnosis.value_counts()
    # >-< diagnostic values >-<
fig = px.bar(df.diagnosis.value_counts().reset_index(), )