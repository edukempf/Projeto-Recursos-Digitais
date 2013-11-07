from django.conf.urls import patterns, url
from banco import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('banco.views',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^sair/$', views.sair, name='sair'),
	url(r'^minhasdisciplinas/$', login_required(views.disciplinas), name='disciplinas'),
	url(r'^(?P<disciplina_id>\d+)/$', login_required(views.questionarios), name='questionarios'),
	url(r'^questionario/(?P<questionario_id>\d+)$', login_required(views.questoes), name='questoes'),

)
