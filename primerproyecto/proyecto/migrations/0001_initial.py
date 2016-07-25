# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta_text', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(verbose_name=b'fecha de publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seleccion_text', models.CharField(max_length=200)),
                ('fkpregunta', models.ForeignKey(to='proyecto.Pregunta')),
            ],
        ),
    ]
