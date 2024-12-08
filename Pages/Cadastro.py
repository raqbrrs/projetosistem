#CADASTRO

import streamlit as st
import pandas as pd

with open("style_cadastro.css") as f:
    st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

def cadastrar_usuario(nome, email, senha):
    try:
        df = pd.read_csv('cadastros.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nome', 'Email', 'Senha'])
    novo_usuario = {'Nome': nome, 'Email': email, 'Senha': senha}
    df = df.append(novo_usuario, ignore_index=True)
    df.to_csv('cadastros.csv', index=False)

st.title("Sistema de Gerenciamento de Atividades Acadêmicas")

nome = st.text_input("Nome Completo")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Cadastrar"):
    st.switch_page("Pages/Formulário.py")

    if nome and email and senha:
        cadastrar_usuario(nome, email, senha)
        st.success(f"Cadastro realizado com sucesso! Bem-vindo, {nome}!")
    else:
        st.error("Por favor, preencha todos os campos.")


if st.checkbox("Mostrar cadastros"):
    try:
        cadastros = pd.read_csv('cadastros.csv')
        st.write(cadastros)
    except FileNotFoundError:
        st.write("Nenhum cadastro realizado ainda.")

st.sidebar.image("https://i.imgur.com/PPJ1vF0.png")
        
st.sidebar.write("💡 Use o menu lateral para navegar!")
