def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    if inicio < fim:
        while inicio <= fim:
            print(inicio)
            inicio += passo

    elif inicio > fim:
        while fim <= inicio:
            print(inicio)
            inicio -= passo

    else:
        print(inicio)


contador(0, 10, 2)
