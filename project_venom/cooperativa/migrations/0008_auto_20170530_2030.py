# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperativa', '0007_auto_20170529_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='fecha_concesion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
    ]
