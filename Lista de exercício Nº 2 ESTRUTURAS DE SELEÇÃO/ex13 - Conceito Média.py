"""Escreva um programa que lê a média semestral de um aluno e imprime o conceito atribuído a esta média. O conceito é
dado como segue:
Média   Conceito
10,0   <= média <= 9,0 A
9,0    <  média <= 8,0 B
8,0    <  média <= 7,0 C
7.0    <  média <= 5.5 D
5,5    <  média        E
"""

media = float(input("Digite a média do aluno: "))
if 9.0 <= media <= 10.0:
    print("Conceito: A")
elif 8.0 < media <= 9.0:
    print("Conceito: B")
elif 7.0 < media <= 8.0:
    print("Conceito: C")
elif 5.0 < media <= 7.0:
    print("Conceito: D")
elif media < 5.5:
    print("Conceito: E")
else:
    print("Valor inválido.")
