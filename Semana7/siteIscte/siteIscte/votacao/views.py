from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse, reverse_lazy

from .models import Questao, Opcao, Aluno
from django.core.files.storage import FileSystemStorage

@login_required(login_url=reverse_lazy('votacao:signup'))
def profile(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None :
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        current_avatar = request.user.aluno.avatar
        if current_avatar != "AvatarDefault":
            fs.delete(request.user.aluno.avatar)

        fs.save("Avatar" + str(request.user.id), myfile)
        request.user.aluno.avatar = "Avatar" + str(request.user.id)
        request.user.aluno.save()

    return render(request, 'votacao/profile.html')

def index(request):
  latest_question_list = Questao.objects.order_by('-pub_data')[:5]
  context = {'latest_question_list': latest_question_list,}
  return render(request, 'votacao/index.html', context)

@login_required(login_url=reverse_lazy('votacao:signup'))
def detalhe(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request, 'votacao/detalhe.html',
               {'questao': questao,})

def resultados(request, questao_id):
 response = "Estes sao os resultados da questao %s."
 return HttpResponse(response % questao_id)

@permission_required('votacao.change_opcao', login_url=reverse_lazy('votacao:fazer_login'))
def voto(request, questao_id):
     questao = get_object_or_404(Questao, pk=questao_id)

     try:
         opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
     except (KeyError, Opcao.DoesNotExist):
            return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção",})
     else:
        if (request.POST['action'] == 'Voto'):
            if(request.user.aluno.total_votos >= 26+5):
                return render(request, 'votacao/detalhe.html',{'questao': questao, 'error_message': "Limite de votos atingido", })
            opcao_seleccionada.votos += 1
            opcao_seleccionada.save()
            request.user.aluno.total_votos += 1
            request.user.aluno.save()
        elif request.POST['action'] == 'Delete':
            opcao_seleccionada.delete()
            return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
     return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))



def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request,'votacao/resultados.html',{'questao': questao})


def criarquestao(request):
    if request.method == 'POST':
        questao_texto = request.POST['questaotext']
        q = Questao(questao_texto=questao_texto, pub_data=timezone.now())
        q.save()
        return HttpResponseRedirect(reverse('votacao:index'))
    return render(request,'votacao/criarquestao.html')

def criaropcao(request, questao_id):
    if request.method == 'POST':
        opcao_texto = request.POST['opcaotext']
        q = get_object_or_404(Questao, pk=questao_id)
        q.opcao_set.create(opcao_texto=opcao_texto, votos=0)
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao_id,)))

    return render(request,'votacao/criaropcao.html',{'questao': get_object_or_404(Questao, pk=questao_id)})

def apagarquestao(request, questao_id):
    q = get_object_or_404(Questao, pk=questao_id)
    q.delete()
    return HttpResponseRedirect(reverse('votacao:index'))


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('votacao:index'))
def signup(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('votacao:index'))
            else:
                return HttpResponseRedirect(reverse('votacao:signup'))
        elif request.POST['action'] == 'Registar':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            curso = request.POST['curso']
            user = User.objects.create_user(username=username, email=email, password=password)
            aluno = Aluno(user=user, curso=curso)
            aluno.save()
            return HttpResponseRedirect(reverse('votacao:signup'))

    else:
        return render(request, 'votacao/login-registar.html')
