import streamlit as st

from app.sistema import SistemaDeEmprestimos


# Configuração da página
st.set_page_config(
    page_title="Sistema de Empréstimos UFRA",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Sistema de Empréstimos - UFRA Paragominas")
st.markdown("### Refatorado com Factory, Facade, Strategy e Observer")


# Inicializa o sistema usando a Facade
if "sistema" not in st.session_state:
    st.session_state.sistema = SistemaDeEmprestimos()

sistema = st.session_state.sistema


# Menu lateral
menu = st.sidebar.selectbox(
    "Escolha uma funcionalidade",
    [
        "🏠 Início",
        "📝 Registrar Empréstimo",
        "🔄 Registrar Devolução",
        "⏰ Empréstimos em Atraso",
    ],
)


if menu == "🏠 Início":
    st.success("Sistema funcionando com padrões de projeto modernos!")
    st.info("Use o menu lateral para navegar.")


elif menu == "📝 Registrar Empréstimo":
    st.subheader("Novo Empréstimo")

    col1, col2 = st.columns(2)

    with col1:
        equip_id = st.number_input(
            "ID do Equipamento",
            min_value=1,
            value=1,
            step=1,
        )
        nome = st.text_input("Nome do Usuário")

    with col2:
        email = st.text_input("Email do Usuário")
        dias = st.number_input(
            "Dias para Devolução",
            min_value=1,
            value=7,
        )

    if st.button("✅ Registrar Empréstimo", type="primary"):
        sucesso = sistema.registrar(
            equip_id,
            nome,
            email,
            dias,
        )

        if sucesso:
            st.success(
                f"Empréstimo registrado com sucesso para {nome}!"
            )
        else:
            st.error(
                "❌ Equipamento não encontrado ou indisponível."
            )


elif menu == "🔄 Registrar Devolução":
    st.subheader("Registrar Devolução")

    emprestimo_id = st.number_input(
        "ID do Empréstimo",
        min_value=1,
        value=1,
    )

    if st.button("🔄 Registrar Devolução", type="primary"):
        sucesso = sistema.registrar_devolucao(emprestimo_id)

        if sucesso:
            st.success("✅ Devolução registrada com sucesso!")
        else:
            st.error("❌ Empréstimo inválido ou já devolvido.")


elif menu == "⏰ Empréstimos em Atraso":
    st.subheader("Empréstimos em Atraso")

    if hasattr(sistema, "_servico"):
        atrasados = sistema._servico.repositorio.listar_em_atraso()
    else:
        atrasados = []

    if not atrasados:
        st.info("Nenhum empréstimo em atraso no momento.")
    else:
        for emp in atrasados:
            st.warning(
                f"ID {emp.id} - {emp.usuario_nome} - "
                f"Devolução prevista: {emp.data_devolucao}"
            )


st.sidebar.success("App funcional criado!")
