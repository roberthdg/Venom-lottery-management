# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperativa', '0006_auto_20170529_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credito',
            old_name='seguro_desgravamen',
            new_name='seguro',
        ),
        migrations.RemoveField(
            model_name='garante',
            name='codigo_cliente',
        ),
        migrations.RemoveField(
            model_name='garante',
            name='ruc',
        ),
        migrations.AddField(
            model_name='garante',
            name='codigo_credito',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='cooperativa.Credito'),
            preserve_default=False,
        ),
    ]