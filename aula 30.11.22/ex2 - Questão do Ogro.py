"""Faça um programa para ajudar o ogro a saber como representar um número entre 0 e 10 com as mãos.
Regras: Quando o número for <= 5, cada dedo da mão esquerda deve ser representado como um "I" e a mão esquerda
 que ficará fechada será representada como "*".
 Ex:
 1 = I *
 3 = III *
 7 = IIIII *
 0 = * *
 """
from random import randint
tamanho = 1
lista = []
while tamanho <= 10:
    aleatorio = randint(0, 10)
    if aleatorio not in lista:
        lista.append(aleatorio)
        tamanho += 1

indice = 0
while indice < len(lista):
    numero = lista[indice]
    print(f"O número {numero} é representado como: ", end="")
    if numero == 0:
        print("* *")
    elif numero - 5 <= 0:
        print("I" * numero, "*")
    else:
        maodireita = numero - 5
        print("IIIII " + "I" * maodireita)
    indice += 1
