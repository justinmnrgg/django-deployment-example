from django.contrib import admin
from .models import (Asuransi, HubunganRumahSakitAsuransi)

# Register your models here.

class AsuransiAdmin(admin.ModelAdmin):
    list_display = ('akun', 'nama', 'url_website', 'nomor_telepon', 'status_validasi')
    list_filter = ('akun', 'nama', 'url_website')
    search_fields = ('akun', 'nama', 'url_website')

class HubunganRumahSakitAsuransiAdmin(admin.ModelAdmin):
    list_display = ('id_hubungan_rumah_sakit_asuransi', 'asuransi', 'rumah_sakit', 'status_validasi_rumah_sakit', 'status_validasi_administrator')
    list_filter = ('id_hubungan_rumah_sakit_asuransi', 'asuransi', 'rumah_sakit')
    search_fields = ('id_hubungan_rumah_sakit_asuransi', 'asuransi', 'rumah_sakit')

admin.site.register(Asuransi, AsuransiAdmin)
admin.site.register(HubunganRumahSakitAsuransi)