"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionários. No final, mostre
o conteúdo da estrutura na tela."""
aluno = {}
nome = input("Informe o nome do aluno: ")
media = float(input("Informe a média do aluno: "))
aluno["Nome"] = nome
aluno["Média"] = media
if media < 7.0:
    aluno["Situação"] = "Reprovado(a)"
else:
    aluno["Situação"] = "Aprovado(a)"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
