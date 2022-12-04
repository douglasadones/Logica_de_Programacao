"""Crie um programa que preencha uma lista com 50 números aleatórios de 0 a 50 e depois disso, mostre a lista
na ordem padrão e depois mostre a lista na ordem contrária."""
from random import randint

quantidade = 1
lista = []

while quantidade <= 50:
    n = randint(0, 50)
    lista.append(n)
    quantidade += 1
print(lista)
print(lista[::-1])


# mostrando a lista inversa sem usar o [::-1]
listainversa = []
quantidadeinversa = -1
while quantidadeinversa >= -50:
    listainversa.append(lista[quantidadeinversa])
    quantidadeinversa -= 1
print(listainversa)


# Método do Rocha: usou a ideia  len(lista) - 1 e depois inverte a posição do externo para o interno
i = 0
j = len(lista) - 1
while i < j:
    x = lista[i]
    lista[i] = lista[j]  # o final vai pro começo
    lista[j] = x  # o começo vai para o final
    i += 1
    j -= 1
print(lista)

# Mostrar o maior e o menor elemento da lista
menor = maior = indice = 0
while indice < len(lista):
    k = lista[indice]
    if indice == 0:
        menor = k
        maior = k
    else:
        if k > maior:
            maior = k
        if k < menor:
            menor = k
    indice += 1
print(maior)
print(menor)
