# Generated by Django 4.2.1 on 2023-05-10 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_empregadoloja_imagem_alter_carrinho_data_inatividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='data_inatividade',
            field=models.DateField(default=datetime.datetime(2023, 5, 17, 15, 54, 29, 92762)),
        ),
        migrations.RemoveField(
            model_name='favoritos',
            name='sneaker',
        ),
        migrations.AddField(
            model_name='favoritos',
            name='sneaker',
            field=models.ManyToManyField(to='store.sneaker'),
        ),
    ]
