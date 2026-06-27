numero1 = input("digite o primeiro numero")
numero2 = input("digite o segundo numero")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 + numero2)
except:
    print("somente permitido numeros")
    