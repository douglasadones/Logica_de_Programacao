"""Crie um programa que ler o nome, o sexo (M, F ou N) e a data de nascimento de várias
pessoas. Guarde os dados de cada pessoa em um dicionário e guarde cada dicionário em
uma lista. No final mostre: a) Quantas pessoas foram cadastradas; b) A média de idade das
pessoas; c) A relação de pessoas do sexo (F)eminino, do sexo (M)asculino e do sexo (N)ão
informado; e d) A relação das pessoas com idade acima da média."""

from datetime import date

dia_atual = date.today().day
mes_atual = date.today().month
ano_atual = date.today().year

continuar = True
pessoas = dict()
todos_os_cadastros = list()
soma_das_idades = 0

while continuar:
    pessoas["nome"] = input("Informe o nome: ").title()
    pessoas["sexo"] = input("Informe o sexo (M, F ou N): ").upper()
    dia_nascimento = int(input("Informe o dia do seu nascimento: "))
    mes_nascimento = int(input("Informe o mês do seu nascimento: "))
    ano_nascimento = int(input("Informe o ano do seu nascimento: "))
    data_nascimento = f"{dia_nascimento:0>2}/{mes_nascimento:0>2}/{ano_nascimento}"
    pessoas["data_nascimento"] = data_nascimento
    idade = (ano_atual - ano_nascimento) - 1
    if mes_atual <= mes_nascimento and dia_atual <= dia_nascimento:
        idade += 1
    soma_das_idades += idade
    todos_os_cadastros.append(pessoas.copy())
    n = int(input("Adicionar cadastro? (1 para sim, 0 para não): "))
    if n == 0:
        continuar = False

# TODO 1 - a) Mostre quantas pessoas foram cadastradas:
print(f"\nTotal de pessoas cadastradas: {len(todos_os_cadastros)}")

# TODO 2 b) Mostrar a média de idade das pessoas;
media_de_idade = soma_das_idades / len(todos_os_cadastros)
print(f"\nMédia de idade: {int(media_de_idade)}")

# TODO 3 c) Mostrar a relação de pessoas do sexo (F)eminino, do sexo (M)asculino e do sexo (N)ão informado;
sexo_f = 0
sexo_m = 0
sexo_n = 0
for cadastro in todos_os_cadastros:
    if cadastro["sexo"] == "F":
        sexo_f += 1
    elif cadastro["sexo"] == "M":
        sexo_m += 1
    else:
        sexo_n += 1
print(f"\nQuantidade de pessoas do sexo Feminino: {sexo_f}\nQuantidade de pessoas do sexo Masculino: {sexo_m}")
print(f"Sexo não especificado: {sexo_n}")

# TODO 4 d) Mostrar a relação das pessoas com idade acima da média.
print("\nPessoas com a idade acima da média: ")

for cadastro in todos_os_cadastros:
    idade = (ano_atual - int(cadastro["data_nascimento"][6:])) - 1
    if mes_atual <= int(cadastro["data_nascimento"][3:5]) and dia_atual <= int(cadastro["data_nascimento"][0:2]):
        idade += 1
    if idade > media_de_idade:
        print(f"{cadastro['nome']} possui idade acima da média - Idade: {idade}")

