import shutil
import os

where = input('Diretório da nova model: ')
model_technical_name = input('Nome técnico da model: ')
author = input('Autor da model: ')
model_name = input('Nome da model: ')
description = input('Descrição da model: ')
icon = 'icon.png'

model_technical_name += '/'
if where[len(where)-1] != '/':
    where += '/'

folders = [
    'data',
    'i18n',
    'models',
    'security',
    'static',
    'static/description',
    'static/src',
    'static/src/img',
    'static/src/js',
    'views']


# Criando todas as pastas necessárias
for folder in folders:
    os.makedirs(where+model_technical_name+folder)


# Criando o __init__.py
init = open(where+model_technical_name+'__init__.py', 'w')
init.write('from . import models')
init.close()

# Criando o __manifest__.py
manifest = open(where+model_technical_name+'__manifest__.py', 'w')
manifest.write('''{
    'name' : "'''+model_name+'''",
    'summary': "'''+model_name+'''",
    'version' : "1.0",
    'description' : """
    '''+description+'''
""",
    'author': "'''+author+'''",
    'depends': [],
    'data': [],
    'installable' : True,
    'auto_install' : True,
    'currency': 'BRL',
}''')
manifest.close()

# Adicionando ícone nova nova model
if icon:
    shutil.copyfile(icon, where+model_technical_name+'static/description/'+icon)

print('Model criada com sucesso.')