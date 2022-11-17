"""Um estacionamento cobra R$ 2,50 por cada hora ou fração de permanência de um veículo. Escreva um programa que lê os
horários de entrada e saída de um veículo (hora e minuto) e calcule o total a ser pago. Se o veículo permanece por mais de
quatro horas no estacionamento, ele ganha uma lavagem grátis. O seu programa deve informar ao usuário se isto ocorrer."""

entrada = int(input("Informe o horário de entrada do veículo (horas): ")) * 60
entrada += int(input("Informe o horário de entrada do veículo (minutos): "))
saida = int(input("Informe o horário de saída do veículo (horas): ")) * 60
saida += int(input("Informe o horário de saída do veículo (minutos): "))
lavagemgratis = False

if saida >= entrada:
    tempototalnoestacionamento = saida - entrada
else:
    tempototalnoestacionamento = abs((entrada - saida) - (24 * 60))

if tempototalnoestacionamento > 240:
    lavagemgratis = True

print(f"Horário de entrada: {entrada // 60:0>2}:{entrada % 60:0>2}", "(Dia 1)" if saida < entrada else "")
print(f"Horário de saída: {saida // 60:0>2}:{saida % 60:0>2}", "(Dia 2)" if saida < entrada else "")
print(f"Total de horas no estacionamento: {tempototalnoestacionamento // 60:0>2}:{tempototalnoestacionamento % 60:0>2}")
print(f"Você deve pagar um total de R${(tempototalnoestacionamento // 60) * 2.5:.2f}")
if lavagemgratis:
    print("Você tem direito a uma lavagem grátis!")
else:
    print("Você ainda não possui direito a uma lavagem grátis. (Permaneça por mais de 4 horas no estacionamento)")
