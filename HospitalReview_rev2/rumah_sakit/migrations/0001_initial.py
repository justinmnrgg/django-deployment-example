# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id_dokter', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nomor_telepon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FasilitasRumahSakit',
            fields=[
                ('id_fasilitas', models.AutoField(primary_key=True, serialize=False)),
                ('sub_fasilitas', models.CharField(max_length=200)),
                ('jumlah', models.IntegerField()),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FotoRumahSakit',
            fields=[
                ('id_foto_rumah_sakit', models.AutoField(primary_key=True, serialize=False)),
                ('foto_rumah_sakit', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JadwalDokter',
            fields=[
                ('id_jadwal', models.AutoField(primary_key=True, serialize=False)),
                ('waktu_masuk', models.TextField()),
                ('waktu_keluar', models.TextField()),
                ('dokter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.Dokter')),
            ],
        ),
        migrations.CreateModel(
            name='JenisFasilitas',
            fields=[
                ('jenis_fasilitas', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('nama', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('gejala', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RumahSakit',
            fields=[
                ('nama', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('foto_profil', models.ImageField(blank=True, upload_to='')),
                ('dokumen', models.FileField(blank=True, upload_to='')),
                ('url_website', models.CharField(max_length=400, unique=True)),
                ('alamat', models.TextField()),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('status_validasi', models.CharField(choices=[('request', 'Request'), ('validated', 'Validated'), ('rejected', 'Rejected')], default='request', max_length=20)),
                ('waktu_validasi', models.DateField(blank=True)),
                ('administrator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='utama.Administrator')),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.Akun')),
            ],
        ),
        migrations.CreateModel(
            name='Spesialis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_spesialis', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='penyakit',
            name='spesialis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.Spesialis'),
        ),
        migrations.AddField(
            model_name='fotorumahsakit',
            name='rumah_sakit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.RumahSakit'),
        ),
        migrations.AddField(
            model_name='fasilitasrumahsakit',
            name='jenis_fasilitas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.JenisFasilitas'),
        ),
        migrations.AddField(
            model_name='fasilitasrumahsakit',
            name='rumah_sakit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.RumahSakit'),
        ),
        migrations.AddField(
            model_name='dokter',
            name='rumah_sakit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.RumahSakit'),
        ),
        migrations.AddField(
            model_name='dokter',
            name='spesialis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rumah_sakit.Spesialis'),
        ),
    ]
