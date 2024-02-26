#-*- coding: utf-8 -*-

# Leia-se do arquivo datetime
# importe a classe date
from datetime import date

# Data simples
hoje = "25/07/2023"
print(type(hoje), hoje)
hoje = date.today()
print(type(hoje), hoje)
print(f"Hoje é dia {hoje.day} \
       de {hoje.month} de {hoje.year}")
dias = ('Segunda-feira', 'Terça-feira'
        , 'Quarta-feira', 'Quinta-feira'
        , 'Sexta-feira', 'Sábado'
        , 'Domingo')
print(f"{hoje.weekday()} {hoje}")