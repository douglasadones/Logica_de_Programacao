"""Crie uma função chamada contar() que recebe três parâmetros inteiros: inicio, fim e passo e
mostra  os  valores  de  inicio  até  fim,  tendo  passo  como  intervalo  entre  os  valores
intermediários. A saída deve mostrar três tipos de contagem, conforme a seguir: a) de 1 até
10, ao passo 1; b) de 10 até 0, ao passo 1; c) uma contagem com os valores de inicio, fim e
passo informados pelo usuário."""


def contar(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" ")
            inicio += passo

    elif inicio > fim:
        while fim <= inicio:
            print(inicio, end=" ")
            inicio -= passo
    else:
        print(inicio)
    print()


# TODO 1 - a) de 1 até 10, ao passo 1;
contar(1, 10, 1)

# TODO 2 - b) de 10 até 0, ao passo 1;
contar(10, 0, 1)

# TODO 3 - c) uma contagem com os valores de inicio, fim e passo informados pelo usuário.
i = int(input("Informe o inicio: "))
f = int(input("Informe o fim: "))
p = int(input("Informe o passo: "))
contar(i, f, p)
