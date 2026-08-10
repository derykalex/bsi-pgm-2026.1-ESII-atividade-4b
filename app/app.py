import streamlit as st

from app.sistema import SistemaDeEmprestimos


st.set_page_config(
    page_title="Sistema de Empréstimos",
    layout="wide",
)

st.title("📚 Sistema de Empréstimos - UFRA Paragominas")

# Inicializa o sistema (Facade)
if "sistema" not in st.session_state:
    st.session_state.sistema = SistemaDeEmprestimos()

sistema = st.session_state.sistema

# Menu lateral
opcao = st.sidebar.selectbox(
    "Escolha uma opção",
    [
        "Registrar Empréstimo",
        "Registrar Devolução",
        "Empréstimos em Atraso",
        "Equipamentos",
    ],
)

if opcao == "Registrar Empréstimo":
    st.subheader("Novo Empréstimo")

    col1, col2 = st.columns(2)

    with col1:
        equip_id = st.number_input(
            "ID do Equipamento",
            min_value=1,
            value=1,
        )
        nome = st.text_input("Nome do Usuário")

    with col2:
        email = st.text_input("Email")
        dias = st.number_input(
            "Dias de Empréstimo",
            min_value=1,
            value=7,
        )

    if st.button("Registrar Empréstimo"):
        sucesso = sistema.registrar(
            equip_id,
            nome,
            email,
            dias,
        )

        if sucesso:
            st.success("✅ Empréstimo registrado com sucesso!")
        else:
            st.error("❌ Equipamento indisponível ou inexistente.")

elif opcao == "Registrar Devolução":
    st.subheader("Devolução de Empréstimo")

    emp_id = st.number_input(
        "ID do Empréstimo",
        min_value=1,
    )

    if st.button("Registrar Devolução"):
        sucesso = sistema.registrar_devolucao(emp_id)

        if sucesso:
            st.success("✅ Devolução registrada!")
        else:
            st.error("❌ Empréstimo inválido.")

elif opcao == "Empréstimos em Atraso":
    st.subheader("📅 Empréstimos em Atraso")

    sistema.listar_atrasados()

elif opcao == "Equipamentos":
    st.subheader("Equipamentos Cadastrados")

    # Lista de equipamentos pode ser implementada posteriormente.
    st.info("Consulta de equipamentos disponível em breve.")

st.sidebar.info(
    "Sistema refatorado com Factory, Facade, Strategy e Observer"
)
