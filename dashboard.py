import streamlit as st
import pandas as pd
import plotly.express as px

st.sidebar.image("nba.png", width=200)
st.title('DashBoard da Análise dos Dados Da NBA')
st.set_page_config(layout="wide")

df = pd.read_csv('NBAcompleto.csv')

team = st.sidebar.selectbox("Team", df['Team'].unique())
df_filtro = df[df['Team'] == team]
df_filtro

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_Nome_salario = px.bar(df_filtro, y='Salary', x='Name', color='Weight', title='Salario por Jogador')
col1.plotly_chart(fig_Nome_salario, use_container_width=True)

fig_Idade_salario = px.bar(df_filtro, y='Age', x='Salary', color='Weight', title='Salario por Idade', orientation='h')
col2.plotly_chart(fig_Idade_salario, use_container_width=True)

df_salarioMedioPorTeam = df.groupby('Team')['Salary'].mean().reset_index()

fig_salarioMedio = px.bar(df_salarioMedioPorTeam, y='Salary', x='Team', title='Média Salarial por Team')
col3.plotly_chart(fig_salarioMedio, use_container_width=True)

fig_peso_altura = px.pie(df_filtro, values='Altura_em_Metros', names='Position', title='Alturas por posição')
col4.plotly_chart(fig_peso_altura, use_container_width=True)

fig_slario_posicao = px.bar(df_filtro, y='Position', x='Salary', title='Salario por Posição')
col5.plotly_chart(fig_slario_posicao, use_container_width=True)