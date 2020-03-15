# -*- coding: utf-8 -*-

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import os.path


meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

if datetime.now().month-2 == -1:
    mes = meses[11]
else:
    mes = meses[datetime.now().month-2]

horas = 180
nfe = 'C:/Users/samug/Downloads/nfe.pdf'

if os.path.isfile(nfe):
    print("\nNota Fiscal (%s)" % mes)
    print("Total de horas: %s\n" % horas)
    confirmar = raw_input("Enviar? [s/n]: ")

    while confirmar.lower() != 's':
        mes = raw_input("\nMês: ")
        horas = raw_input("Total de horas: ")
        print("\nNota Fiscal (%s)" % mes)
        print("Total de horas: %s\n" % horas)
        confirmar = raw_input("Enviar? [s/n]: ")

    try:
        msg = MIMEMultipart()
        password = "Y7zQ1@0P!3"
        msg['From'] = "sagoswins@gmail.com"
        msg['To'] = "mauro.gebrim@waybee.com.br,giancarlo.trentini@waybee.com.br,fabio.simonetti@waybee.com.br"
        msg['Subject'] = "Nota Fiscal ("+str(mes)+")"
        msg.attach(MIMEText("Mês: "+str(mes)+"\nTotal de horas: "+str(horas), 'plain'))
        fp=open(nfe,'rb')
        anexo = MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        anexo.add_header('Content-Disposition','attachment',filename="Nota Fiscal ("+str(mes)+")")
        msg.attach(anexo)
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print("Nota fiscal enviada com sucesso!")
    except Exception as e:
        print("Erro ao enviar: %s" % str(e))
else:
    print("Nota fiscal não foi encontrada.")