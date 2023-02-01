"""Crie uma função chamada leiaInt() que vai  funcionar de forma semelhante a função input()
do  Python,  só  que  fazendo  a  validação  para  aceitar  apenas  um  valor  numérico  inteiro.
Exemplo de protótipo: n = leiaInt(“Informe um número: ”)"""


def leiaInt():
    while True:
        n = input("Informe um número inteiro: ")
        if not(n.isnumeric() and "." not in n):
            print("Por favor informe um número inteiro!")
        else:
            print("Número Válido!")
            return int(n)


n = leiaInt()
print(f"Número informado: {n}, Típo informado: {type(n)}")
