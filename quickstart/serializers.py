from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Company, Sale, Salesperson


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    salesperson = serializers.StringRelatedField()
    class Meta:
        model = Sale
        fields = ['amount', 'salesperson']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name']  

class SalespersonSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model = Salesperson
        fields = ['name', 'company']  