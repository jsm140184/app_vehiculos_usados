import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Explorador de Vehículos Usados")

# Subida del archivo CSV
st.sidebar.header("Sube tu archivo CSV")
uploaded_file = st.sidebar.file_uploader("Elige un archivo", type="csv")

# Si el usuario sube un archivo
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Vista previa del dataset")
    st.dataframe(df.head())

    # Histograma de kilometraje
    st.subheader("Distribución del Kilometraje (odometer)")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["odometer"], kde=True, bins=30, ax=ax1)
    st.pyplot(fig1)

    # Gráfico de dispersión entre odómetro y precio
    st.subheader("Relación entre Kilometraje y Precio")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="odometer", y="price", alpha=0.5, ax=ax2)
    st.pyplot(fig2)

    # Gráfico de conteo por tipo de vehículo
    st.subheader("Cantidad de Vehículos por Tipo")
    fig3, ax3 = plt.subplots()
    sns.countplot(data=df, y="type", order=df["type"].value_counts().index, ax=ax3)
    st.pyplot(fig3)

else:
    st.warning("Por favor, sube un archivo CSV para comenzar.")
