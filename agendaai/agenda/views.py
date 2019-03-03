from rest_framework import generics, exceptions
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
	serializer_class = UserSerializer
	name = 'user-create'

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