from django.shortcuts import render
from django.views.generic import (TemplateView, View, ListView,
                                  DetailView, FormView, DeleteView,
                                  UpdateView, CreateView)
from .models import (Akun, Asuransi, Administrator,
                     RumahSakit, HubunganRumahSakitAsuransi)
# Create your views here.
from utama import models

from .form import (AsuransiForm, UserForm)

class RegistrasiAsuransi(View):

    def get(self, request):
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            asuransi_form = AsuransiForm(data=request.POST)

            if user_form.is_valid() and administrator_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()



        else:
            user_form = UserForm()
            asuransi_form = AsuransiForm()
            #akun_form = AkunForm()

            return render(request, 'admin/registera.html', {'user_form':user_form, 'asuransi_form' : asuransi_form})
