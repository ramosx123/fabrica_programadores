#autor: Felipe Davi
#projeto: loja d carro import streamlit as st
import streamlit as st

st.sidebar.image("img/logo.jpg") #logo
st.sidebar.markdown("bueno's car") #nome

lista_carros = ["audi r8", "koenigsegg jesko", "mitsubishi eclipse"]
detalhes_carros = {
    "audi r8": {"cor": "Preto", "portas": 2, "preço": 650000, "descrição": "O Audi R8 é um carro esportivo de alto desempenho, conhecido por seu design elegante e motor potente."},
    "koenigsegg jesko": {"cor": "Vermelho", "portas": 2, "preço": 2000000, "descrição": "O Koenigsegg Jesko é um hipercarro sueco, famoso por sua velocidade extrema e tecnologia avançada."},
    "mitsubishi eclipse": {"cor": "Prata", "portas": 4, "preço": 55000, "descrição": "O Mitsubishi Eclipse é um carro esportivo compacto, popular por seu estilo aerodinâmico e desempenho ágil."}
}

carro_selecionado = st.sidebar.selectbox("Selecione o carro desejado", lista_carros)
detalhes_selecionado = detalhes_carros[carro_selecionado]

st.image(f"img/{carro_selecionado}.jpg")


st.subheader("🚗 Detalhes do Veículo")
col1, col2, col3 = st.columns(3)
col1.metric("Preço Diária", f'R$ {detalhes_selecionado["preço"]}')
col2.metric("Portas", detalhes_selecionado["portas"])
col3.metric("Cor", detalhes_selecionado["cor"])
st.divider()
qtd_dias = st.number_input("Quantos dias quer ficar com o carro?", 1)
if st.button("Alugar", type="primary"):
    st.success(f'O aluguel do carro vai custar: **R$ {qtd_dias * detalhes_selecionado["preço"]}**')
st.write(f"**Preço:** R$ {detalhes_carros[carro_selecionado]['preço']}")
st.write(f"**Descrição:** {detalhes_carros[carro_selecionado]['descrição']}")