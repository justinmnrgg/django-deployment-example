from django.db import models
from utama.models import Akun, User
from rumah_sakit.models import (RumahSakit)

# Create your models here.
class Pengunjung(models.Model):
    """docstring for User."""
    STATUS_CHOICES = (
        ('pria','Pria'),
        ('wanita','Wanita')
    )

    nama = models.CharField(max_length=100, primary_key=True)
    akun = models.ForeignKey(Akun)
    tempat_tanggal_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    golongan_darah = models.CharField(max_length=3)
    alamat = models.TextField()
    jenis_kelamin = models.CharField(max_length=8, choices=STATUS_CHOICES, default='jenis')
    nomor_telepon = models.CharField(max_length=20)
    foto_profil = models.ImageField(upload_to='foto_profil_pengunjung', blank=True)

    def __str__(self):
        return self.nama

class Review(models.Model):
    """docstring for Review."""
    STATUS_CHOICES = (
        ('rejected','Rejected'),
        ('validated','Validated'),
        ('request','Request'),
        ('rejected_by_system','Rejected By System')
    )
    id_review = models.AutoField(primary_key=True)
    pengunjung = models.ForeignKey(Pengunjung)
    rumah_sakit = models.ForeignKey(RumahSakit)
    isi_review = models.TextField()
    waktu_stamp = models.DateTimeField(auto_now_add=True)
    waktu_validasi = models.DateTimeField(blank=True)
    data_lokasi_pengunjung = models.CharField(max_length=300)
    status_validasi = models.CharField(max_length=50, choices=STATUS_CHOICES, default='request')
    rating = models.IntegerField()

    def __str__(self):
        return self.id_review+"--"+self.user+"-"+self.rumah_sakit

class FotoReview(models.Model):
    """docstring for FotoReview."""
    id_foto_profil = models.AutoField(primary_key=True)
    id_review = models.ForeignKey(Review)
    foto_review = models.ImageField(upload_to='foto_review', blank=True)

    def __str__(self):
        return self.url_foto_review
