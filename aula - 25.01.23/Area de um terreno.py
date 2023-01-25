"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e
comprimento) e mostre a área do terreno.
"""


def area(larg, comp):
    total = larg * comp
    print(f"A área do terreno de dimensões {larg} x {comp} é: {total:.1f}")


largura = float(input("Informe a largura do terreno: "))
comprimento = float(input("Informe o comprimento do terreno: "))
area(largura, comprimento)
