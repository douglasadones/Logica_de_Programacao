# Escrever um programa que leia dois valores inteiros e apresente o maior dos valores lidos.

maiorn = int

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

if n1 > n2:
    maiorn = n1
else:
    maiorn = n2

print(f"O maior valor entre {n1} e {n2} é {maiorn}.")