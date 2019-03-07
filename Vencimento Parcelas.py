# -*- coding: utf-8 -*-

from datetime import datetime,date
from dateutil.relativedelta import relativedelta


date_format = '%Y-%m-%d %H:%M:%S'


dia = 15

#data_atual = date.today()
data_atual = date(year=2019, month=6, day=7) # Data para testes

data_vencimento = date(year=data_atual.year, month=data_atual.month, day=dia)

print('Dia atual: '+str(data_atual.day))

calc = (data_vencimento-data_atual).days

if data_atual.month >= 10:
    vencimento = date(year=data_atual.year+1, month=1, day=dia).strftime(date_format)
    print('Vencimento: '+str(vencimento))
else:
    if calc > 7:
        vencimento = date(year=data_atual.year, month=data_atual.month, day=dia).strftime(date_format)
        print('Vencimento: '+str(vencimento))
    else:
        vencimento = date(year=data_atual.year, month=data_atual.month+1, day=dia).strftime(date_format)
        print('Vencimento: '+str(vencimento))