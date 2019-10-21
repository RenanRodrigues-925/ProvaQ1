from django.db import models

class Despesa(models.Model):
    data_criacao = models.DateField('Data de Criação')
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
    tipo_despesa = models.CharField('Tipo de Despesa', max_length=20, choices=TIPO_CHOICES_DESPESA, default=ALI)
    descricao = models.CharField('Descrição', max_length=300)
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
    quitado = models.BooleanField('Quitado')

    class Meta:
        verbose_name_plural = 'Despesas'
        verbose_name = 'Despesa'

def __str__(self):
    return '{} {} - {}'.format(
            self.data.strftime('%d/%m/%Y'),
            self.hora.strftime('%H:%M'),
            self.data_criacao
        )

def __str__(self):
    return self.data_criacao