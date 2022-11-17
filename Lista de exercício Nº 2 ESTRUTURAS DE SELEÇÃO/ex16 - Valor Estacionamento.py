"""Um estacionamento cobra R$ 2,50 por cada hora ou fração de permanência de um veículo. Escreva um programa que lê os
horários de entrada e saída de um veículo (hora e minuto) e calcule o total a ser pago. Se o veículo permanece por mais de
quatro horas no estacionamento, ele ganha uma lavagem grátis. O seu programa deve informar ao usuário se isto ocorrer."""

horaentrada = int(input("Informe o horário de entrada do veículo (horas): "))
minutoentrada = int(input("Informe o horário de entrada do veículo (minutos): "))
horasaida = int(input("Informe o horário de saída do veículo (horas): "))
minutosaida = int(input("Informe o horário de saída do veículo (minutos): "))
lavagemgratis = False

horasnoestacionamento = 0

if horasaida - horaentrada > 1:  # Verificação unicamente por horas
    horasnoestacionamento = (horasaida - horaentrada) - 1

if horaentrada > horasaida:  # Verificando o caso 00:00
    horasnoestacionamento = (24 - (abs(horaentrada - horasaida))) - 1  # - 1 deixa a verificação da última hora para os minutos.

if horaentrada != horasaida:  # Verificação por minutos
    if minutoentrada <= minutosaida:
        horasnoestacionamento += 1
    if horasnoestacionamento >= 4:
        lavagemgratis = True

print(f"Horário de entrada: {horaentrada:0>2}:{minutoentrada:0>2}", " (Dia 1)" if horaentrada > horasaida else "")
print(f"Horário de saída: {horasaida:0>2}:{minutosaida:0>2}", " (Dia 2)" if horaentrada > horasaida else "")
print(f"Total de horas no estacionamento: {horasnoestacionamento}", "hora." if horasnoestacionamento == 1 else "horas.")
if lavagemgratis:
    print("Você tem direito a uma lavagem grátis!")
else:
    print("Você ainda não possui direito a uma lavagem grátis. (Atinja 4 horas ou mais no estacionamento)")
