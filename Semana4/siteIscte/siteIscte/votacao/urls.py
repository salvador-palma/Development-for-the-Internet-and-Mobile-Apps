from django.urls import include, path
from . import views

app_name = 'votacao'
urlpatterns = [
    path("", views.index, name='index'),
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    path('<int:questao_id>/voto', views.voto, name='voto'),
]