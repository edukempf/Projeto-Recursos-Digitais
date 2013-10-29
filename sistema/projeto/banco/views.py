# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from banco.models import *


def index(request):
	lista_disciplina=Disciplina.objects.all().order_by('nome')
	return render_to_response('index.html',{'lista_disciplina': lista_disciplina})

def questionarios(request, disciplina_id):
	lista_questionarios=Questionario.objects.filter(disciplina=disciplina_id).order_by('titulo')
	return render_to_response('questionarios.html',{'lista_questionarios': lista_questionarios})

def questoes(request, questionario_id):
	lista_questoes=Questao.objects.filter(questionario=questionario_id).order_by('titulo')
	return render_to_response('questoes.html',{'lista_questoes': lista_questoes})
