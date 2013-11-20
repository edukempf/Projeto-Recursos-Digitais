from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(models.Model):
	nome = models.CharField(max_length=100)
	siape = models.IntegerField()
	email = models.EmailField(max_length=100)
	def __unicode__(self):
		return self.nome

class Curso(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.CharField(max_length=25)
	professores = models.ManyToManyField(Professor)
	def __unicode__(self):
		return self.nome

class Aluno(models.Model):
	user = models.OneToOneField(User)
	nome = models.CharField(max_length=100)
	codigo = models.CharField(max_length=25)
	email = models.EmailField(max_length=100)
	def __unicode__(self):
		return self.nome

#def create_user_aluno(sender, instance, created, **kwargs):
 #   if created:
 #       Aluno.objects.create(user=instance)

#post_save.connect(create_user_aluno, sender=User)

class Disciplina(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.CharField(max_length=25)
	periodo = models.IntegerField()
	participantes = models.ManyToManyField(Aluno)
	models.ForeignKey(Curso)
	models.ForeignKey(Professor)
	def __unicode__(self):
		return self.nome

class Monitor(models.Model):
	models.ForeignKey(Aluno)

class TipoTema(models.Model):
	descricao = models.CharField(max_length=200)
	def __unicode__(self):
		return self.descricao

class Tema(models.Model):
	tema = models.ForeignKey(TipoTema)
	descricao = models.CharField(max_length=200)
	codigo = models.CharField(max_length=25)
	def __unicode__(self):
		return self.codigo

class Questao(models.Model):
	tema = models.ForeignKey(Tema)
	descricao = models.TextField(max_length=1000)
	titulo = models.CharField(max_length=200)
	dificuldade = models.IntegerField()
	def __unicode__(self):
		return self.titulo

class Forum(models.Model):
	questao = models.ForeignKey(Questao)
	monitor = models.ForeignKey(Monitor)
	resposta = models.CharField(max_length=1000)
	data_resposta = models.DateTimeField('Data de resposta:')
