MAIOR_IDADE = 18

idade = int(input("Informe sua Idade: "))

if idade >= MAIOR_IDADE:
    print("Maior Idade, pode tirar a CNH!")

if idade < MAIOR_IDADE:
    print("Você ainda não pode tirar CNH")