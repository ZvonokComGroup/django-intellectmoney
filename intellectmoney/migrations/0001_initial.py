# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntellectMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('orderId', models.CharField(editable=False, max_length=255, unique=True)),
            ],
        ),
    ]
