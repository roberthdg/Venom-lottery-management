# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 01:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperativa', '0004_auto_20170528_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credito',
            old_name='entaje',
            new_name='encaje',
        ),
    ]
