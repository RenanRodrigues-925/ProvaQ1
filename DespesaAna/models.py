from django.db import models

class Despesa(models.Model):
    data_criacao = models.DateField('Data de Criação')
    tipo_despesa = models.CharField('Tipo de Despesa',)
    RE = 'Remedio'
    RO = 'Roupas'
    ALI = 'Alimentação'
    ED = 'Educação'
    TRANS = 'Transporte'
    OUT = 'Outros'
    TIPO_CHOICES_DESPESA = [
        (RE, 'Remedio'),
        (RO, 'Roupas'),
        (ALI, 'Alimentação'),
        (ED, 'Educação'),
        (TRANS, 'Transporte'),
        (OUT, 'Outros')
    ]
    tipo_despesa = models.CharField('Tipo de Despesa', max_length=20, choices=TIPO_CHOICES_DESPESA)
    descricao = models.TextField('Descrição')
    DI = 'Dinheiro'
    CC = 'Cartão de Crédito'
    CD = 'Cartão de Débito'
    CRE = 'Cartão Crediário'
    CH = 'Cheque'
    TIPO_CHOICES_PAGAMENTO = [
        (DI, 'Dinheiro'),
        (CC, 'Cartão de Crédito'),
        (CD, 'Cartão de Débito'),
        (CRE, 'Cartão Crediário'),
        (CH, 'Cheque')
    ]
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=20, choices=TIPO_CHOICES_PAGAMENTO, default=DI)
    vencimento = models.DateField('Vencimento')
    quitado = models.BooleanField()

    def __str__(self):
        return "%s %s %s"%(
            self.descricao,
            self.data_criacao.strftime("%d/%M/%Y"),
            self.tipo_despesa
        )

    class Meta:
        verbose_name_plural = 'Despesas'
        verbose_name = 'Despesa'

ordering = ('vencimento','forma_pagamento')