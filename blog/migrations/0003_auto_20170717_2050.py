# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-17 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170717_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateField(),
        ),
    ]