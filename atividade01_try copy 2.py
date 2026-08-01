#autor felipe davi
#projeto: entendendo tratamento de exceçao

try:
    num1 = (float(input("Digite o primeiro numero: ")))
    num2 = (float(input("digite o segundo numero: "))) 
    soma = num1 + num2  
    print(f"a soma dos numeros é: {soma}")
except ValueError:
    print("somente permitido numeros, daremos outra tentativa")

