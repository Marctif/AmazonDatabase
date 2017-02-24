# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-17 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon_Core', '0020_delete_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('numAvailable', models.IntegerField()),
            ],
        ),
    ]