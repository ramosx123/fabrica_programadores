
#autor: felipe davi
#PROJETO: desvio condicional

#CRIAÇAO DE VARIAVEIS
nome = input("digite seu nome: ")
idade = float(input("sua idade: "))
if idade >= 18:
    print("parabens", nome, idade, "você foi aprovado")
else:
    print("infelizmente ", nome, "você foi reprovado")