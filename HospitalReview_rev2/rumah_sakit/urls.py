from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'rumah_sakit'

urlpatterns = [
    url(r'^admin/register', views.RegistrasiRumahsakit.as_view(), name='register')
]
