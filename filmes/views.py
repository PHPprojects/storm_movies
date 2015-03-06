# -*- coding: utf-8 -*-
from django.shortcuts import render
from filmes.models import Genero, Ator, Filme
from django.db.models import Q


# Create your views here.
def home(request):
	#import pdb; pdb.set_trace()
	order = request.GET.get('ord')
	
	if order:
		if order == 'asc':
			filmes = Filme.objects.all().order_by('nome')
		else:
			filmes = Filme.objects.all().order_by('-nome')
	else:	
		filmes = Filme.objects.all().order_by('nome')

	context = {'filmes': filmes, 'count':1}
	return  render(request, 'index.html', context)

def interna(request):
	context = {}
	
	filme_id = request.GET.get('id')
	
	
	filme = Filme.objects.filter(id=filme_id)[0]
	atores = filme.atores.all()
	generos = filme.generos.all()

	lista_filmes = Filme.objects.filter(Q(generos__in=generos) | Q(atores__in=atores)).distinct().exclude(id=filme_id)


	context = {'filme':filme, 'atores':atores, 'generos':generos, 'lista_filmes':lista_filmes}
	
	return  render(request, 'interna.html', context)

def artista(request):
	context = {}
	artista_id = request.GET.get('id')
	
	ator = Ator.objects.all().filter(id=artista_id)[0]
	filmes = Filme.objects.all().filter(atores=artista_id)[:20]

	context = {'ator': ator, 'filmes':filmes, 'count':1}
	return render(request, 'artista.html', context)


def genero(request):
	context = {}
	#import pdb; pdb.set_trace()
	genero_id = request.GET.get('id')

	nome = Genero.objects.all().filter(id=genero_id)[0]

	order = request.GET.get('ord')

	if order:
		if order == 'asc':
			filmes = Filme.objects.all().filter(generos=genero_id).order_by('nome')
		else:
			filmes = Filme.objects.all().filter(generos=genero_id).order_by('-nome')
	else:	
		filmes = Filme.objects.all().filter(generos=genero_id).order_by('nome')

	filmes = Filme.objects.all().filter(generos=genero_id)
	context = {'nome': nome, 'filmes':filmes}
	return render(request, 'genero.html', context)




