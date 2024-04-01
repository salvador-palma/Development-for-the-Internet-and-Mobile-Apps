from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

class District(models.Model):
    name = models.CharField(max_length=30)

class Enterprise(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    #Campos calculados (para evitar demasiadas queries em runtime) 💕
    rating_amount = models.IntegerField(default=0)
    rating_average = models.FloatField()

class Rating(models.Model):
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now) #Para obtermos as reviews mais recentes 👍

class Photo(models.Model):
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)
    href = models.CharField(max_length=250)