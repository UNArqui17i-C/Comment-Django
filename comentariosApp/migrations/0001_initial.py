# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]