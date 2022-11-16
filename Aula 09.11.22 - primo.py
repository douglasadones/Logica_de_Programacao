# Programa que mostre todos os números primos até o número informado pelo usuário

m = int(input("Digite um número inteiro positivo: "))
n = 3
print("2", end=" ")
while n <= m:
    ehprimo = True
    i = 2
    while i <= n // 2:
        if n % i == 0:
            ehprimo = False
            break
        i += 1
    if ehprimo:
        print(f"{n}", end=" ")
    n += 2