import streamlit as st
st.set_page_config(
    page_title="Como um bom cavalo estuda",
    page_icon="🐴",
    layout="wide"
)
st.title("Mapa de eficiência do estudo")
st.subheader("insira seu dados")

st.sidebar.header("Defina")
horas = st.sidebar.slider("Quanto tempo estuda por dia?", 25, 0, 8)
pausas = st.sidebar.slider("Quantas pausas faz nesse tempo?", 25, 0, 8)
metodo = st.sidebar.selectbox("Qual metódo do seu estudo?", ["Revisão","Leitura","Exercícios"])

st.metric("Horas de estudo por dia: ", horas)
st.metric("Pausas nesse tempo: ", pausas)
st.metric("Método: ", metodo)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sobre as horas")
    if horas < 1:
        st.write("Estude mais!")
    elif horas >= 1 and horas < 3:
        st.write("Parabéns! Esse horario está perfeito!")
    else:
        st.write("Melhor reduzir a carga!")
with col2:
    st.header("Sobre as pausas")
    if pausas < 1:
        st.write("Faça pausas!")
    elif pausas >= 1 and pausas < 5:
        st.write("Parabéns! Essa quantidade de pausas está perfeita!")
    else:
        st.write("Melhor reduzir as pausas!")
with col3:
    st.header("Metodo escolhido")
    st.write(metodo)
with st.expander("Saiba mais!"):
    st.write("Estude ao menos uma hora por dia, mas não exceda!")
    st.write("Faça pelo menos uma pausa, mas não exagere!")
    st.write("O método fica a seu critério! Particularmente, prefiro o de revisões!")
st.markdown("---")
st.markdown("Obrigado por acessar nosso site!")