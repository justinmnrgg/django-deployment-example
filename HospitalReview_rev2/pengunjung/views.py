from django.shortcuts import render
from django.views.generic import (TemplateView, View, ListView,
                                  DetailView, FormView, DeleteView,
                                  UpdateView, CreateView)
from .models import (RumahSakit, Akun, Review,
                     Pengunjung, FotoReview)

from utama import models
from .form import (PengunjungForm, UserForm)
# Create your views here.


class RegistrasiPengunjung(View):

    def get(self, request):
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            pengunjung_form = PengunjungForm(data=request.POST)

            if user_form.is_valid() and pengunjung_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()



        else:
            user_form = UserForm()
            pengunjung_form = PengunjungForm()
            #akun_form = AkunForm()

            return render(request, 'admin/registerp.html', {'user_form':user_form, 'pengunjung_form' : pengunjung_form})
