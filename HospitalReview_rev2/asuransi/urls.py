from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'asuransi'

urlpatterns = [
    url(r'^admin/register', views.RegistrasiAsuransi.as_view(), name='register')
]
