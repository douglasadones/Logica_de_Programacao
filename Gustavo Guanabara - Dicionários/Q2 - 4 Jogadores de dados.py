"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep

numero_de_jogadores = 4
jogadores_e_numeros_obtidos = {}

print("Valores Sorteados:")
for jogador in range(1, numero_de_jogadores + 1):
    numero = randint(1, 6)
    jogadores_e_numeros_obtidos[f"jogador{jogador}"] = numero
    print(f"\tO jogador{jogador} tirou {numero}")
    sleep(0.8)

jogadores = [k for k in jogadores_e_numeros_obtidos.keys()]
numeros = [v for v in jogadores_e_numeros_obtidos.values()]
jogadores_e_numeros_obtidos.clear()

list_to_dict = []

for valor in range(numero_de_jogadores):
    maior = (numeros.index(max(numeros)))
    tupla_temporaria = (jogadores[maior], numeros[maior])
    list_to_dict.append(tupla_temporaria)
    numeros.pop(maior)
    jogadores.pop(maior)
jogadores_e_numeros_obtidos = dict(list_to_dict)

print("Ranking dos jogadores:")
rank = 1
for v, k in jogadores_e_numeros_obtidos.items():
    print(f"\t{rank}º lugar: {v} com {k}")
    rank += 1
    sleep(0.8)


