from datetime import datetime
from time import sleep
import pyperclip


begin = input('Tempo da task: ')
desc = None

if len(begin) == 13:
    end = begin.split(' ~ ')[1]
    begin = begin.split(' ~ ')[0]
elif len(begin) > 15:
    end = begin[9:14]
    desc = begin[16:]
    begin = begin[1:6]
else:
    end = input('Fim da task: ')
    
formato = '%H:%M'

if not end:
    end = datetime.strftime(datetime.today(), formato)

try:
    calc = datetime.strptime(end, formato) - datetime.strptime(begin, formato)
    seconds = calc.seconds
except:
    seconds = 0

hours = 0
minutes = 0

while seconds >= 60:
    seconds -= 60
    minutes += 1

while minutes >= 60:
    minutes -= 60
    hours += 1

if hours < 10:
    hours = '0'+str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = '0'+str(minutes)
else:
    minutes = str(minutes)

print('\nTempo nesta task: '+hours+':'+minutes)

if desc:
    print('Descrição: '+desc)
    pyperclip.copy(desc)
    sleep(8)

pyperclip.copy(hours+':'+minutes)