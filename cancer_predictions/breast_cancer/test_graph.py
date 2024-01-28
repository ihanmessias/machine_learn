# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

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
sns.countplot(df, x='diagnosis', hue='diagnosis')

# M and B
df.diagnosis.value_counts()
df['diagnosis'].value_counts()

# Criação do gráfico com PX
fig = px.bar(
    #df['diagnosis'].value_counts().reset_index().sort_values(by='count')
    df['diagnosis'].value_counts().reset_index(),x='diagnosis',
    y='count', title='Contagem de M e B', color='diagnosis',
    orientation='v', labels={'diagnosis': 'Diagnóstico', 'count': 'Contagem'},)
fig.update_yaxes(showticklabels=False, showgrid=False, title_text='')
fig.update_xaxes(showgrid=False, title_text='')
fig.update_traces(hovertemplate='Contagem: %{y}')
fig.update_layout(showlegend=False )

# Criando o gráfico de barras com GO
fig = go.Figure(data=[go.Bar(
    x=df['diagnosis'].value_counts().reset_index()['diagnosis'],
    y=df['diagnosis'].value_counts().reset_index()['count'],
    orientation='v',
    hoverinfo='y',
    marker=dict(color=['linen', 'magenta'])
)])
# Configurando o layout do gráfico
fig.update_layout(
    title='Contagem de B e M',
    yaxis=dict(title='Diagnóstico' ,showticklabels=False, showgrid=False),
    xaxis=dict(title='Diagnóstico'),
    showlegend=False
)

# Criação do gráfico countplot usando o Seaborn
ax = sns.countplot(data=df, x='diagnosis', hue='diagnosis', palette='husl' )
ax.set(xlabel='Diagnóstico', ylabel='Contagem')
plt.title('Contagem de M e B')

# Barra
ax = sns.barplot(data=df['diagnosis'].value_counts().reset_index(), y='count', x='diagnosis', hue='diagnosis', palette={'M': 'red', 'B': 'blue'})
ax.set(xlabel='Diagnóstico', ylabel='Contagem')
plt.title('Contagem de M e B')

# Corr
# check correlation values
fig = px.imshow(df.corr().round(1), text_auto=True,
                labels=dict(color="Correlation"),
                aspect='auto')
# fig.update_xaxes(tickangle=270)
fig.update_layout(width=1200,height=900)