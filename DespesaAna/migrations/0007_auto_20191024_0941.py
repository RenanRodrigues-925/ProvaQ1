# Generated by Django 2.2.6 on 2019-10-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DespesaAna', '0006_auto_20191020_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='quitado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.CharField(choices=[('Remedio', 'Remedio'), ('Roupas', 'Roupas'), ('Alimentação', 'Alimentação'), ('Educação', 'Educação'), ('Transporte', 'Transporte'), ('Outros', 'Outros')], max_length=20, verbose_name='Tipo de Despesa'),
        ),
    ]
