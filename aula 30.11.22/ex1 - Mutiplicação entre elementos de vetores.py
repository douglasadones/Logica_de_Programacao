"""Programa que leia dois vetores de 10 posições e faça a multiplicação dos elementos de mesmo índice,
colocando o resultado em um terceiro vetor. Mostre o vetor resultante."""

vetor1 = []
vetor2 = []
vetorresultante = []
indice = 0
controle = 1
while controle <= 20:
    elemento = int(input("Digite um valor para o vetor 1: "))
    vetor1.append(elemento)
    elemento = int(input("Digite um valor para o vetor 2: "))
    vetor2.append(elemento)
    controle += 1

while indice < len(vetor1):
    resultado = vetor1[indice] * vetor2[indice]
    vetorresultante.append(resultado)
    indice += 1

print(vetor1)
print(vetor2)
print(vetorresultante)
