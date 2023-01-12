# Escrever um programa que leia três valores inteiros e apresente o menor dos valores lidos.

# Modo preguiçoso:
listadevalores = []
for valores in range(1, 4):
    valor = int(input(f"Digite o {valores}º valor: "))
    listadevalores.append(valor)
print(f"O menor valor entre {listadevalores[0]}, {listadevalores[1]} e {listadevalores[2]} é: ", end="")
listadevalores.sort()
print(listadevalores[0])


# Modo menos preguiçoso:
menorvalor = 0
for valores in range(1, 4):
    valor = int(input(f"Digite o {valores}º valor: "))
    listadevalores.append(valor)
    if valores == 1:
        menorvalor = valor
    else:
        if valor < menorvalor:
            menorvalor = valor
print(f'O menor valor entre ', end="")
print(*listadevalores, sep=", ", end=" ")
print(f"é: {menorvalor}")
