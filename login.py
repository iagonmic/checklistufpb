import streamlit as st
import hashlib
import sqlite3

# Função para criar a tabela de usuários se não existir
def init_user_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
              (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Função para adicionar um novo usuário
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute(f"INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

# Função para verificar as credenciais do usuário
def check_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute(f"SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    result = c.fetchone()
    conn.close()
    return result is not None

# Função da página de LOGIN
def login_page():
    st.title("Login - UFPB Checklist App")
    
    init_user_db()

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login",):
        if check_user(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha não cadastrados ou incorretos!")

    if st.button("Cadastro"):
        if username and password:
            add_user(username, password)
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")