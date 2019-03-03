from django.contrib.auth.models import User
from rest_framework import serializers
from agenda.models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('url', 'pk', 'name')
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'pk', 'username', 'email')

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'pk', 'username', 'email','password')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ('url','pk','street','number','district','city','state','country','zip_code')

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		fields = ('url','pk','name','telefone','email','site','manager', 'cnpj','category','address')