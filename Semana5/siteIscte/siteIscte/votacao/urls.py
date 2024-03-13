from django.urls import include, path
from . import views

app_name = 'votacao'
urlpatterns = [
    path("", views.index, name='index'),
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    path('<int:questao_id>/voto', views.voto, name='voto'),
    path('criarquestao', views.criarquestao, name='criarquestao'),
    path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),
    path('<int:questao_id>/apagarquestao', views.apagarquestao, name='apagarquestao')
]