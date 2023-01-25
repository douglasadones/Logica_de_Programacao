"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Admita 35 anos de contr. para aposentadoria."""

from datetime import datetime

ano_atual = datetime.now().year

pessoa_fisica = dict()
pessoa_fisica["Nome"] = input("Nome: ")
pessoa_fisica["Nascimento"] = int(input("Ano de Nascimento: "))
pessoa_fisica["Idade"] = (pessoa_fisica["Nascimento"] - ano_atual) * (-1)

ctps = int(input("Carteira de Trabalho (0 não tem): "))
if ctps != 0:
    pessoa_fisica["Contratação"] = int(input("Ano de Contratação: "))
    pessoa_fisica["Salário"] = float(input("Salário: "))
    ano_da_aposentadoria = pessoa_fisica["Contratação"] + 35
    idade_para_aposentadoria = ano_da_aposentadoria - pessoa_fisica["Nascimento"]
    pessoa_fisica["Aposentadoria"] = idade_para_aposentadoria

print("\nDetalhes Do Cadastro")

for k, v in pessoa_fisica.items():
    print(f"{k}: {v}")
