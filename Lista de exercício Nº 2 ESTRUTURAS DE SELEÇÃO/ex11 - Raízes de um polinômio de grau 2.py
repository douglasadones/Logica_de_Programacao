"""Dados os números reais a, b e c determine as raízes da equação de segundo grau ax² + bx + c = 0 indicando se as raízes
são reais ou complexas. Considere também o caso em que a = 0."""

from math import sqrt

print("Calculadora de raízes de polinômios do 2° grau")
a = float(input("Valor do coeficiente \"a\": "))
b = float(input("Valor do coeficiente \"b\": "))
c = float(input("Valor do coeficiente \"c\": "))

delta = b**2 - 4*a*c
raiz1 = 0
raiz2 = 0
if a != 0:
    if delta > 0:  # Duas Raizes
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print(f"O polinômio ({a})x² + ({b})x + ({c}) possui duas raízes reais: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}")
    elif delta == 0:  # Uma Raíz
        raiz1 = (-b + sqrt(delta)) / 2 * a
        print(f"O polinômio ({a})x² + ({b})x + ({c}) possui uma raíz real: x1 = {raiz1:.2f}")
    else:  # Nenhum Raíz Real
        print(f"O polinômio ({a})x² + ({b})x + ({c}) Não possui raízes reais.")
else:
    print("O coeficiente \"a\" de um polinômio de grau 2 deve ser diferente de 0.")