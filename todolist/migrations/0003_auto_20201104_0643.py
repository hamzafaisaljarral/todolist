# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-11-04 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170928_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=b'2020-11-04'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default=b'2020-11-04'),
        ),
    ]