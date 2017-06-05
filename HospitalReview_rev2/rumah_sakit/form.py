from django import forms
from utama import models
from rumah_sakit import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = models.User
        fields = ('username','email', 'password')

class RumahSakitForm(forms.ModelForm):
    class Meta():
        model = models.RumahSakit
        fields = ('nama', 'foto_profil', 'dokumen', 'url_website', 'alamat', 'nomor_telepon')
