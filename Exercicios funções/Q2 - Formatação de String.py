"""Crie uma função chamada escrever() que recebe como parâmetro um texto qualquer como
parâmetro e mostra  três mensagens  conforme a  seguir: a) A  primeira mensagem imprime
uma  linha  (conjunto  de  hifens)  do  mesmo  tamanho  do  texto  recebido.  b)  A  segunda
mensagem imprime o texto recebido. c) A terceira mensagem deve ser a mesma o item (a).
A  quantidade  de  hifens  deve  ser  a  mesma  quantidade  de  caracteres  do  texto. """


def escrever(msg):
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))


mensagem = input("Digite uma mensagem: ")
escrever(mensagem)
