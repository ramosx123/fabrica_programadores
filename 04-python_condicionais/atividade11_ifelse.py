nome = input("digite seu nome: ")
nota1= float(input("digite sua primeira nota: "))
nota2= float(input("digite sua segunda nota: "))
nota3= float(input("digite sua terceira nota: "))
nota = (nota1 + nota2 + nota3) / 3

if nota >=7:
     print("parabens " + nome + " voce foi aprovado")
elif nota  >=4:
        print("voce esta de recuperação")
else:  
    print("desculpe " + nome + " voce foi reprovado, estude mais")