# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-25 14:52
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='导演描述'),
        ),
    ]
