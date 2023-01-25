def mostrar(*b):  # b armazena em uma tupla
    print(b)


def mostrar_2(**c):  # c armazena um dicionário e para isso precisamos da sintaxe: a="asdn", b=211 e etc...
    print(c)


b = 1, 2, 3, 4
mostrar(b)

mostrar_2(a="oi", b=123)

