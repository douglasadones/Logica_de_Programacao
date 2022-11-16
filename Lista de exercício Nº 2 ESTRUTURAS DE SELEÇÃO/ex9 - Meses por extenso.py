# Escreva um programa que apresente o mês por extenso, a partir de um número digitado pelo usuário (entre 1 e 12).
mesesdicionario = {
    '1': "Janeiro",
    '2': "Fevereiro",
    '3': "Março",
    '4': "Abril",
    '5': "Maio",
    '6': "Junho",
    '7': "Julho",
    '8': "Agosto",
    '9': "Setembro",
    '10': "Outubro",
    '11': "Novembro",
    '12': "Dezembro",
}

meseslista = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
              "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Usando dicionário:
n = int(input("Digite um número entre 1 e 12 para ver o mês correspondente: "))
print(f"O mês correspondente a {n} é {mesesdicionario[str(n)]}")

# Usando lista:
n = int(input("Digite um número para ver o mês correspondente: "))
print(f"O mês correspondente a {n} é {meseslista[n - 1]}")
