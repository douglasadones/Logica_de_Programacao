continuar = True
while continuar:
    matriz = []

    # Obtendo dados

    m = int(input(""))
    n = int(input(""))
    if m != 0 and n != 0 and m <= 100 and n <= 100:

        # Armazenando os dados como uma matriz

        for l in range(m):
            linha = []
            for c in range(n):
                e = int(input(""))
                linha.append(e)
            matriz.append(linha)

        # Criando lista com elementos reordenados (girados em 90°) Ainda sem formato de matriz (lista dentro de lista)

        matriz_inversa = matriz[::-1]
        elementos_da_matriz = []
        for i in range(n):
            matriz_momentanea = []
            for e in matriz_inversa:
                elementos_da_matriz.append(e[i])

        # Formatando a lista de elementos reordenados para o formato de matriz (lista dentro de lista)

        geral = []
        for i in range(n):
            lista_temporaria = []
            for c in range(m):
                lista_temporaria.append(elementos_da_matriz[c])
            geral.append(lista_temporaria)
            for k in range(m):
                elementos_da_matriz.pop(0)

        # Mostrando para o usuário a lista após o giro de 90°

        for linha in geral:
            for p, elem in enumerate(linha):
                if p != len(linha) - 1:
                    print(elem, end=" ")
                else:
                    print(elem, end="\n")
        print("")
    else:
        continuar = False
