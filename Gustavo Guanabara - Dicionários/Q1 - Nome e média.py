"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionários. No final, mostre
o conteúdo da estrutura na tela."""
aluno = {}
nome = input("Informe o nome do aluno: ")
aluno["Nome"] = nome

for nota in range(1, 4):
    n = float(input(f"Informe a {nota}ª nota: "))
    aluno[f"nota{nota}"] = n
aluno["Média"] = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
if 4.0 < aluno["Média"] < 7.0:
    aluno["Situação"] = "Exame Final"
elif aluno["Média"] >= 7.0:
    aluno["Situação"] = "Aprovado(a)"
else:
    aluno["Situação"] = "Reprovad(a)"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
