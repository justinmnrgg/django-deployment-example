from django import forms
from utama import models
from pengunjung import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = models.User
        fields = ('username','email', 'password')

class PengunjungForm(forms.ModelForm):
    class Meta():
        model = models.Pengunjung
        fields = ('nama', 'tempat_tanggal_lahir', 'tanggal_lahir', 'golongan_darah', 'alamat', 'jenis_kelamin', 'nomor_telepon', 'foto_profil')
