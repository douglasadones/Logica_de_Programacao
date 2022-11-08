# Programa: Usuário dará dois números e escolherá a operação desejada. Obs: Usar apenas if, elif e else.
print("Calculadora")
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
operacao = int(input("""Escolha uma das operações abaixo:
1 para Somar;
2 para Subtrair;
3 para Multiplicar;
4 para Dividir (Caso possível).
Faça a sua escolha: """))

if operacao == 1:
    print(f"O resultado da soma  entre {n1} e {n2}é: {n1 + n2}")
elif operacao == 2:
    print(f'O resultado da subtração entre {n1} e {n2} é: {n1 - n2}')
elif operacao == 3:
    print(f'O resultado do produto entre {n1} e {n2} é: {n1 * n2}')
else:
    print(f'O resultado da divisão entre {n1} e {n2} é: {n1 / n2:.2f}')
print('Programa finalizado.')
