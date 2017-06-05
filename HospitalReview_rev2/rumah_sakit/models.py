from django.db import models
from utama.models import Administrator, Akun, User

# Create your models here.
class RumahSakit(models.Model):
    """docstring for RumahSakit."""
    STATUS_CHOICES = (
        ('request','Request'),
        ('validated','Validated'),
        ('rejected','Rejected')
    )

    nama = models.CharField(max_length=100, primary_key=True)
    akun = models.ForeignKey(Akun)
    foto_profil = models.ImageField(upload_to='foto_profil_rumah_sakit', blank=True)
    dokumen = models.FileField(upload_to='dokumen_rumah_sakit', blank=True)
    url_website = models.CharField(max_length=400,unique=True)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=20)
    status_validasi = models.CharField(max_length=20, choices=STATUS_CHOICES, default='request')
    waktu_validasi = models.DateField(blank=True)
    administrator = models.ForeignKey(Administrator,blank=True)

    def __str__(self):
        return self.nama

class FotoRumahSakit(models.Model):
    """docstring for FotoRumahSakit."""
    id_foto_rumah_sakit = models.AutoField(primary_key=True)
    rumah_sakit = models.ForeignKey(RumahSakit)
    foto_rumah_sakit = models.ImageField(upload_to='foto_rumah_sakit', blank=True)

    def __str__(self):
        return self.url_foto_rumah_sakit

class JenisFasilitas(models.Model):
    """docstring for Fasilitas."""
    jenis_fasilitas = models.CharField(max_length=300, primary_key=True)
    deskripsi = models.TextField()

    def __str__(self):
        return self.fasilitas

class FasilitasRumahSakit(models.Model):
    """docstring for FasilitasRumahSakit."""
    id_fasilitas = models.AutoField(primary_key=True)
    jenis_fasilitas = models.ForeignKey(JenisFasilitas)
    rumah_sakit = models.ForeignKey(RumahSakit)
    sub_fasilitas = models.CharField(max_length=200)
    jumlah = models.IntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.rumah_sakit+"--"+self.sub_fasilitas

class Spesialis(models.Model):
    """docstring for Spesialis."""
    jenis_spesialis = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.jenis_spesialis

class Dokter(models.Model):
    """docstring for Dokter."""
    id_dokter = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=20)
    rumah_sakit = models.ForeignKey(RumahSakit)
    spesialis = models.ForeignKey(Spesialis)

    def __str__(self):
        return self.nama

class JadwalDokter(models.Model):
    """docstring for JadwalDokter."""
    id_jadwal = models.AutoField(primary_key=True)
    dokter = models.ForeignKey(Dokter)
    waktu_masuk = models.TextField()
    waktu_keluar = models.TextField()

    def __str__(self):
        return self.id_jadwal+"--"+self.dokter

class Penyakit(models.Model):
    nama = models.CharField(max_length=100, primary_key=True)
    gejala = models.TextField()
    spesialis = models.ForeignKey(Spesialis)

    def __str__(self):
        return self.nama
