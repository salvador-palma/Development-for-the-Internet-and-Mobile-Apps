from django.urls import include, path
from . import views
app_name = 'PastelDeNata'
urlpatterns = [
 path("", views.index, name="index"),
 path("registar", views.registar, name="registar"),
 path("sair", views.sair, name="sair"),
 path('<int:company_id>/perfil', views.companyprofile, name='companyprofile'),
 path('<int:company_id>/perfil/edit', views.companyprofileedit, name='companyprofileedit'),
]