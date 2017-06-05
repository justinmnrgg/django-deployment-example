# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asuransi', '0004_auto_20170514_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asuransi',
            name='dokumen',
            field=models.FileField(blank=True, upload_to='dokumen_asuransi'),
        ),
        migrations.AlterField(
            model_name='asuransi',
            name='foto_profil',
            field=models.ImageField(blank=True, upload_to='foto_profil_asuransi'),
        ),
        migrations.AlterField(
            model_name='hubunganrumahsakitasuransi',
            name='dokumen',
            field=models.FileField(blank=True, upload_to='dokumen_hubungan_rumah_sakit_asuransi'),
        ),
    ]
