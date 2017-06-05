from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pengunjung'

urlpatterns = [
    url(r'^admin/register', views.RegistrasiPengunjung.as_view(), name='register')
]
