"""Crie  uma  função  chamada  notas()  que  pode  receber  várias  notas  de  um  aluno  e  vai
retornar um dicionário com as seguintes informações: Quantidade de notas, a maior nota, a
menor nota, a média das notas e a situação (opcional) de acordo com a média, sendo menor
que  4.0,  situação  RN  (reprovado  por  nota); entre  4.0 e menor  que  7.0,  situação  PF  (prova
final) e maior ou igual a 7.0, situação AP (aprovado)."""


def notas(*dados, sit=False):
    aluno_dict = dict()
    aluno_dict["quant"] = len(dados)
    aluno_dict["maior"] = max(dados)
    aluno_dict["menor"] = min(dados)
    soma_das_notas = 0
    for n in dados:
        soma_das_notas += n
    media = soma_das_notas / len(dados)
    aluno_dict["media"] = round(media, 2)
    if sit:
        if media < 4.0:
            aluno_dict["sit"] = "RN"
        elif media < 7.0:
            aluno_dict["sit"] = "PF"
        else:
            aluno_dict["sit"] = "AP"
    return aluno_dict


aluno_1 = notas(7.0, 7.0, 7.0, sit=True)
print(aluno_1)
aluno_2 = notas(5.0, 7.0, 4.0, sit=True)
print(aluno_2)
aluno_3 = notas(2.0, 4.0, 4.0, sit=True)
print(aluno_3)
aluno_4 = notas(7.8, 9.0, 2.3)
print(aluno_4)
