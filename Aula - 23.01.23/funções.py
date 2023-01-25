"""
Abstração - Técnica de programação que nos permite pensar num problema em diversos níveis.

Caso o return de uma função não seja especificado, será retornado "None"
Ex:
    def soma():
        return
    print(soma())  # será printado: "None"

    def funcao():
        print("Olá, tudo bem?")
    print(funcao())  # Retornadará:  Olá, tudo bem? e None


    def funcao2(nome):  # nome é um parâmetro/argumento formal
        c = 3

    funcao2("Joao")  # "Jogao" é um parâmetro/argumento real


Obs: Os parâmetros opcionais das funções, sempre devem ser os últimos.
ex:
    def funcao3(nome, idade, est_civil="solteiro/a"):
        comandos

"""
