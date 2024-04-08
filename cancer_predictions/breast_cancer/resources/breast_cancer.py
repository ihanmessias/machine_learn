# importing libraries
import pandas as pd
import plotly.express as px

# inserting dataframe
df = pd.read_csv('./data.csv')

# capture dimention
l, c = df.shape
print(f'linhas: {l} | colunas: {c}')

# checking missing values
df.isnull().sum()

# remove columns
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)
df.columns

# descriptive statistics
df.describe().T

# check diagnostic values
df.diagnosis.value_counts()
    # diagnostic values
fig = px.bar(df.diagnosis.value_counts().reset_index(), x='diagnosis',
            y='count', title='Contagem de M e B', color='diagnosis',
            color_discrete_sequence=['LightSeaGreen','lightcoral'],
            labels={'diagnosis': 'Diagnóstico', 'count': 'Contagem'})
fig.update_yaxes(showgrid=False)
fig.update_xaxes(title_text='', categoryorder='total ascending')
fig.update_traces(hovertemplate='Contagem: %{y}')
fig.update_layout(width=500, height=400)

# binary classification
df.diagnosis = df.diagnosis.apply(lambda x: 1 if x == 'M' else 0)

# check correlation values
fig = px.imshow(df.corr().round(1), text_auto=True,
            labels=dict(color='Correlation', aspect='auto'))
fig.update_xaxes(tickangle=270)
fig.update_layout(width=1200, height=900)

# removing redundant warnings
import warnings
warnings.filterwarnings('ignore')

# import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# dataset split
X = df.drop(columns=['diagnosis'])
y = df.diagnosis
X_training, X_test, y_training, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# training the model
clf = RandomForestClassifier(random_state=42)
clf.fit(X_training, y_training)

# runing the model
predictions = clf.predict(X_test)
print('Relatório de Clf:\n', classification_report(y_test, predictions))

# confusion matrix
fig = px.imshow(confusion_matrix(y_test, predictions), text_auto=True,
            labels=dict(x='Previsto', y='Real'),
            x=['B', 'M'],
            y=['B', 'M'],
            color_continuous_scale='mint')
fig.update_traces(hovertemplate='Previsto %{x}<br>Real %{y}<br>Contagem %{z}')
fig.update_layout(title='Matrix de Confusão', xaxis_title='Previsto',
            yaxis_title='Real', width=800, height=500)