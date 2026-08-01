#autor felipe davi
#projeto: entendendo tratamento de exceçao

try:
    num1 = (float(input("Digite o primeiro numero: ")))
    num2 = (float(input("digite o segundo numero: ")))

    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == "+":
        print(f"a soma dos numeros é: {num1 + num2}")
    elif operacao == "-":
     print(f"a subtração dos numeros é: {num1 - num2}")
    elif operacao == "*":
      print(f"a multiplicação dos numeros é: {num1 * num2}")
    elif operacao == "/":
      print(f"a divisão dos numeros é: {num1 / num2}")
    else:
       print("operaçao invalida, tente novamente")
except ValueError:
    print("somente permitido numeros, daremos outra tentativa")