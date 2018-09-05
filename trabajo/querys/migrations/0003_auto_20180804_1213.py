# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querys', '0002_auto_20180804_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='position',
            field=models.IntegerField(blank=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='link',
            field=models.TextField(primary_key=True),
        ),
        migrations.AlterField(
            model_name='paperquality',
            name='quality',
            field=models.ForeignKey(db_column='quality', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='querys.Quality'),
        ),
    ]