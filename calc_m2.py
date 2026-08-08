import streamlit as st

st.write("ola, seja bem vindo!")
st.title("calculador de (m²)")
st.write("Para calcular a área em metros quadrados, você precisa informar o comprimento e a largura em metros.")
st.write("comprimento (m):")
comprimento = st.number_input("Digite o comprimento em metros", min_value=0.0, step=0.1)
st.write("largura (m):")
largura = st.number_input("Digite a largura em metros", min_value=0.0, step=0.1)
if st.button("Calcular m²"):
  if comprimento > 0 and largura > 0:
    area = comprimento * largura
    st.success(f"A área é: {area:.2f} m²")
  else:
      st.error("O comprimento e a largura devem ser maiores que zero.")
st.write("deseja mais informações sobre o cálculo de área em metros quadrados?")
st.title("OBTENHA NOSSO PLANO COMPLETO:")
import streamlit as st

# Injeção de CSS para o botão estilo RGB Animado
import streamlit as st

import streamlit as st

st.markdown(
    """
    <style>
    /* Estilo principal do botão */
    div.stButton > button:first-child {
        height: 70px;
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        background-color: #0e1117;
        border: none;
        border-radius: 12px;
        position: relative;
        z-index: 1;
        cursor: pointer;
        
        /* Garante que o crescimento afete o botão e os pseudoelementos juntos */
        transform-style: preserve-3d;
        transition: transform 0.1s ease-in-out, text-shadow 0.3s ease;
    }

    /* Cria a borda RGB externa */
    div.stButton > button:first-child::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        background-size: 400%;
        z-index: -1;
        border-radius: 15px;
        animation: rgb-glow 20s linear infinite;
    }

    /* Máscara interna para o contorno */
    div.stButton > button:first-child::after {
        content: '';
        position: absolute;
        top: 1px;
        left: 1px;
        right: 1px;
        bottom: 1px;
        background-color: #0e1117;
        z-index: -1;
        border-radius: 11px;
        transition: background-color 0.3s ease;
    }

    /* Animação do gradiente RGB */
    @keyframes rgb-glow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Hover (passar o mouse) - Pré-crescimento suave */
    div.stButton > button:first-child:hover {
        text-shadow: 0 0 10px rgba(255,255,255,0.8);
        transform: scale(1.02); 
    }
    div.stButton > button:first-child:hover::after {
        background-color: #1a1c23;
    }

    /* CLIQUE (Active): O botão e o contorno RGB crescem juntos */
    div.stButton > button:first-child:active {
        transform: scale(1.10) !important; /* Cresce 10% no momento exato do clique */
        transition: transform 0.05s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Renderiza o botão com a ação
if st.button("🚀 CLIQUE E VEJA CRESCER", use_container_width=True):
    st.success("Ação disparada com sucesso!")
import streamlit as st
st.write("verificar o valor do terreno em m²")
# Injeção de CSS para o botão personalizado (Grande, contorno RGB e cresce no clique)
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        height: 70px;
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        background-color: #0e1117;
        border: none;
        border-radius: 12px;
        position: relative;
        z-index: 1;
        cursor: pointer;
        transform-style: preserve-3d;
        transition: transform 0.1s ease-in-out, text-shadow 0.3s ease;
    }

    div.stButton > button:first-child::before {
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        background-size: 400%;
        z-index: -1;
        border-radius: 15px;
        animation: rgb-glow 20s linear infinite;
    }

    div.stButton > button:first-child::after {
        content: '';
        position: absolute;
        top: 1px;
        left: 1px;
        right: 1px;
        bottom: 1px;
        background-color: #0e1117;
        z-index: -1;
        border-radius: 11px;
        transition: background-color 0.3s ease;
    }

    @keyframes rgb-glow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    div.stButton > button:first-child:hover {
        text-shadow: 0 0 10px rgba(255,255,255,0.8);
        transform: scale(1.02); 
    }
    
    div.stButton > button:first-child:hover::after {
        background-color: #1a1c23;
    }

    div.stButton > button:first-child:active {
        transform: scale(1.10) !important;
        transition: transform 0.05s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧮 Calculadora de Valor de Terreno")

# Entrada do tamanho do terreno em m²
area = st.number_input(
    "Digite o tamanho do terreno em metros quadrados (m²):", 
    min_value=0.0, 
    value=100.0, 
    step=10.0
)

# Valor fixo por metro quadrado
PRECO_POR_M2 = 200.0

# Botão estilizado para calcular
if st.button("💰 CALCULAR VALOR TOTAL", use_container_width=True):
    # Cálculo preciso do valor total
    valor_total = area * PRECO_POR_M2
    
    # Exibição do resultado estilizado
    st.markdown("---")
    st.subheader(f"✅ Resultado do Cálculo")
    st.metric(label="Valor Total do Terreno", value=f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.info(f"Cálculo realizado com base na taxa fixa de R$ {PRECO_POR_M2:.2f} por m².")
