
# instalar o streamlit
#pip install streamlit on terminal
import streamlit as st

st.write("ola, seja bem vindo!")
st.title("calculadora de IMC")
st.write("IMC é o índice de massa corporal, que é uma medida internacional usada para calcular se uma pessoa está no peso ideal, abaixo ou acima do peso.")
st.write("Para calcular o IMC, você precisa informar seu peso em kg e sua altura em metros.")
st.write("peso (kg):")
peso = st.number_input("Digite seu peso em kg", min_value=0.0, step=0.1)
st.write("altura (m):")
altura = st.number_input("Digite sua altura em metros", min_value=0.0, step=0.01)
st.button("Calcular IMC")