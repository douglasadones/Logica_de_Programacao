"""Crie uma função chamada tipo_voto() que recebe como parâmetro o ano de nascimento de
uma  pessoa  e  retorna  um  valor  literal  (texto)  indicando  se  a  pessoa  tem  voto  NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições. """

from datetime import date


def tipo_voto(nasc):
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 18:
        print("Voto NEGADO")
    elif idade < 70:
        print("Voto OBRIGATÓRIO")
    else:
        print("Voto OPCIONAL")


tipo_voto(2006)



