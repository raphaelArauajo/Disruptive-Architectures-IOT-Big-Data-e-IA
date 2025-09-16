# src/dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_engine

engine = get_engine()

@st.cache_data(ttl=60)
def load_data(view_name):
    try:
        return pd.read_sql(f"SELECT * FROM {view_name}", engine)
    except Exception as e:
        st.error(f"Erro ao carregar {view_name}: {e}")
        return pd.DataFrame()

st.set_page_config(page_title="Dashboard IoT - Temperaturas", layout="wide")
st.title("Dashboard de Temperaturas IoT")

st.header('Média de Temperatura por Dispositivo')
df_avg = load_data('avg_temp_por_dispositivo')
if not df_avg.empty:
    fig1 = px.bar(df_avg, x='room_id', y='avg_temperature', title='Média de Temperatura por Dispositivo')
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.write("Nenhum dado na view avg_temp_por_dispositivo")

st.header('Leituras por Hora do Dia')
df_hora = load_data('leituras_por_hora')
if not df_hora.empty:
    fig2 = px.line(df_hora, x='hora', y='total_leituras', title='Leituras por Hora do Dia', markers=True)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.write("Nenhum dado na view leituras_por_hora")

st.header('Temperaturas Máximas e Mínimas por Dia')
df_day = load_data('temp_max_min_por_dia')
if not df_day.empty:
    fig3 = px.line(df_day, x='dia', y=['temp_maxima','temp_minima'], title='Temperaturas Máximas e Mínimas por Dia')
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.write("Nenhum dado na view temp_max_min_por_dia")