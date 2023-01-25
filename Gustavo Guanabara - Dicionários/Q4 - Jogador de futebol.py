"""Crie  um  programa  que  gerencia  o  aproveitamento  de  um  jogador  de  futebol  em  um
determinado  campeonato. O  programa  deve lê  o  nome  do jogador e quantas  partidas ele
jogou.  Em  seguida,  o  programa  deve  lê a  quantidade  de  gols  feitos  pelo  jogador em  cada
partida. Todos os dados devem ser guardados em um dicionário. No  final, mostre todos os
dados armazenados no dicionário."""

aproveitamento_individual = {}

aproveitamento_individual["Nome"] = input("Nome do jogador: ")
aproveitamento_individual["Partidas"] = int(input("Partidas jogadas: "))

gols_por_partida = []
for jogos in range(1, aproveitamento_individual["Partidas"] + 1):
    g = int(input(f"Gols feitos na {jogos}ª partida: "))
    gols_por_partida.append(g)
aproveitamento_individual["Gols"] = gols_por_partida

for k, v in aproveitamento_individual.items():
    if k != "Gols":
        print(f"{k}: {v}")
    else:
        print(f"{k} por partida: ", end="")
        for c in aproveitamento_individual["Gols"]:
            print(f"{c}", end=", " if aproveitamento_individual["Gols"].index(c) !=
                                      len(aproveitamento_individual["Gols"]) - 1 else ".")
