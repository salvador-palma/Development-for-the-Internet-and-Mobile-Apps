from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

class District(models.Model):
    name = models.CharField(max_length=30)

class Enterprise(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField(null=True)
    address = models.CharField(max_length=100, null=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE, null=True)
    #Campos calculados (para evitar demasiadas queries em runtime) 💕
    rating_amount = models.IntegerField(default=0)
    rating_average = models.FloatField(default=0)

    def is_valid(self):
        return bool(self.description) and bool(self.address) and bool(self.district)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, default="Sem descrição ainda...")
    bio = models.CharField(max_length=150, null=True, default="Sem bio ainda...")
    picture = models.CharField(max_length=100, null=True, default="AvatarDefault")



class Rating(models.Model):
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now) #Para obtermos as reviews mais recentes 👍



class Photo(models.Model):
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)
    href = models.CharField(max_length=250)