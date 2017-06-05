from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import (CreateView, UpdateView, DeleteView,
                                  FormView, TemplateView, DetailView,
                                  ListView, View)
from .models import (Administrator, Akun, Berita,
                     Group, User)
from .form import (AdministratorForm, BeritaForm, UserForm)

from rumah_sakit.models import RumahSakit
# Create your views here.

class HomeView(View):
    def get(self, request):
        rumah_sakit = RumahSakit.objects.all()
        return render(request, 'home/index.html', {'rumah_sakits':rumah_sakit})



class RegistrasiAdministrator(View):

    def get(self, request):
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            administrator_form = AdministratorForm(data=request.POST)

            if user_form.is_valid() and administrator_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()



        else:
            user_form = UserForm()
            administrator_form = AdministratorForm()
            #akun_form = AkunForm()

            return render(request, 'admin/registeru.html', {'user_form':user_form, 'administrator_form' : administrator_form})
