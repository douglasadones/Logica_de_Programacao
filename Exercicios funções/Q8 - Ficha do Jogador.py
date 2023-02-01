"""Crie  uma  função  chamada  ficha()  que  recebe  dois  parâmetros  opcionais:  o  nome  de  um
jogador e quantos gol ele marcou. O programa deve mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente"""


def ficha(nome="Não Informado", gols="Não informado"):
    print(f"Nome do jogador: {nome}")
    print(f"Gols Marcados: {gols}")


ficha("João", 10)
print()
ficha(nome="Mendes")
print()
ficha(gols=12)
