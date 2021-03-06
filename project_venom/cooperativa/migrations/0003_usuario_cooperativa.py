# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cooperativa', '0002_remove_cooperativa_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_cooperativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_permiso', models.IntegerField()),
                ('cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperativa.Cooperativa')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
