# Generated by Django 2.2.6 on 2019-10-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DespesaAna', '0003_delete_formapagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data_criacao',
            field=models.DateField(max_length=10, verbose_name='Data de Criação'),
        ),
    ]