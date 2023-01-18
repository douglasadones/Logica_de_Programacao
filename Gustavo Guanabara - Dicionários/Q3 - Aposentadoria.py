"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Admita 35 anos de contr. para aposentadoria."""

from datetime import datetime

data = datetime.now()
ano_atual = data.year

pessoa_fisica = dict()
pessoa_fisica["nome"] = input("Nome: ")
pessoa_fisica["nascimento"] = int(input("Ano de Nascimento: "))
pessoa_fisica["idade"] = (pessoa_fisica["nascimento"] - ano_atual) * (-1)

ctps = int(input("Carteira de Trabalho (0 não tem): "))
if ctps != 0:
    pessoa_fisica["contratação"] = int(input("Ano de Contratação: "))
    pessoa_fisica["salário"] = float(input("Salário: "))



