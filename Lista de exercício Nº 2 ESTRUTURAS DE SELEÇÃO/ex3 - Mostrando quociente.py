"""Escreva um programa que lê dois números inteiros, correspondentes ao dividendo e ao divisor de uma divisão, e mostra o
quociente. O programa deve impedir que se efetue uma divisão por zero e imprimir uma mensagem de erro quando isso
ocorrer."""

n1 = int(input("Digite o valor do Dividendo: "))
n2 = int(input("Digite o valor do Divisor: "))
if n2 != 0:
    print(f"O quociente entre {n1} e {n2} é", f"0" if n1 == 0 else f"{n1 / n2:.2f}")
else:
    print("Divisor inválido!")
