from random import randint

quantidade = 1
lista = []

while quantidade <= 20:
    n = randint(0, 50)
    lista.append(n)
    quantidade += 1
print(lista)

indice = quantidadespares = quantidadesimpares = 0

while indice < len(lista):
    if lista[indice] % 2 == 0:
        quantidadespares += 1
    else:
        quantidadesimpares += 1
    indice += 1
print(quantidadespares)
print(quantidadesimpares)
