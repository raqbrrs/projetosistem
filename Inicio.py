import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

nomes = []

st.title("Bem-Vindo ao SGAA!")
st.write("O que é a SGAA?")
st.text("Somos uma ferramenta essencial para otimizar a organização e o acompanhamento das atividades acadêmemicas de estudantes e professores em uma instituição de ensino.  ")
st.write("")
st.header("Como devemos o chamar?")
inp_txt = st.text_input("Digite seu nome")

if inp_txt:
    st.write(f"Prazer, {inp_txt}!")

if st.button ("Próximo"):
    st.switch_page("Pages/Cadastro.py") 

st.sidebar.image("https://i.imgur.com/PPJ1vF0.png")
        
st.sidebar.write("💡 Use o menu lateral para navegar!")