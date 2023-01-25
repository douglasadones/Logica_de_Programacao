def mostrar(a):
    print("\n## Dados do Aluno ##")
    print(f"Nome: {a['nome']}\nNota 1: {a['n1']}\nNota 2: {a['n2']}\nNota 3: {a['n3']}")


aluno = dict()
aluno["nome"] = input("Nome: ")
aluno["n1"] = float(input("Nota 1: "))
aluno["n2"] = float(input("Nota 2: "))
aluno["n3"] = float(input("Nota 3: "))
mostrar(aluno)
