from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Address(models.Model):
	street = models.CharField(max_length=200)
	number = models.CharField(max_length=5)
	district = models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country =models.CharField(max_length=200, null=True)
	zip_code = models.CharField(max_length=11, null=True)
	def __str__(self):
		return self.street+' Nº '+self.number+' '+self.district

class Business(models.Model):
	name = models.CharField(max_length=200)
	telefone = models.CharField(max_length=20, null=True)
	email = models.CharField(max_length=200, null=True)
	site=models.CharField(max_length=200, null=True)
	manager = models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
	cnpj = models.CharField(max_length=20)
	category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING, null=True)
	address = models.OneToOneField(Address, related_name='address', on_delete=models.DO_NOTHING, null=True)
	def __str__(self):
		return self.name
class Profession(models.Model):
	name=models.CharField(max_length=200)
	value = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	def __str__(self):
		return self.name

class Professional(models.Model):
	usuario = models.OneToOneField(User, related_name='professional', on_delete=models.CASCADE)
	profession = models.OneToOneField(Profession, related_name='profession', on_delete=models.CASCADE)
	business = models.ForeignKey(Business, related_name='professionals', on_delete=models.CASCADE, null=True)


class Day(models.Model):
	name = models.CharField(max_length=29)
	def __str__(self):
		return self.name

class Horario(models.Model):
	day = models.ForeignKey(Day, related_name='day', on_delete=models.CASCADE)
	init = models.CharField(max_length=5)
	end = models.CharField(max_length=5)

class Atendimento(models.Model):
	usuario = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)
	report = models.CharField(max_length=512, null=True)
	realizado = models.BooleanField(default=False)

class Agenda(models.Model):
	business = models.ForeignKey(Business, related_name='agenda', on_delete=models.CASCADE, default=None)
	horario = models.ForeignKey(Horario, related_name='horario', on_delete=models.CASCADE)
	atendimento = models.ForeignKey(Atendimento, related_name='atendimento', on_delete=models.CASCADE)
	confirmed = models.BooleanField(default=False)