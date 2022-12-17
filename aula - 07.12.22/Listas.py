"""
Forma "correta" (indicada) de inicialização de uma lista:
Ex:
vetor = [0] * 10  # Lista com dez elementos (iguais a 0)
print(vetor)
Dessa forma, poderemos por exemplo: lista[0] = 3.

A forma ainda mais indicada é inicializá-la dessa forma:
vetor = [None] * 10  # Lista nula, sem nenhum tipo específico.
print(vetor)

Função List:
lista = list('UESPI PHB')  # Mesma função do split.
print(lista)

Forma diferente de usar o Join:
print('UESPI'.join(['P', 'H', 'B']))

Podemos usar o range() para criar listas completas:
lista = range(10)  # resultado do comando: lista == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Lembrando que o range() possui 3 parâmetros parecidos com os do slice.

Prova dia 21.

"""
