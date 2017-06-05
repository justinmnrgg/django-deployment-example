from django.contrib import admin
from .models import (Pengunjung, Review, FotoReview)

# Register your models here.

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ('nama', 'akun', 'golongan_darah', 'jenis_kelamin', 'nomor_telepon')
    list_filter = ('nama', 'akun', 'golongan_darah', 'jenis_kelamin')
    search_fields = ('nama', 'akun')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id_review', 'pengunjung', 'rumah_sakit', 'data_lokasi_pengunjung', 'status_validasi', 'rating')
    list_filter = ('id_review', 'pengunjung', 'rumah_sakit')
    search_fields = ('id_review', 'pengunjung', 'rumah_sakit')

class FotoReviewAdmin(admin.ModelAdmin):
    list_display = ('id_foto_profil', 'id_review')
    list_filter = ('id_foto_profil', 'id_review')
    search_fields = ('id_foto_profil', 'id_review')

admin.site.register(Pengunjung, PengunjungAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(FotoReview, FotoReviewAdmin)