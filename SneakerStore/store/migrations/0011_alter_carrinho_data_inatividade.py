# Generated by Django 4.2 on 2023-05-08 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_carrinho_data_inatividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='data_inatividade',
            field=models.DateField(default=datetime.datetime(2023, 5, 15, 14, 7, 27, 149076)),
        ),
    ]
