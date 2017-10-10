# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-26 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(max_length=300)),
                ('interests', models.TextField()),
                ('joining_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('roll_no', models.IntegerField(default=0)),
                ('course', models.CharField(default=0, max_length=300)),
            ],
        ),
    ]
