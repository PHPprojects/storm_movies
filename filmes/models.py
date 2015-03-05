# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Genero(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		#return unicode(self.nome) 
		return u"%s" % self.nome


class Ator(models.Model):
	nome = models.CharField(max_length=200)
	pais = models.CharField(max_length=200)
	foto = models.ImageField(upload_to='img/ator')


	def __str__(self):
		#return unicode(self.nome)
		return u"%s" % self.nome

class Filme(models.Model): 
	nome = models.CharField(max_length=200)
	sinopse = models.TextField(max_length=400)
	foto = models.ImageField(upload_to='img/filme')
	atores = models.ManyToManyField(Ator)
	generos = models.ManyToManyField(Genero)


	def __str__(self):
		#return unicode(self.nome)
		return u"%s" % self.nome