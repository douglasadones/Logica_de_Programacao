"""Dado  o  conjunto  de  produtos  que  são  vendidos  numa  loja  e  seus  respectivos  valores  em  estoque,
construa um código que controla o estoque, não permitindo que a quantidade em estoque fique abaixo
do  limite  (5  unidades).  Sempre  que  executado  o  programa  mostra  a  lista  dos  produtos  e  o  valor  em
estoque dos itens que estão abaixo do limite de estoque. Segue exemplo de dados de entrada:"""

limite = 5
produtos = ["tv", "iphone", "kindle", "mac", "pc", "ssd", "ipad", "memoria"]
estoque = [4, 10, 8, 7, 2, 18, 5, 12]
for i, valor in enumerate(estoque):
    if valor < limite:
        print(f"{produtos[i]}: {valor}")
