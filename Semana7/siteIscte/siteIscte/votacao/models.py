import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils import timezone
class Questao(models.Model):
     questao_texto = models.CharField(max_length=200)
     pub_data = models.DateTimeField('data de publicacao')

     def __str__(self):
          return self.questao_texto
     def publicada_recentemente(self):
          return timezone.now() - datetime.timedelta(days=1) <= self.pub_data

class Opcao(models.Model):
     questao = models.ForeignKey(Questao,on_delete=models.CASCADE)
     opcao_texto = models.CharField(max_length=200)
     votos = models.IntegerField(default=0)

     def __str__(self):
          return self.opcao_texto

class Aluno(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     curso = models.CharField(max_length=100)
     avatar = models.CharField(max_length=25, default="AvatarDefault")
     total_votos = models.IntegerField(default=0)