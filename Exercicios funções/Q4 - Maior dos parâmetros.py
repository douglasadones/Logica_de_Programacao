"""Crie  uma  função  chamada mostra_maior()  que  recebe  uma  quantidade  variada  de  valores
inteiros e mostra o maior valor constate na relação recebida."""


def mostrar_maior(*valores):
    maior = 0
    for n in valores:
        if n > maior:
            maior = n
    print(f"O maior valor informado é: {maior}")


mostrar_maior(1, 4, 3)
mostrar_maior(1, 6, 2, 7, 5)
