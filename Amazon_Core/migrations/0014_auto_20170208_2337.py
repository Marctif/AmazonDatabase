# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-08 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon_Core', '0013_auto_20170208_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='Zipcode',
            field=models.IntegerField(null=True),
        ),
    ]