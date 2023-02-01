"""Aprimore o exercício 4 (aproveitamento do jogador de futebol) para que ele armazene e
gerencie os dados e produza resultados para vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento individual dos jogadores."""

aproveitamento_individual = dict()
cadastros = list()
continuar = True

while continuar:
    # Obtenção de dados
    aproveitamento_individual["nome"] = input("Nome do jogador: ").title()
    aproveitamento_individual["partidas"] = int(input("Partidas jogadas: "))

    gols_por_partida = []
    for jogos in range(1, aproveitamento_individual["partidas"] + 1):
        g = int(input(f"Gols feitos na {jogos}ª partida: "))
        gols_por_partida.append(g)
    aproveitamento_individual["gols"] = gols_por_partida
    cadastros.append(aproveitamento_individual.copy())
    continuar = int(input("Deseja adicionar mais um jogador? (0 para não, 1 para sim):  "))
if sum(aproveitamento_individual["gols"]) == 0:
    aproveitamento_individual["gols"] = "Nenhum Gol Feito."


# Sistema de vizualização individual dos jogadores
continuar_vizualizando = True
while continuar_vizualizando:
    print(f"\nVizualização individual de cadastro: ")
    for n, jogador in enumerate(cadastros):
        print(f"{n}.", jogador["nome"])
    vizualizacao = int(input(f"Escolha de 0 a {len(cadastros) - 1} (-1 para encerrar): "))

    if vizualizacao == - 1:
        break

    print("")
    for key, value in cadastros[vizualizacao].items():
        if key != "gols":
            print(f"{key.capitalize()}: {value}")
        else:
            if aproveitamento_individual["gols"] != "Nenhum Gol Feito.":
                print(f"{key.capitalize()} por partida: ", end="")
                for c in aproveitamento_individual["gols"]:
                    print(f"{c}", end=", " if aproveitamento_individual["gols"].index(c) !=
                                              len(aproveitamento_individual["gols"]) - 1 else ".\n")
            else:
                print(f"{key.capitalize()} por partida: {aproveitamento_individual['gols']}")
                break


