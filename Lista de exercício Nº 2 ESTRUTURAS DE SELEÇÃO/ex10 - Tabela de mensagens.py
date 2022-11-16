"""Escreva um programa que leia um caractere do teclado e forneça na tela uma das seguintes mensagens:
A ou a Alteração, C ou c Consulta, E ou e Exclusão, I ou i Inclusão, F ou f Finalização, Outro Opção inválida"""

c = input("""Digite algum dos caracteres a seguir: 
A ou a;
C ou c;
E ou e;
I ou i;
F ou f.
Sua resposta: """).lower()

if c == "a":
    print("Alteração")
elif c == "c":
    print("Consulta")
elif c == "e":
    print("Exclusão")
elif c == "i":
    print("Inclusão")
elif c == "f":
    print("Finalização")
else:
    print("Opção Inválida.")