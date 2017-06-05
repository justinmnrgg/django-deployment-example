from django.db import models
from utama.models import Administrator, Akun, User
from rumah_sakit.models import RumahSakit

# Create your models here.

class Asuransi(models.Model):
    """docstring for Asuransi."""
    STATUS_CHOICES = (
        ('rejected', 'Rejected'),
        ('validated', 'Validated'),
        ('request', 'Request')
    )

    akun = models.ForeignKey(Akun)
    nama = models.CharField(max_length=100, primary_key=True)
    url_website = models.CharField(max_length=400,unique=True)
    dokumen = models.FileField(upload_to='dokumen_asuransi', blank=True)
    foto_profil = models.ImageField(upload_to='foto_profil_asuransi', blank=True)
    nomor_telepon = models.CharField(max_length=20)
    status_validasi = models.CharField(max_length=50, choices=STATUS_CHOICES, default='request')
    waktu_validasi = models.DateTimeField(blank=True)
    administrator = models.ForeignKey(Administrator, blank=True)

    def __str__(self):
        return self.nama


class HubunganRumahSakitAsuransi(models.Model):
    """docstring for HubunganRumahSakitAsuransi."""
    STATUS_CHOICES = (
        ('rejected', 'Rejected'),
        ('validated', 'Validated'),
        ('request', 'Request')
    )

    id_hubungan_rumah_sakit_asuransi = models.AutoField(primary_key=True)
    asuransi = models.ForeignKey(Asuransi)
    rumah_sakit = models.ForeignKey(RumahSakit)
    dokumen = models.FileField(upload_to='dokumen_hubungan_rumah_sakit_asuransi', blank=True)
    administrator = models.ForeignKey(Administrator)
    status_validasi_rumah_sakit = models.CharField(max_length=50, choices=STATUS_CHOICES, default='request')
    status_validasi_administrator = models.CharField(max_length=50, choices=STATUS_CHOICES, default='request')
    waktu_validasi = models.DateTimeField(blank=True)

    def __str__(self):
        return self.asuransi+"--"+self.rumah_sakit
