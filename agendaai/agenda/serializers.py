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
		fields = ('username', 'email','password')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ('url','pk','street','number','district','city','state','country','zip_code')

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Business
		fields = ('url','pk','name','telefone','email','site','manager', 'cnpj','category','address')

class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profession
		fields = ('url', 'pk', 'name', 'value')

class ProfessionalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Professional
		fields = ('url','pk','usuario', 'profession', 'business')

class DaySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Day
		fields = ('url','pk','name')

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Horario
		fields = ('url','pk','day', 'init', 'end')

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Agenda
		fields = ('url', 'pk', 'business', 'professional', 'horario', 'confirmed', 'cliente')


class AtendimentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Atendimento
		fields = ('url', 'pk','agenda', 'report', 'realizado')