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

def index(request):
	return render_to_response("index.html")

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			logar(request, form.get_user())
            		return HttpResponseRedirect("/banco/minhasdisciplinas/")
		else:
        		return render(request, "login.html", {"form": form})
	return render(request, "login.html", {"form": AuthenticationForm()})

def sair(request):
	logout(request)
	return render_to_response("index.html")

@login_required
def disciplinas(request):
	usuario = request.user
	aluno = Aluno.objects.filter(user = usuario)
	lista_disciplina=Disciplina.objects.filter(participantes = aluno).order_by('nome')
	return render_to_response('disciplinas.html',{'lista_disciplina': lista_disciplina})

@login_required
def questionarios(request, disciplina_id):
	lista_questionarios=Questionario.objects.filter(disciplina=disciplina_id).order_by('titulo')
	return render_to_response('questionarios.html',{'lista_questionarios': lista_questionarios})

@login_required
def questoes(request, questionario_id):
	lista_questoes=Questao.objects.filter(questionario=questionario_id).order_by('titulo')
	return render_to_response('questoes.html',{'lista_questoes': lista_questoes})
