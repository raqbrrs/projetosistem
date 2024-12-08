import streamlit as st
from datetime import datetime

st.title("Gerenciador de Atividades")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []  

st.subheader("Adicionar Nova Atividade")
new_task = st.text_input("Digite a nova atividade:")
new_data = st.text_input("Digite a data (dd/mm/aaaa):")

if st.button("Adicionar"):
    try:

        task_date = datetime.strptime(new_data, "%d/%m/%Y").date()
        if new_task.strip():
            st.session_state.tasks.append({"tarefa": new_task, "data": task_date, "status": "pendente"})
            st.success(f"Atividade '{new_task}' adicionada com sucesso para {task_date.strftime('%d/%m/%Y')}!")
        else:
            st.error("Por favor, insira uma atividade válida.")
    except ValueError:
        st.error("Por favor, insira uma data no formato válido (dd/mm/aaaa).")

#calculo
pendentes = [task for task in st.session_state.tasks if task["status"] == "pendente"]
feitas = [task for task in st.session_state.tasks if task["status"] == "feito"]
total_tarefas = len(st.session_state.tasks)
total_feitas = len(feitas)
total_pendentes = len(pendentes)
progresso = total_feitas / total_tarefas if total_tarefas > 0 else 0

#barra
st.subheader("Progresso das Atividades")
st.progress(progresso)  
st.write(f"Rendimento: {total_feitas} Feitas / {total_pendentes} Pendentes")


st.subheader("Atividades Pendentes")
if pendentes:
    for i, task in enumerate(pendentes):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"📋 {task['tarefa']} - {task['data'].strftime('%d/%m/%Y')}")
        with col2:
            if st.button("✅ Feito", key=f"done_{i}"):
                task["status"] = "feito"
else:
    st.info("Nenhuma atividade pendente.")


st.subheader("Atividades Feitas")
if feitas:
    for task in feitas:
        st.write(f"✔️ {task['tarefa']} - {task['data'].strftime('%d/%m/%Y')}")
else:
    st.info("Nenhuma atividade concluída.")


st.sidebar.image("https://i.imgur.com/PPJ1vF0.png")
st.sidebar.write("💡 Use o menu lateral para navegar!")