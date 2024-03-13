from django.db.models import *

from votacao.models import Questao, Opcao
from django.utils import timezone

print("=====TESTE DE BASE DE DADOS=====")

print("Alinea a)")
result = Questao.objects.all()
print(result)

print("Alinea b)")
result = Opcao.objects.filter(questao__questao_texto__startswith = "Gostas de ")
print(result)

print("Alinea c)")
result = Opcao.objects.filter(questao__questao_texto__startswith = "Gostas de ", votos__gt = 2)
print(result)

print("Alinea d)")
result = Questao.objects.filter(pub_data__year__gte = timezone.now().year - 3)
print(result)

print("Alinea e)")
result = Opcao.objects.aggregate(Sum("votos", default=0))
print(result)

print("Alinea f)")
for q in Questao.objects.all():
    o = None
    for opcao in q.opcao_set.all():
        if o is None or opcao.votos > o.votos:
            o = opcao
    print(str(q) + " > " + str(o))

