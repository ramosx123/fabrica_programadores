nome = input("digite seu nome: ")
salario = float(input("digite seu salario: "))
CALCULO = salario * 0.10
if salario >= 100:
    resposta = "parabens " + nome + " voce tem dinheiro"
else:  
    resposta = "desculpe " + nome + " voce ta liso, aposte no tigre"
print(resposta)