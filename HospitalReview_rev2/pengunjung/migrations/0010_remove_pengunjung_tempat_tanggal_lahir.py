# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengunjung', '0009_auto_20170515_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengunjung',
            name='tempat_tanggal_lahir',
        ),
    ]