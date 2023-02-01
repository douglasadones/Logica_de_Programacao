"""Crie duas funções, a primeira chamada sortear() e a segunda somar_par(). A função sortear()
sorteia  (gera)  dez  números,  armazenando‐os  em  uma  lista  chamada numeros.  A  função
somar_par() vai mostrar a soma dos números pares sorteados na função sortear(). """

from random import randint


def sortear():
    numeros = [randint(0, 10) for random in range(10)]
    print(f"Lista gerada: {numeros}")
    return numeros


def somar_par(teste):
    total = 0
    for n in teste:
        if n % 2 == 0:
            total += n
    print(f"A soma dos números pares é: {total}")


lista = sortear()
somar_par(lista)
