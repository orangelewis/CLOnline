# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 22:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='洲')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '洲',
                'verbose_name_plural': '洲',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
                ('desc', models.CharField(max_length=50, verbose_name='特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='喜爱数')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('image', models.ImageField(default='', upload_to='director/%Y/%m', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '导演',
                'verbose_name_plural': '导演',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('desc', models.TextField(verbose_name='描述')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='喜爱数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('film_nums', models.IntegerField(default=0, verbose_name='电影数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.ContinentDict', verbose_name='所属洲')),
            ],
            options={
                'verbose_name': '国家地区',
                'verbose_name_plural': '国家地区',
            },
        ),
        migrations.AddField(
            model_name='director',
            name='reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Region', verbose_name='所属国家地区'),
        ),
    ]