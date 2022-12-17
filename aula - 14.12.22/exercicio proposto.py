"""Dada as seguintes listas: meses, que representa os meses do ano; vendas1sem e vendas_2sem, que representa
os valores totais das vendas mensais do primeiro e segundo semestre do ano, respectivamente."""

meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19960]
vendas_2sem = [9850, 20120, 17540, 15555, 49051, 19650]

# TODO 1 - Construa um código que mostre o nome do mês e o valor do melhor e pior desempenho em vendas no ano
vendas_ano = vendas_1sem + vendas_2sem  # ou vendas_1sem.extend(vendas_2sem) que evita criar uma outra lista.
maior_venda = vendas_ano.index(max(vendas_ano))  # Pega o índice do maior valor. É também índice do mês correspondente.
menor_venda = vendas_ano.index(min(vendas_ano))
print(f"Melhor mês foi {meses[maior_venda]} com R$ {vendas_ano[maior_venda]}\n"
      f"Pior mês foi {meses[menor_venda]} com R$ {vendas_ano[menor_venda]}")

# TODO 2 - Construa um código que calcula e mostra o faturamento total do ano e quanto que o melhor mês representa em
#  porcentagem do faturament total
faturamento_total = sum(vendas_ano)
porcentagem_melhor_mes = (vendas_ano[maior_venda] * 100) / faturamento_total
print(f'O faturamento total foi de R$ {faturamento_total}')
print(f'O melhor mês representa {porcentagem_melhor_mes:.2f}% do faturamento total')

# TODO 3 - Cria uma lista e coloque nesta o Top 3 ou seja, os três maiores valores mensais de vendas do ano.
#  Observações: (1) Não faça no "Olhômetro" e insira na lista; (2) Não ordenar a lista.
copia_vendas_ano = vendas_ano.copy()  # Cria uma cópia da lista de valores. Objetivo: Alteração segura na estrutura.
TOP = 3  # Quantidade de elementos da lista lista_top_vendas mensais
lista_top_vendas = []
for top in range(TOP):
    maior_valor = max(copia_vendas_ano)
    lista_top_vendas.append(maior_valor)
    copia_vendas_ano.remove(maior_valor)
print(f'Top {TOP} vendas: {lista_top_vendas}')

# TODO 4
for item in range(len(vendas_ano)):
    print(f'{item:>2} {meses[item]}: R$ {vendas_ano[item]:>5}')
print('-' * 16)
print(f'TOTAL: R$ {sum(vendas_ano)}')
