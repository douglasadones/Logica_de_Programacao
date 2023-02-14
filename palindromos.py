# Douglas Adones de Souza Nascimento, Miguel Angelo Assunção Veras Carvalho

continuar = True

while continuar:
    casos = int(input(""))
    if casos != 0 and 1 <= casos <= 100:
        for n in range(casos):
            num = int(input(""))
            if 1 <= num <= 100000000:
                num_str = str(num)
                if num_str == num_str[::-1]:
                    print("palindromo")
                else:
                    print("nao‐palindromo")
            else:
                break
        print("")
    else:
        continuar = False
