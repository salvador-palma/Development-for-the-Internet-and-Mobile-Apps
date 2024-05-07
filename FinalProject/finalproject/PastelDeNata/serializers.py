from django.contrib.auth.models import User
from rest_framework import serializers

from PastelDeNata.models import Enterprise, Rating


class EnterpriseSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    class Meta:
        model = Enterprise
        fields = ('pk', 'user', 'description', 'address', 'district', 'rating_amount', 'rating_average', 'first_name')


class RatingSerializer(serializers.ModelSerializer):

    user_first_name = serializers.CharField(source='client.user.first_name', read_only=True)
    class Meta:
        model = Rating
        fields = ('pk', 'enterprise', 'client', 'value', 'review', 'date', 'user_first_name')