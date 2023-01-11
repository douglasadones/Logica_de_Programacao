"""Digamos que você está analisando as vendas de produtos de uma empresa de e‐commerce e quer
identificar quais os produtos tiveram no ano de 2022 mais vendas do que no ano de 2021, para reportar
o fato à diretoria da empresa. Você pode elaborar um relatório com cada produto, suas respectivas
vendas de 2021, vendas de 2022 e a porcentagem (%) de crescimento de vendas de 2022 em relação a
vendas de 2021. Dica: se desejar, utilize a função enumerate() para facilitar o uso do for‐in. Segue
exemplo de dados de entrada:"""

produtos = ["tv", "iphone", "kindle", "mac", "pc", "ssd", "ipad", "memoria", "notebook", "adega", "galaxy", "motorola"]
vendas2021 = [558147, 712350, 573823, 718654, 531580, 973139, 405252, 892292, 422760, 154753, 887061, 438508]
vendas2022 = [951642, 244295, 26964, 787604, 867670, 78830, 710331, 646016, 644913, 539704, 324831, 667179]

for i, produto in enumerate(produtos):
    if vendas2022[i] > vendas2021[i]:
        porcentagem = (vendas2022[i] - vendas2021[i]) / vendas2021[i]
        print(f"{produto}, cresceu {porcentagem:.2%} em vendas")
