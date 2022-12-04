"""Crie um programa que leia 20 números e armazene todos em uma lista(vetor). Mostrar a lista."""

elementosnalista = 0
lista = []
while elementosnalista != 20:
    n = int(input("Digite um número para armazená-lo em um vetor: "))
    lista.append(n)
    elementosnalista += 1
print(lista)
