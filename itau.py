#!/Users/dudus/Work/pyboleto/venv/bin/python
# -*- coding: utf-8 -*-

import datetime

import pyboleto
from pyboleto.bank.itau import BoletoItau
from pyboleto.pdf import BoletoPDF


def print_teste_boleto(boleto, banco_nome):
    # Caixa Formato normal - uma pagina por folha A4
    pdf = BoletoPDF('boleto-%s-mobile-teste.pdf' % banco_nome)
    for i in range(2):
        pdf.drawBoleto(boleto)
        pdf.nextPage()
    pdf.save()

    # Formato carnê - uma pagina por folha A4
    # pdf = BoletoPDF('boleto-%s-formato-carne-teste.pdf' % banco_nome, True)
    # for i in range(2):
    #     pdf.drawBoletoCarneDuplo(boleto, boleto)
    #     pdf.nextPage()
    # pdf.save()


def print_itau():
    d = BoletoItau()
    d.carteira = '109'
    d.cedente = 'MÓBILE CURSOS OPCIONAIS LTDA - CCM: 3.293.299-5 CNPJ: 06.124.009/0001-90'
    d.cedente_documento = "102.323.777-01"
    d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
    d.agencia_cedente = '1565'
    d.conta_cedente = '32414'
    d.data_vencimento = datetime.date(2010, 3, 27)
    d.data_documento = datetime.date(2010, 2, 12)
    d.data_processamento = datetime.date(2010, 2, 12)
    d.valor = 315.00
    d.valor_documento = d.valor
    d.nosso_numero = "00068393"
    d.numero_documento = d.nosso_numero
    d.aceite = ''
    d.especie_documento = ''
    d.local_pagamento = "ATÉ O VENCIMENTO, PREFERENCIALMENTE NO ITAÚ. APÓS O VENCIMENTO, SOMENTE NO ITAÚ"
    d.instrucoes = [
        "1 - Sr. Caixa, cobrar multa de 2% após o vencimento",
        "2 - Receber até 10 dias após o vencimento",
    ]
    d.demonstrativo = [
        "1 - Serviço Teste R$ 315,00",
        "2 - Total R$ 315,00",
    ]
    d.sacado = [
        "ARTHUR ERNESTO KIRSCHNER",
        "MEDGAR EVERS, 2",
        "04020080 - São Paulo - SP"
    ]
    print_teste_boleto(d, 'itau')


def print_all():
    print "Pyboleto version: %s" % pyboleto.__version__
    print "----------------------------------"
    print "     Printing Example Boletos     "
    print "----------------------------------"

    print "Itau"
    print_itau()

    print "----------------------------------"
    print "Ok"


if __name__ == "__main__":
    print_all()