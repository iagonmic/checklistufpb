import sqlite3
import streamlit as st
from datetime import datetime

def init_tracking_db():
    conn = sqlite3.connect('user_interactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                username TEXT, action_type TEXT, item_id TEXT, timestamp DATETIME''')
    conn.commit()
    conn.close()

def log_interaction(username, action_type, item_id):
    conn = sqlite3.connect('user_interactions.db')
    c = conn.cursor()
    
# Load and display the logo
st.image("logo_ufpb.png", width=100)

# Title
st.title("Ementa UFPB CÁLCULO DIFERENCIAL E INTEGRAL II")
st.caption("(Cód.1103178)")

# Main content

st.header("1. Integral De Funções De Uma Variável")

# Seção 1.1
with st.expander("1.1 Primitivas e o Conceito De Integral"):
    st.checkbox("[Integral Indefinida - Definição](https://www.youtube.com/watch?v=IEif-WBad4U)")
    st.checkbox("[Como Integrar Potências De X](https://www.youtube.com/watch?v=n1JOygBMH6I)")

    st.subheader("EXERCÍCIOS")
    st.checkbox("[Integral Indefinida Exercícios Resolvidos](https://www.youtube.com/watch?v=-guXJsi1_pQ)")
    st.checkbox("[Problemas de Valor Inicial](https://www.youtube.com/watch?v=kGVQIr9OE3c) (Aqui é utilizado método de substituição, recomendado pular se for estudar pela primeira vez)")
    st.checkbox("[Resolução De Exercícios Sobre Integral Indefinida](https://www.youtube.com/watch?v=ZXzo7TitXP4) (Aqui é utilizado método de substituição, recomendado pular se for estudar pela primeira vez)")
    st.checkbox("[Exercícios Resolvidos](https://www.youtube.com/watch?v=30UPUOESJBw) (Ver apenas depois de estudar as técnicas de integração, recomendado pular se não viu ainda)")

# Seção 1.2
with st.expander("1.2 Técnicas de Integração"):
    st.write("SUBSTITUIÇÃO")
    st.checkbox("[Integral Por Substituição](https://www.youtube.com/watch?v=GeDvFMNW7wQ)")
    st.checkbox("[Integral Por Substituição Exercícios Resolvidos](https://www.youtube.com/watch?v=ZKO4dIyHAPs)")

    st.write("POR PARTES")
    st.checkbox("[Método de Integração por Partes](https://www.youtube.com/watch?v=D-FAKmJMNJo)")
    st.checkbox("[Integração Por Partes Exercícios Resolvidos](https://www.youtube.com/watch?v=q7rLwHylnf8)")
    st.checkbox("[Resolução de Exercícios: Integração por Partes](https://www.youtube.com/watch?v=HQ4kPrI_Rqo)")

# Seção 1.3
with st.expander("1.3 Teorema Fundamental do Cálculo (Integral Definida)"):  # Adicionar checkboxes ou outros elementos aqui
    st.checkbox("[Integral Definida](https://www.youtube.com/watch?v=b_obOKXOp-w)")
    st.checkbox("[Como Calcular Integral Definida](https://www.youtube.com/watch?v=OnNumVQkHgQ)")

with st.expander("1.4 Integral Imprópria"):
    st.checkbox("[Integrais Impróprias](https://www.youtube.com/watch?v=0cqcO9opyuU)")

with st.expander("1.5 Aplicações: comprimento de curvas, área de uma região plana, volume de sólidos de revolução"):
    pass  # Adicionar checkboxes ou outros elementos aqui

with st.expander("1.6 Área em coordenadas polares"):
    pass  # Adicionar checkboxes ou outros elementos aqui