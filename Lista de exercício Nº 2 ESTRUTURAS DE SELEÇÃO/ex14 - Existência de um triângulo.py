"""Escreva um programa que lê 3 números inteiros e verifique se estes podem formar um triângulo, ou seja, a soma de dois
lados tem que ser necessariamente maior que o terceiro lado. Caso os valores formem um triângulo, verificar se é um
triângulo eqüilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes). Imprima uma mensagem
conforme o resultado obtido."""

arestaA = int(input("Informe o tamanho da primeira aresta do triândugo: "))
arestaB = int(input("Informe o tamanho da segunda aresta do triândugo: "))
arestaC = int(input("Informe o tamanho da terceira aresta do triândugo: "))
tipodotriangulo = ""

if (arestaA + arestaB) > arestaC and (arestaA + arestaC) > arestaB and (arestaB + arestaC) > arestaA:
    if arestaA == arestaB == arestaC:
        tipodotriangulo = "Eqüilátero"
    elif arestaA == arestaB or arestaA == arestaC or arestaB == arestaC:
        tipodotriangulo = "Isósceles"
    else:
        tipodotriangulo = "Escaleno"
    print(f"O triângulo informado existe e é do tipo {tipodotriangulo}")
else:
    print("As arestas informadas não formam um triângulo.")
