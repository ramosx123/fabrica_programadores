nome = input("digite seu nome: ")
idade = float(input("digite sua idade: "))
cidade = input("digite sua cidade: ")
resposta = "voce é menor de idade" if idade < 12 else "voce é maior de idade"
print("parabens", nome, idade, cidade, resposta)