# Escrever um programa que leia três valores inteiros e os mostre na tela em ordem crescente.
valores = []
for numeros in range(1, 4):
    n = int(input(f"Digite o {numeros}° Valor: "))
    valores.append(n)
valores.sort()
print(f"Valores ordenados: {valores}")
