from django import forms
from utama import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = models.User
        fields = ('username','email', 'password')

class AdministratorForm(forms.ModelForm):
    class Meta():
        model = models.Administrator
        fields = ('nama', 'jenis_kelamin', 'nomor_telepon', 'foto_profil')

class BeritaForm(forms.ModelForm):
    class Meta():
        model = models.Berita
        fields = ('judul', 'isi', 'foto_berita')
