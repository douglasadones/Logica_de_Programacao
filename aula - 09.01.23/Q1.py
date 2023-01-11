"""A  você  foi  atribuído  o  desenvolvimento  de  um  sistema  de  controle  de  um  hotel/pousada.  Sua  tarefa
atual é  construir a  sub‐rotina  de  registro  de  chegada  dos  hóspedes. O  hotel  possui  seus  quartos  com
capacidade para 1, 2, 3 e/ou 4 pessoas. Sua tarefa será:
a) Fazer a sub‐rotina lê a quantidade de pessoas que serão hospedadas no quarto (1, 2, 3 e/ou 4);
b) De acordo com a quantidade de pessoas informadas, lê o nome e o CPF de cada pessoa, a  fim de
registrá‐la no quarto;
c) Gerar uma listagem contendo o nome e o CPF das pessoas registradas naquele quarto. """

quantidade = int(input("informe a quantidade de hóspedes: "))
quarto = []
if 1 <= quantidade <= 4:
    for i in range(quantidade):
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        quarto.append([nome, cpf])
else:
    print("Quantidade de hóspedes inválida!!")
print("\nPessoas hospedadas no quarto: ")
for pessoa in quarto:
    print(f"nome: {pessoa[0]}, CPF: {pessoa[1]}")


