

period_letivo = fields.Datetime(string="Período letivo", compute="ano_atual")

@api.multi
    def ano_atual(self):
        self.period_letivo = str(datetime.datetime.today().year)