nome = input("Digite o seu nome: ")
nota = float(input("Digite a sua nota: "))
def status (nota):
    if nota >= 7:
        print(f'{nome} aprovado')
    elif nota >= 5:
        print(f'{nome} em recuperação')
    else:
        print(f'{nome} reprovado')
status(nota)
