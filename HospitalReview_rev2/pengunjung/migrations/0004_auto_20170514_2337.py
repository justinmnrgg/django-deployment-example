# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengunjung', '0003_auto_20170514_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='data_lokasi_user',
            new_name='data_lokasi_x',
        ),
        migrations.AlterField(
            model_name='pengunjung',
            name='jenis_kelamin',
            field=models.CharField(choices=[('pria', 'Pria'), ('wanita', 'Wanita')], default='jenis', max_length=8),
        ),
    ]
