"""
Sobre data em python:
formato da representação: "2023-02-01" ou "20230201"
Métodos:
    from datetime import datetime, date
    date.strptime("sep-22-2021","%b%d%Y")
    date.strftime("01/02/2023")


Convertendo string para date:
    strdate = '11/07/2023'
    date = datetime.strptime(str_date, '%d/%m/%Y').date()
    ou
    strdate = '11-07-2023'
    date = datetime.strptime(str_date, '%Y-%m-%d').date()
    ou
    strdate = 'sep-22-2021'
    date = datetime.strptime(str_date, '%b-%d-%Y').date()  # '%b' pois o mês está na forma abreviada.


    Verificando a idade de uma pessoa com date:
    date_nasc = "20/01/2000"
    hoje = date.today()
    datetime.strptime(date_nasc, "%d/%m/%Y).date()  # O .date() remove a hora mantendo apenas a data.
    print(f"Nascimento: {date_nasc}")
    print(f"Hoje......: {hoje}")
"""
