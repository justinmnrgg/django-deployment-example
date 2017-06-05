from django.shortcuts import render
from django.views.generic import (TemplateView, View, ListView,
                                  DetailView, FormView, DeleteView,
                                  UpdateView, CreateView)
from .models import (Akun, RumahSakit, Administrator,
                     JadwalDokter, FotoRumahSakit, Penyakit,
                     JenisFasilitas, Dokter, Spesialis,
                     FasilitasRumahSakit)

from utama import models

from .form import (RumahSakitForm, UserForm)


# Create your views here.


class RegistrasiRumahsakit(View):

    def get(self, request):
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            rumahsakit_form = RumahSakitForm(data=request.POST)

            if user_form.is_valid() and administrator_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()



        else:
            user_form = UserForm()
            rumahsakit_form = RumahSakitForm()
            #akun_form = AkunForm()

            return render(request, 'admin/register.html', {'user_form':user_form, 'rumahsakit_form' : rumahsakit_form})
