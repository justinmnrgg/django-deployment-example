from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'utama'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/register', views.RegistrasiAdministrator.as_view(), name='register')
]
