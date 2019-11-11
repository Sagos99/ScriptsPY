from datetime import datetime



begin = input('Início da task: ')
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


print('\nTempo da task: '+hours+':'+minutes)