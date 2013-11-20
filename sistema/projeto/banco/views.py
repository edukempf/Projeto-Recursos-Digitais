# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as logar, logout, authenticate
from django.shortcuts import get_object_or_404, render_to_response, render
from banco.models import *
from random import randint

def index(request):
	return render_to_response("index.html")

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			logar(request, form.get_user())
            		return HttpResponseRedirect("/banco/temas/")
		else:
        		return render(request, "login.html", {"form": form})
	return render(request, "login.html", {"form": AuthenticationForm()})

def sair(request):
	logout(request)
	return render_to_response("index.html")

@login_required
def tipo_temas(request):
	#usuario = request.user
	#aluno = Aluno.objects.filter(user = usuario)
	lista_tipo_tema=TipoTema.objects.all().order_by('descricao')
	return render_to_response('temas.html',{'lista_tipo_tema': lista_tipo_tema})

@login_required
def temasespecificos(request, tipotema_id):
	lista_temas=Tema.objects.filter(tema=tipotema_id).order_by('descricao')
	return render_to_response('temasespecificos.html',{'lista_temas': lista_temas})

@login_required
def questao(request, tema_id):
	lista_questoes=Questao.objects.filter(tema=tema_id).order_by('titulo')
	if (lista_questoes > 0):
		num = randint(0,(len(lista_questoes)-1))
		questao = lista_questoes[num]
	return render_to_response('questao.html',{'questao': questao})
