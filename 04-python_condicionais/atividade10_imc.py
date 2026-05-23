nome = input("digite seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso / (altura * altura)
print("O resultado do imc é: ", imc)
if imc <= 18.5:
    print("magreza")
elif imc <= 24.9:
    print("peso ideal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau 1")
else:
    print("obesidade grave")

