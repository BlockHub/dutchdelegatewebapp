# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0006_auto_20170927_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='wallet',
            new_name='main_ark_wallet',
        ),
    ]
