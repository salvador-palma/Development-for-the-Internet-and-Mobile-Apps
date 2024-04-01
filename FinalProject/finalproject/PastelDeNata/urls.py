from django.urls import include, path
from . import views
app_name = 'PastelDeNata'
urlpatterns = [
 path("", views.index, name="index"),
 path("registar", views.registar, name="registar"),
 path("sair", views.sair, name="sair"),
]