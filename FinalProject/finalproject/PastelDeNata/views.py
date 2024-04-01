from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def index(request):
    return render(request, 'PastelDeNata/index.html')
def registar(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Login':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('PastelDeNata:index'))
            else:
                return HttpResponseRedirect(reverse('PastelDeNata:registar'))
        elif request.POST['action'] == 'Registar':

            # clientType = request.POST['entityType']
            username = request.POST['username']
            lastname = request.POST['lastname']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=email, first_name=username, email=email, password=password, last_name=lastname)
            # if clientType == 'Company':
            #     company = Enterprise.objects.create(user=user, )
            user.save()
            print("USER CREATED WITH SUCCESS!")
            return HttpResponseRedirect(reverse('PastelDeNata:registar'))
    else:
        return render(request, 'PastelDeNata/login.html')

def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('PastelDeNata:index'))