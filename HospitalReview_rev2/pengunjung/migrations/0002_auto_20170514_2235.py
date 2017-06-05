# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pengunjung', '0001_initial'),
        ('utama', '0001_initial'),
        ('rumah_sakit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rumah_sakit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.RumahSakit'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengunjung.Pengunjung'),
        ),
        migrations.AddField(
            model_name='pengunjung',
            name='akun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.Akun'),
        ),
        migrations.AddField(
            model_name='fotoreview',
            name='id_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengunjung.Review'),
        ),
    ]