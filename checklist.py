import sqlite3
import streamlit as st
from datetime import datetime

def init_tracking_db():
    conn = sqlite3.connect('user_interactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions (
                username TEXT, action_type TEXT, item_id TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()

def log_interaction(username, action_type, item_id):
    conn = sqlite3.connect('user_interactions.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''INSERT INTO interactions VALUES (?, ?, ?, ?)''',
                (username, action_type, item_id, timestamp))
    conn.commit()
    conn.close()

def tracked_checkbox(label, key, username):
    state = st.session_state.get(key, False)
    checked = st.checkbox(label, key=key, value=state)
    if checked != state: # se a checkbox n estiver marcada
        log_interaction(username, "checkbox_toggled", key)
        st.session_state[key] = checked

def tracked_link(label, url, key, username):
    if st.markdown(f"[{label}]({url})", unsafe_allow_html=True):
        log_interaction(username, "link_clicked", key)

def checklist_page():
    st.image("logo_ufpb.png", width=100)
    
    st.title(f"Bem-vindo, {st.session_state['username']}")

    st.header("Ementa UFPB CÁLCULO DIFERENCIAL E INTEGRAL II")
    st.caption("(Cód.1103178)")

    init_tracking_db()

    with st.expander("1.1 Primitivas e o Conceito De Integral"):
        # Definição
        if tracked_checkbox("[Integral Indefinida - Definição](https://www.youtube.com/watch?v=IEif-WBad4U)", "calculo2_integral1.1_01", st.session_state['username']):
            tracked_link("[Integral Indefinida - Definição]", "(https://www.youtube.com/watch?v=IEif-WBad4U)", "link_calculo2_integral1.1_01", st.session_state['username'])
        tracked_checkbox("[Como Integrar Potências De X](https://www.youtube.com/watch?v=n1JOygBMH6I)", "calculo2_integral1.1_02", st.session_state['username'])

        # Exercícios
        st.subheader("EXERCÍCIOS")
        tracked_checkbox("[Integral Indefinida Exercícios Resolvidos](https://www.youtube.com/watch?v=-guXJsi1_pQ)", "calculo2_integral1.1_exercicio01", st.session_state['username'])
        tracked_checkbox("[Problemas de Valor Inicial](https://www.youtube.com/watch?v=kGVQIr9OE3c) (Aqui é utilizado método de substituição, recomendado pular se for estudar pela primeira vez)",
                         "calculo2_integral1.1_exercicio02", st.session_state['username'])
        tracked_checkbox("[Resolução De Exercícios Sobre Integral Indefinida](https://www.youtube.com/watch?v=ZXzo7TitXP4) (Aqui é utilizado método de substituição, recomendado pular se for estudar pela primeira vez)", 
                         "calculo2_integral1.1_exercicio03", st.session_state['username'])
        tracked_checkbox("[Exercícios Resolvidos](https://www.youtube.com/watch?v=30UPUOESJBw) (Ver apenas depois de estudar as técnicas de integração, recomendado pular se não viu ainda)", 
                         "calculo2_integral1.1_exercicio04", st.session_state['username'])
    
