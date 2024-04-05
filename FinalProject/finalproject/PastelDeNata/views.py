from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from PastelDeNata.models import Enterprise

from PastelDeNata.models import Rating

from PastelDeNata.models import Photo

from PastelDeNata.models import District


def index(request):
    companies = Enterprise.objects.all().order_by('rating_average')
    districts = District.objects.all().order_by('name')
    return render(request, 'PastelDeNata/index.html',{'companies': companies, "districts": districts})
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

            clientType = request.POST['clientType']

            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=email, first_name=username, email=email, password=password)

            if clientType == 'company':
                company = Enterprise.objects.create(user=user)
                company.save()
            user.save()
            return HttpResponseRedirect(reverse('PastelDeNata:registar'))
    else:
        return render(request, 'PastelDeNata/login.html')
def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('PastelDeNata:index'))

def companyprofileedit(request, company_id):
    if(request.user.enterprise.id != company_id):
        return HttpResponseRedirect(reverse('PastelDeNata:index'))
    company = get_object_or_404(Enterprise, pk=company_id)

    districts = District.objects.all()
    company_photos = Photo.objects.filter(enterprise__id=company_id)

    return render(request, 'PastelDeNata/estabelecimento-editar.html',{'company': company,'company_photos': company_photos, 'districts': districts})

def companyprofile(request, company_id):
    company = get_object_or_404(Enterprise, pk=company_id)

    if request.method=='POST' and request.POST['action'] == 'GUARDAR':
        photo_href_list = request.POST.getlist('companyPhoto')
        update_company_photos(company, photo_href_list)
        company.district = District.objects.get(name = request.POST['companyDistrict'])
        company.address = request.POST['companyAddress']
        company.description = request.POST['companyDescription']
        company.save()

    latest_reviews = Rating.objects.filter(enterprise__id = company_id).order_by('-date')[:5]
    company_photos = Photo.objects.filter(enterprise__id = company_id)
    return render(request, 'PastelDeNata/estabelecimento.html',{'company': company, 'latest_reviews': latest_reviews, 'company_photos': company_photos})




# ========= 👾 H E L P F U L    F U N C T I O N S 🧩 ========== #

def update_company_photos(company, href_list):
    existing_photos = Photo.objects.filter(enterprise = company)
    existing_href_set = set(photo.href for photo in existing_photos)
    provided_href_set = set(href_list)

    # Delete photos whose hrefs are not in the provided list
    photos_to_delete = existing_photos.exclude(href__in=provided_href_set)
    photos_to_delete.delete()

    # Add new photos for the hrefs that don't already exist
    new_hrefs = provided_href_set - existing_href_set
    for href in new_hrefs:
        Photo.objects.create(enterprise=company, href=href).save()

def get_all_companies(request):

    district = request.GET['district']
    search_str = request.GET['search_str']
    sorting_mode = request.GET['sorting_mode']

    results = Enterprise.objects.all()
    if search_str != " ":
        results = results.filter(user__first_name__contains=search_str)
    if district != "Portugal Inteiro":
        results = results.filter(district__name=district)

    # Nao vale a pena otimizar, Python 3.9 nao tem switch/match 🙃💔
    if sorting_mode == 'RAT_ASC':
        results = results.order_by('rating_average')
    elif sorting_mode == 'RAT_DESC':
        results = results.order_by('-rating_average')
    elif sorting_mode == 'REV_ASC':
        results = results.order_by('rating_amount')
    elif sorting_mode == 'REV_DESC':
        results = results.order_by('-rating_amount')
    elif sorting_mode == 'ALF_ASC':
        results = results.order_by('user__first_name')
    elif sorting_mode == 'ALF_DESC':
        results = results.order_by('-user__first_name')

    return render(request, 'PastelDeNata/company_table.html',{'companies': results,})