nome = input("digite seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    resposta = "parabens " + nome + " voce tem um imc saudavel"
else:  
    resposta = f"desculpe {nome} voce ta gordo, va para o gym"
print(resposta)                                   