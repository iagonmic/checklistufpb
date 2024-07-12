import streamlit as st
import login
import checklist

# Rodando login
def main():
    st.set_page_config(page_title="UFPB Checklist App", layout="centered", page_icon="✅") # Set page config

    #with open("style.css", 'r') as css:
    #    st.html(f"<style>{css}</style>") # Inserindo os estilos

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if st.session_state["logged_in"]:
        checklist.checklist_page()
    else:
        login.login_page()

if __name__ == "__main__":
    main()