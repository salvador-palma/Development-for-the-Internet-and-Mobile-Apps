from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Questao, Opcao


def index(request):
  latest_question_list = Questao.objects.order_by('-pub_data')[:5]
  context = {'latest_question_list': latest_question_list,}
  return render(request, 'votacao/index.html', context)

def detalhe(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request, 'votacao/detalhe.html',
               {'questao': questao})

def resultados(request, questao_id):
 response = "Estes sao os resultados da questao %s."
 return HttpResponse(response % questao_id)

def voto(request, questao_id):
     questao = get_object_or_404(Questao, pk=questao_id)
     try:
         opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
     except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção",})
     else:
         opcao_seleccionada.votos += 1
         opcao_seleccionada.save()
     return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request,'votacao/resultados.html',{'questao': questao})