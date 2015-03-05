# -*- coding: utf-8 -*-
from django.shortcuts import render
from filmes.models import Genero, Ator, Filme


# Create your views here.
def home(request):
	#import pdb; pdb.set_trace()
	filmes = Filme.objects.all()
	context = {'filmes': filmes}
	return  render(request, 'index.html', context)

def interna(request):
	context = {}
	filme_id = request.GET.get('id')

	if filme_id :
		#Pega um somente uma reposta
		Filme.objects.get(id=filme_id)

		#Pega todos os filmes - Retorma uma lista
		filmes = Filme.objects.filter(id=filme_id) 

		if len(filmes) != 1:
			return  render(request, 'interna.html', context)
		else:
			context = {'Filme':filmes[0]}
			return  render(request, 'interna.html', context)
	else:
		
		return  render(request, 'interna.html', context)
			