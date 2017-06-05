from django.contrib import admin
from .models import (RumahSakit, FotoRumahSakit, JenisFasilitas,
                     FasilitasRumahSakit, Spesialis, Dokter,
                     JadwalDokter, Penyakit)
# Register your models here.

class RumahSakitAdmin(admin.ModelAdmin):
    list_display = ('nama', 'akun', 'url_website', 'nomor_telepon', 'status_validasi')
    list_filter = ('nama', 'akun', 'url_website', 'nomor_telepon')
    search_fields = ('nama','akun')

class FotoRumahSakitAdmin(admin.ModelAdmin):
    list_display = ('id_foto_rumah_sakit', 'rumah_sakit')
    list_filter = ('id_foto_rumah_sakit', 'rumah_sakit')
    search_fields = ('id_foto_rumah_sakit', 'rumah_sakit')

class FasilitasRumahSakitAdmin(admin.ModelAdmin):
    list_display = ('id_fasilitas', 'jenis_fasilitas', 'rumah_sakit', 'sub_fasilitas', 'jumlah')
    list_filter = ('id_fasilitas', 'jenis_fasilitas', 'rumah_sakit', 'sub_fasilitas')
    search_fields = ('id_fasilitas', 'jenis_fasilitas', 'rumah_sakit', 'sub_fasilitas')

class DokterAdmin(admin.ModelAdmin):
    list_display = ('id_dokter', 'nama', 'email', 'nomor_telepon', 'rumah_sakit', 'spesialis')
    list_filter = ('id_dokter', 'nama', 'email', 'rumah_sakit', 'spesialis')
    search_fields = ('id_dokter', 'nama', 'email', 'rumah_sakit', 'spesialis')

class JadwalDokterAdmin(admin.ModelAdmin):
    list_display = ('id_jadwal', 'dokter')
    list_filter = ('id_jadwal', 'dokter')
    search_fields = ('id_jadwal', 'dokter')

class PenyakitAdmin(admin.ModelAdmin):
    list_display = ('nama', 'spesialis')
    list_filter = ('nama', 'spesialis')
    search_fields = ('nama', 'spesialis')

admin.site.register(RumahSakit, RumahSakitAdmin)
admin.site.register(FotoRumahSakit, FotoRumahSakitAdmin)
admin.site.register(JenisFasilitas)
admin.site.register(FasilitasRumahSakit, FasilitasRumahSakitAdmin)
admin.site.register(Spesialis)
admin.site.register(Dokter, DokterAdmin)
admin.site.register(JadwalDokter, JadwalDokterAdmin)
admin.site.register(Penyakit, PenyakitAdmin)