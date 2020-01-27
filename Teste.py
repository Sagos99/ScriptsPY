listinha = ['Samuel','Ramos']

first_name = listinha[0]
listinha.pop(0)
last_name = listinha[len(listinha)-1]
listinha.pop(len(listinha)-1)
middle_name = ''

for name in listinha:
    if name != listinha[len(listinha)-1]:
        middle_name += name+' '
    else:
        middle_name += name

print(first_name+' '+middle_name+' '+last_name)