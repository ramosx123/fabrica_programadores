valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

def calcular():
    print("Resultados:")
    print("Soma:", valor1 + valor2)
    print("Subtração:", valor1 - valor2)
    print("Multiplicação:", valor1 * valor2)
    print("Divisão:", valor1 / valor2)

print(f' o resultado da soma é: {valor1 + valor2}')
print(f' o resultado da subtração é: {valor1 - valor2}')
print(f' o resultado da multiplicação é: {valor1 * valor2}')
print(f' o resultado da divisão é: {valor1 / valor2}')

calcular()