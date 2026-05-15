from datetime import datetime, timedelta
import calendar

dias_semana: tuple = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
br_format: str = "%d-%m-%Y"
feriados: tuple = (datetime(2026,4,20).strftime(br_format),)
dia_semana: list = [0,1] # segunda e terça
data_inicio: datetime = datetime.today()
data_termino: datetime = datetime(2026, 6, 30)
intervalo: timedelta = data_termino - data_inicio


dias: int = 0 # contador de dias
for d in range(intervalo.days):
    if data_inicio.weekday() in dia_semana and data_inicio.strftime(br_format) not in feriados:
        dias += 1
        print(f"Dias {dias}, data: {data_inicio}")
    data_inicio += timedelta(days=1)
    
print(f"""
    Dia da semana: {dia_semana}
    Data de Inicio: {data_inicio.strftime(br_format)}
    Data Termino: {data_termino.strftime(br_format)}
    Iintervalo: {intervalo}
    Semanas: 
    1 dia: {dias_semana[data_inicio.weekday()], data_inicio.month}
""")