"""Escrever um programa que leia 2 valores inteiros a e b e os apresente com a mensagem "são múltiplos" ou "não são
múltiplos"."""

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
if a % b == 0 or b % a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")
