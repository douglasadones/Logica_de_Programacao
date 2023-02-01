"""Crie  uma  função  chamada  calcular_area()  que  recebe  como  parâmetro  as  dimensões
(largura  e  comprimento)  de  um  terreno  retangular  e  mostra  a  área  do  terreno.  Crie  o
programa que testa sua função."""


def calcular_area(largura, comprimento):
    return f"A área do terreno {largura} x {comprimento} é: {(largura*comprimento):.2f}"


l = float(input("Informe a largura do terreno: "))
c = float(input("Informe o comprimento do terreno: "))

print(calcular_area(l, c))
