"""
Tuplas são IMUTÁVEIS
Uma tupla pode ser criada de duas formas: tupla = (1,) ou tupla = 1,
Caso a seja criada como: tupla = (1), esta não será reconhecida como tupla, e sim como int.
"""
tupla = (1,)
print(type(tupla), "com vírgula")

tupla = (10+3)
print(3*tupla, "sem vírgula")

tupla = (10+3,)
print(3*tupla, "com vírgula")

lista = [1, 2, 3]
tupla = (lista,)
print(tupla, "criada a partir de uma lista")


"""
Operador de formatação: %
Formato geral: template % valor
template é uma string entremeada por códigos de formatação.
    Um código de formatação é em geral composto do caractere  seguido de uma letra descritiva do tipo do valor a formatar.
    Ex: s para string f para float, d para inteiro, dentre outros.
    
    "sem template" "notas: {}, {}, {}, média {}".format(n1, n2, n3, media)

Com template:
    "notas: %f, %f, %f, média %f"%(n1, n2, n3, media)
    tipos:
    %a => inteiro ou %i
    %f => float
    %s => string  

podemos tbm informar apenas a tupla:
    tupla = (n1, n2, n3, (n1+n2+n3)/3)
    "notas: %f, %f, %f, média %f"%tupla
    
Dps ver Flags de conversão(opcional):
    - indica alinhamento à esquerda
    + indica que um sinal deve preceder o valor convertido
    "" Indica que um espaço deve preceder número positivos.
    0 indica oreenchimento à esquerda com zeros.
    
Comprimento mínimo do campo(opcional):
    O valor formatado terá este comprimento no mínimo
    Se igual a * (asterisco), o comprimento será lido da tupla

Um "."(ponto) seguido pela precisão(número)(opcional):
    Usado para converter as casas decimais de floats.
    Se aplica para strings, indica o comprimento máximo.
    Se igual a *, o valor será lido da tupla
"""

# Exemplo prático de template:
template = "%s tem %d anos"
tupla = ("Pedro", 10)

print(template % tupla)

"""
Existe um módulo chamado string que contém uma grande quantidade de funcionalidades para trabalhar com strings.
Basta usar: from string import *

find(substring, inicio, fim)
retorna o índice da primeira ocorrência da substring
inicio e fim são opcionais
Caso substring não apareça na string, find() retorna -1.

A diferênça do operador "in" é que O "in" retorna um valor booleano.
"""

s = "quem parte e reparte, fica com a maior parte"
print(s.find("parte"))
print(s.find("reparte"))
print(s.find("parcela"))
print(s.find("parte", 6, 12))

"""
"".join()
"""

s = "/".join(["abc", "def", "ghi"])  # Os itens da tupla/lista devem ser strings.
print(s)

k = "|"
s = k.join(("abc", "def", "ghi"))
print(s)

"""
Métodos: 
    .lower() ou .casefold() - É recomendado usar o .casefold()
    
    .upper()
    
    replace(velho, novo, n) Se n for especificado, apenas n instâncias são trocadas.
    
    split(separador)
    
    .strip() Remove os espaços iniciais e finais caso o caractere n seja informado
        .rstrip() Remove os caracteres à direita da string
        .lstrip() Remove os caracteres à esquerda da string
        
    translate(trans)
        Retorna uma cópia da string onde os caracteres são substituídos de acordo com a tabela de tradução trans
        trans é uma string com 256 caracteres, um para cada possível código de oito bits.
"""

s = "quem parte e reparte, fica com a maior parte"
print(s)

print(s.replace("parte", "parcela"))

s = "xxx yyy zzz xxx zzz"
print(s)
print(s.split())
print(s.split("xxx"))

s = "xxx yyy zzz xxx"
print(s)
print(s.strip("xy "))  # removerá os caracteres "x", "y" e " ".
