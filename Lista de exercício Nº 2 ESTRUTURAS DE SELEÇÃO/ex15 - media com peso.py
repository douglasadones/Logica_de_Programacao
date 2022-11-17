"""Em uma disciplina são realizadas quatro provas. As duas primeiras notas tem peso 1 e as duas últimas peso 2. O aluno que
obtém média 7,0 ou superior é aprovado. Se a média for inferior a 7,0 e superior ou igual a 2,5 o aluno está de exame final.
Se a média for inferior a 2,5 o aluno está reprovado. Além das notas é considerada também a freqüência do aluno que deve
ser maior ou igual a 75% para que ele não reprove por falta. Faça um programa que lê a freqüência do aluno, o número
total de aulas e as quatro notas, calcule a média e imprima junto com uma mensagem que indique a situação do aluno:
“aprovado”, “exame final”, “reprovado por nota” ou “reprovado por falta”."""

from math import ceil  # Arredondado para cima.

PESO1 = 1
PESO2 = 1
PESO3 = 2
PESO4 = 2

totaldeaulas = int(input("Informe o total de aulas: "))
frequencia = int(input("Informe quantas aulas o aluno participou: "))
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
nota4 = float(input("Informe a quarta nota do aluno: "))
frequenciaminima = ceil(totaldeaulas * (75/100))
media = round((nota1 * PESO1 + nota2 * PESO2 + nota3 * PESO3 + nota4 * PESO4) / (PESO1 + PESO2 + PESO3 + PESO4),
              ndigits=1)
print(f"Média: {media} - Situação: ", end="")
if frequencia >= frequenciaminima:
    if media >= 7.0:
        print("Aprovado!")
    elif media >= 2.5:
        print("Exame Final")
    else:
        print("Reprovado Por Nota")
else:
    print("Reprovado por falta")
