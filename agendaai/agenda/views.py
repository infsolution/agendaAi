from rest_framework import generics, exceptions
from rest_framework.response import Response
from agenda.models import *
from agenda.serializers import *
#from django.shortcuts import render

class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	name = 'category-detail'

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'

class UserCreate(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer
	name = 'user-create'
	def perform_create(self, serializer):
	 	if self.request.method == 'POST':
	 		user = User.objects.create_user(self.request.POST['username'],self.request.POST['email'],self.request.POST['password'] )
	 		user.save()
	 	return serializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'

class BusinessList(generics.ListCreateAPIView):
	queryset = Business.objects.all()
	serializer_class = BusinessSerializer
	name = 'business-list'

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Business.objects.all()
	serializer_class = BusinessSerializer
	name = 'business-detail'

class AddressList(generics.ListCreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	name = 'address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	name = 'address-detail'

class ProfessionList(generics.ListCreateAPIView):
	queryset = Profession.objects.all()
	serializer_class = ProfessionSerializer
	name = 'profession-list'

class ProfessionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profession.objects.all()
	serializer_class = ProfessionSerializer
	name = 'profession-detail'

class ProfessionalList(generics.ListCreateAPIView):
	queryset = Professional.objects.all()
	serializer_class = ProfessionalSerializer
	name = 'professional-list'

class ProfessionalDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Professional.objects.all()
	serializer_class = ProfessionalSerializer
	name = 'professional-detail'

class DayList(generics.ListCreateAPIView):
	queryset = Day.objects.all()
	serializer_class = DaySerializer
	name = 'day-list'

class DayDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Day.objects.all()
	serializer_class = DaySerializer
	name = 'day-detail'

class HorarioList(generics.ListCreateAPIView):
	queryset = Horario.objects.all()
	serializer_class = HorarioSerializer
	name = 'horario-list'

class HorarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Horario.objects.all()
	serializer_class = HorarioSerializer
	name = 'horario-detail'
class AtendimentoList(generics.ListCreateAPIView):
	queryset = Atendimento.objects.all()
	serializer_class = AtendimentoSerializer
	name = 'atendimento-list'
class AtendimentoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Atendimento.objects.all()
	serializer_class = AtendimentoSerializer
	name= 'atendimento-detail'