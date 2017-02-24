# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-09 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon_Core', '0014_auto_20170208_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='CreditCardNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='ExpMonth',
            field=models.IntegerField(choices=[('JAN', '1'), ('FEB', '2'), ('APR', '3'), ('MAY', '4'), ('JUNE', '5')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='ExpYear',
            field=models.IntegerField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default=2017, null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='SecurityCode',
            field=models.IntegerField(null=True),
        ),
    ]
