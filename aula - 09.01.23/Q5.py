"""Dado o conjunto de vendedores de uma loja com seus respectivos valores de vendas do mês (conforme
quadro ao lado) e o valor de R$ 1000,00 que corresponde a meta mensal a ser atingida.
Construa um código que:
a) Mostra quantos vendedores atingiram a meta mensal e a
porcentagem desse total;
b) Mostra o nome de todos os vendedores que atingiram a meta;
c) Mostra o nome de todos os vendedores que atingiram a meta e
seus valores atingidos;
d) Mostra a mensagem “<Fulano>, seja mais produtivo!” para os
vendedores que não atingiram a meta mensal (“Fulano” é o nome
do vendedor)."""

meta = 1000
vendas = [
    ["joao", 1673],
    ["maria", 987],
    ["jose", 8812],
    ["ana", 177],
    ["ivo", 224],
    ["eva", 1758],
    ["ely", 1935],
    ["dalva", 876]
    ]

quantidade = 0
maior = 0
vendedor = ""
for item in vendas:
    if item[1] > maior:
        maior = item[1]
        vendedor = item[0]
    if item[1] >= 1000:
        quantidade += 1
        print(f"{item[0]} vendeu {item[1]}, atingiu a meta.")
    else:
        print(f"{item[0]}, seja mais produtivo.")
percent = quantidade / len(vendas)
print(f"{quantidade} vendedores ({percent:.2%}) atingiram a meta.")
print(f"{vendedor} vendeu R${maior}, foi o melhor vendedor.")
