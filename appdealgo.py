import streamlit as st

st.set_page_config(
    page_title="Bons hábitos",
    page_icon="👌",
    layout = "wide"
)

st.title("Medidor de bons hábitos")
st.subheader("Insira seus dados para concluirmos a qualidade dos seus hábitos.")

st.sidebar.header("Seus hábitos")
sono = st.sidebar.slider("Horas de Sono", 25, 0, 12)
copos = st.sidebar.slider("Copos de água", 25, 0, 20)
exe = st.sidebar.selectbox("Pratica esportes?", ["Pratico","Não pratico"])

st.metric("Ingestão de água: ", copos, "copos de água em um dia")
st.metric("Tempo de sono: ", sono," horas")
st.metric("Exercicio: ", exe)
st.write("Hora do diagnostico!")
colun1, colun2, colun3 = st.columns(3)

with colun1:
    st.header("Água")
    st.write("Tome mais água!" if copos <= 7 else"Continue assim! Parabéns!")
with colun2:
    st.header("Sono")
    st.write("Durma mais!" if sono < 8 else "Continue assim! Parabéns")
with colun3:
    st.header("Exercícios")
    st.write("Comece a se exercitar!" if exe == "Não pratico" else "Continue assim! Parabéns!")

with st.expander("Saiba mais sobre habitos saudavéis"):
    st.write("Durma pelo menos 8 horas por dia!")
    st.write("Tome ao menos 7 copos de água por dia!")
    st.write("Pratique mais exercicios!")

st.markdown("----")
st.markdown("Skibidi Toilete")