#autor felipe davi
#projeto: entendendo tratamento de exceçao

print("conversao de temperatura")
print("felipe davi")
try:
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"a temperatura em fahrenheit é: {fahrenheit}")
except ValueError:
    print("somente permitido numeros, daremos outra tentativa")