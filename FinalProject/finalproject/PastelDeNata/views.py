import random
import string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum, Avg
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from PastelDeNata.models import Enterprise, Rating, Photo, District, Client
from django.core.files.storage import FileSystemStorage

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
            else:
                cliente = Client.objects.create(user=user)
                cliente.save()
            user.save()
            return HttpResponseRedirect(reverse('PastelDeNata:registar'))
    else:
        return render(request, 'PastelDeNata/login.html')
def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('PastelDeNata:index'))


def companyprofileedit(request, company_id):
    if (request.user.enterprise.id != company_id):
        return HttpResponseRedirect(reverse('PastelDeNata:index'))

    if request.method == 'POST' and request.POST['action'] == 'GUARDAR':
        company = get_object_or_404(Enterprise, pk=company_id)
        update_company_photos(company, request)
        company.district = District.objects.get(name__contains=request.POST['companyDistrict'])
        company.address = request.POST['companyAddress']
        company.description = request.POST['companyDescription']
        company.save()
        return HttpResponseRedirect(reverse('PastelDeNata:companyprofile', kwargs={'company_id': company_id}))
    else:
        company = get_object_or_404(Enterprise, pk=company_id)
        districts = District.objects.all()
        company_photos = Photo.objects.filter(enterprise__id=company_id)

        return render(request, 'PastelDeNata/estabelecimento-editar.html',{'company': company,'company_photos': company_photos, 'districts': districts})

def companyprofile(request, company_id):
    company = get_object_or_404(Enterprise, pk=company_id)

    if request.method == 'POST':

        if request.POST['action'] == 'SUBMETER':

            previous_review = Rating.objects.filter(enterprise=company, client=request.user.client)

            value = request.POST['stars']
            review = request.POST['review_text']

            if previous_review.exists():

                company.rating_average = ((company.rating_average*company.rating_amount) - int(value))/(max(company.rating_amount - 1, 1))
                company.rating_amount -= 1
                previous_review.delete()
            company_stars = Rating.objects.filter(enterprise=company).aggregate(total_sum=Sum('value')).get('total_sum', 0)
            if company_stars is None:
                company_stars = 0
            total_stars = company_stars + int(value)
            company.rating_amount += 1
            company.rating_average = total_stars / company.rating_amount
            company.save()

            rating = Rating.objects.create(enterprise=company, client=request.user.client, value=value, review=review)
            rating.save()

    latest_reviews = Rating.objects.filter(enterprise__id=company_id).order_by('-date')[:5]
    if hasattr(request.user, 'client'):
        latest_reviews = Rating.objects.filter(enterprise__id=company_id, client=request.user.client) | latest_reviews
    company_photos = Photo.objects.filter(enterprise__id=company_id)
    return render(request, 'PastelDeNata/estabelecimento.html', {'company': company, 'latest_reviews': latest_reviews, 'company_photos': company_photos})


def userprofile(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST' and request.POST['action'] == 'GUARDAR':

        if request.FILES.get('picture') is not None:
            picture_file = request.FILES['picture']
            fs = FileSystemStorage()
            current_avatar = client.picture
            if current_avatar != "AvatarDefault":
                fs.delete(current_avatar)

            fs.save("Avatar" + str(client_id), picture_file)
            client.picture = "Avatar" + str(client_id)
            print(client.picture)

        client.description = request.POST['description']
        client.user.first_name = request.POST['firstname']
        client.bio = request.POST['bio']
        client.save()
        client.user.save()

    all_reviews = Rating.objects.filter(client__id=client_id).order_by('-date')
    average_rating = all_reviews.aggregate(avg_value=Avg('value'))['avg_value']
    return render(request, 'PastelDeNata/profile.html',{'client': client, 'all_reviews': all_reviews, 'average_rating': average_rating})


def userprofileedit(request, client_id):
    if(request.user.client.id != client_id):
        return HttpResponseRedirect(reverse('PastelDeNata:index'))
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'PastelDeNata/profile-editar.html',{'client': client})


# ========= 👾 A J A X    A N D    R E Q U E S T 🧩 ========== #
def update_company_photos(company, request):
    pictureList = request.FILES.getlist('companyPhotosSrc')
    pictureListFixed = request.POST.getlist('companyPhotosSrcFixed')
    fs = FileSystemStorage()
    for item in Photo.objects.filter(enterprise__id=company.id):
        if item.href not in pictureListFixed:
            item.delete()
            fs.delete(item.href)

    for item in pictureList:
        file_name = fs.save("Picture" + str(company.id) + "-" + generate_random_filename(20), item)
        photo = Photo.objects.create(enterprise=company, href=file_name)
        photo.save()


def get_all_companies(request):

    district = request.GET['district']
    search_str = request.GET['search_str']
    sorting_mode = request.GET['sorting_mode']

    results = Enterprise.objects.all()
    if search_str != " ":
        results = results.filter(user__first_name__contains=search_str)
    if district != "Portugal Inteiro":
        results = results.filter(district__name=district)

    # Nao vale a pena otimizar, Python 3.9 nao tem switch/match 🙃
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

    return render(request, 'PastelDeNata/company_table.html', {'companies': results, })


def remove_review(request, company_id, client_id):
    company = get_object_or_404(Enterprise, pk=company_id)
    client = get_object_or_404(Client, pk=client_id)
    previous_review = Rating.objects.get(enterprise=company, client=client)
    previous_review.delete()

    total_stars = Rating.objects.filter(enterprise=company).aggregate(total_sum=Sum('value')).get('total_sum', 0)
    if total_stars is None:
        total_stars = 0
    company.rating_amount -= 1
    company.rating_average = total_stars / max(company.rating_amount, 1)
    company.save()
    return HttpResponseRedirect(reverse('PastelDeNata:companyprofile', kwargs={'company_id': company_id}))


# ========= 👾 H E L P F U L    F U N C T I O N S 🧩 ========== #
def generate_random_filename(length):
    allowed_characters = string.ascii_letters + string.digits + "_-"
    random_string = ''.join(random.choice(allowed_characters) for _ in range(length))
    return random_string