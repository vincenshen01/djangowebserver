# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 15:01
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170228_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]
