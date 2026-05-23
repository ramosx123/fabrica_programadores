nome = input("digite seu nome: ")
idade = float(input("digite sua idade: "))
resposta = input("voce possui carteira de motorista? (sim/nao) e voce possui mais de 18 anos? (sim/nao): ")
                 
if resposta == "sim" and idade >= 18:
    print("parabens", nome, idade, resposta, "você foi aprovado, e pode dirigir")
else:
    print("infelizmente ", nome, "você foi reprovado e não pode dirigir")