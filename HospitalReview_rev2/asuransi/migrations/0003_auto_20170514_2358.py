# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 16:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asuransi', '0002_auto_20170514_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asuransi',
            old_name='administrator',
            new_name='administrator_id',
        ),
    ]
