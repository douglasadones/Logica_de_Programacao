"""Dado o conjunto de vendedores de uma loja, o conjunto de seus respectivos valores de vendas do mês e
o valor de R$ 1000,00 que corresponde a meta mensal a ser atingida, construa um código que:
a) Mostra quantos vendedores atingiram a meta mensal e a porcentagem desse total;
b) Mostra o nome de todos os vendedores que atingiram a meta;
c) Mostra o nome de todos os vendedores que atingiram a meta e seus valores atingidos;
d) Mostra a mensagem “<Fulano>, seja mais produtivo!” para os vendedores que não atingiram a meta
mensal (“Fulano” é o nome do vendedor).
Segue exemplo de dados de entrada:"""

meta = 1000
vendedores = ["joao", "maria", "jose", "ana", "ivo", "eva", "ely", "dalva"]
valores = [1673, 987, 8812, 177, 224, 1758, 1935, 876]

quantidade = 0
for valor in valores:
    if valor >= meta:
        quantidade += 1
porcentagem = quantidade / len(valores)
print(f"{quantidade} vendedores, {porcentagem: .2%} atingiram a meta")

for i, valor in enumerate(valores):
    if valor >= meta:
        print(f"{vendedores[i]}, vendeu R${valor:.2f}, atingiu a meta.")
    else:
        print(f"{vendedores[i]}, seja mais produtivo(a)")

maior = max(valores)
print(f"{vendedores[valores.index(maior)]} foi o melhor vendedor.")
