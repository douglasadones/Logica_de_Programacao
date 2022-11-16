"""Escrever um programa que leia um número real fornecidos pelo usuário e calcule sua raiz quadrada. O programa deve
evitar calcular a raiz de um número negativo."""

from math import sqrt

numero = float(input("Digite um número real positivo para saber sua raiz: "))
if numero < 0:
    print("O Valor deve ser positivo.")
else:
    print(f"A raiz de {numero} é {sqrt(numero)}")
