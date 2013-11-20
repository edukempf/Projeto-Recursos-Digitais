from django.conf.urls import patterns, url
from banco import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('banco.views',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^sair/$', views.sair, name='sair'),
	url(r'^temas/$', login_required(views.tipo_temas), name='temas'),
	url(r'^temas/(?P<tipotema_id>\d+)$', login_required(views.temasespecificos), name='temasespecificos'),
	url(r'^questao/(?P<tema_id>\d+)$', login_required(views.questao), name='questao'),

)
