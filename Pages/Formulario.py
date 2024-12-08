#FORMULARIO

from os import write
import streamlit as st;
st.title("Incluir Aluno")
with st.form(key="include_aluno"):
    input_name = st.text_input(label="Digite o seu nome")
    input_age = st.number_input(label="Insira sua idade", format= "%d", step=1)
    input_occupation = st.selectbox("Selecione sua graduação", ["1 ano do Ensino Médio", "2 ano do Ensino Médio", "3 ano do Ensino Médio", "Ensino Superior"])
    input_curso = st.selectbox("Selecione seu curso", ["Administração","Desenvolvimento de Sistemas", "Agronegocio", "Contabilidade", "EnergiaRenovável", "Direito", "Estetica", "Música", "Outro"])
    input_button_submit = st.form_submit_button("Enviar")
if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade: {input_age}')
    st.write(f'Graduação: {input_occupation}')
    st.write(f'Curso: {input_curso}')

st.sidebar.image("https://i.imgur.com/PPJ1vF0.png")
        
st.sidebar.write("💡 Use o menu lateral para navegar!")