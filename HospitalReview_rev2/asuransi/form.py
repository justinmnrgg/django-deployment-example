from django import forms
from utama import models
from asuransi import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = models.User
        fields = ('username','email', 'password')

class AsuransiForm(forms.ModelForm):
    class Meta():
        model = models.Asuransi
        fields = ('nama', 'url_website', 'dokumen', 'foto_profil', 'nomor_telepon')
