"""Escrever um programa que lê 4 valores: P, A, B e C. Se P=1 então calcular a média aritmética de A, B e C e escrever esta
média; se P=2 somar os 3 valores atribuindo este valor a uma variável qualquer e escrevendo esta soma; se P=3 fazer um
teste para saber se B é par, se é par escrever a mensagem e o valor, caso contrário escrever que é ímpar. Se for qualquer
outro valor mostrar a mensagem “operação inválida”."""

A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
P = int(input("""1. Média Aritmética dos valores;
2. Soma dos valores;
3. Verificar se o segundo valor é ou não Par.
Digite a sua escolha: """))

if P == 1:
    # TODO 1 - M.A de A, B e C
    media = (A + B + C) // 3
    print(f"A média entre os valores informados é: {media:.1f}")
elif P == 2:
    # TODO 2 - Somar A, B e C
    print(f"A soma dos valores é: {A + B + C}")
elif P == 3:
    # TODO 3 - Verificar se B é par. Caso seja, escreva "o Valor {B} é Par, caso contrário, "O Valor {B} é Ímpar
    if B % 2 == 0:
        print(f"O Valor {B} é Par.")
    else:
        print(f"O valor {B} é ímpar.")
else:
    print("Operação Inválida")