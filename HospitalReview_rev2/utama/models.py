from django.db import models
from django.contrib.auth.models import User, Group
# from asuransi.models import Asuransi
# from rumah_sakit.models import RumahSakit

class Akun (models.Model):
    user = models.OneToOneField(User)
    waktu_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Administrator(models.Model):
    STATUS_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    )

    akun = models.ForeignKey(Akun)
    nama = models.CharField(max_length=100, primary_key=True)
    jenis_kelamin = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pria')
    nomor_telepon = models.CharField(max_length=20)
    foto_profil = models.ImageField(upload_to='foto_profil_administrator', blank=True)

    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=200, unique=True, primary_key=True)
    isi = models.TextField()
    waktu = models.DateTimeField(auto_now_add=True)
    administrator = models.ForeignKey(Administrator)
    foto_berita = models.ImageField(upload_to='foto_berita', blank=True)

    def __str__(self):
        return self.judul
