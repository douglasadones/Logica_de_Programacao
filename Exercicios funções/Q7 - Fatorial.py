"""Crie  uma  função  chamada  fatorial()  que  recebe  dois  parâmetros,  o  número  a  calcular  o
fatorial  e  outra  chamado  show  que  será  um  valor  lógico  (opcional)  indicando  se  será
mostrado ou não na tela o processo de cálculo do fatorial. Ex.: Se número = 4 e show = True
a função mostra fat(4) = 4*3*2*1 = 24; se show for False a função mostra fat(4) = 24. """


def fatorial(num, show):
    fat = 1
    print(f"fat({num}) = ", end="")
    for n in range(num, 0, -1):
        fat *= n
        if show:
            if n != 1:
                print(n, end="*")
            else:
                print("1 = ", end="")
    print(fat)


fatorial(4, False)
fatorial(4, True)


