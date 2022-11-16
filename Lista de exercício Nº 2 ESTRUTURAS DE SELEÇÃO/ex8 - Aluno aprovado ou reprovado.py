"""Escreva um programa que lê as quatro notas de um aluno e calcula a média. O programa deve imprimir a média calculada e
uma mensagem indicando se o aluno foi aprovado ou reprovado. Um aluno é aprovado quando este obtém uma média
maior ou igual a 7,0."""

notas = []
for contador in range(1, 5):
    n = float(input(f"Digite a {contador}º nota: "))
    notas.append(n)
media = sum(notas) / len(notas)
print(f"Média: {media} - ", end="")
if media >= 7.0:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")
