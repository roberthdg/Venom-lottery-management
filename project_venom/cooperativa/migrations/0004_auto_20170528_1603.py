# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperativa', '0003_usuario_cooperativa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credito',
            name='saldo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='saldo',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]