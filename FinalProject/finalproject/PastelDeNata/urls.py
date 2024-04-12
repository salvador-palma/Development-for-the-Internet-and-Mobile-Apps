from django.urls import include, path
from . import views
app_name = 'PastelDeNata'
urlpatterns = [
 path("", views.index, name="index"),
 path("registar", views.registar, name="registar"),
 path("sair", views.sair, name="sair"),
 path('<int:company_id>', views.companyprofile, name='companyprofile'),
 path('<int:company_id>/edit', views.companyprofileedit, name='companyprofileedit'),
 path('user/<int:client_id>', views.userprofile, name='userprofile'),
 path('user/<int:client_id>/edit', views.userprofileedit, name='userprofileedit'),

 # ========= 📞 H E L P F U L    U R L    C A L L S 💭 ========== #
 path('companies', views.get_all_companies, name='get_all_companies'),
]