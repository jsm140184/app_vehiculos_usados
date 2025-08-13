import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Explorador de Vehículos Usados')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar dataset
st.subheader('Vista previa del dataset')
st.dataframe(car_data.head())

# Botón para histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma de kilometraje (odometer)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button('Mostrar dispersión odómetro vs precio'):
    st.write('Relación entre kilometraje y precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2)
