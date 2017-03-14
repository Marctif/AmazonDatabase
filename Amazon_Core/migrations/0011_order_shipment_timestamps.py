# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-08 22:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon_Core', '0010_school_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineitem', models.CharField(default=None, max_length=50)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('custProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazon_Core.CustomerProfile')),
                ('payMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazon_Core.CreditCard')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OR', 'Ordered'), ('SP', 'Shipped'), ('DE', 'Delivered')], default='OR', max_length=5)),
                ('estimated_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('shipped_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazon_Core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Timestamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=10)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amazon_Core.Shipment')),
            ],
        ),
    ]