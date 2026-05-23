nome = input("digite seu nome: ")
telefone = input("digite seu telefone: ")
cidade = input("digite sua cidade: ")
salario = float(input("digite seu salario: "))

if salario >=1000:
    print("voce possui um salario bom")
elif salario >700:
    print("voce possui um salario razoavel")
elif salario >500:
    print("voce possui um salario baixo")
else:
    print("voce possui um salario muito baixo")