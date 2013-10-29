from django.conf.urls import patterns, url
from banco import views

urlpatterns = patterns('banco.views',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<disciplina_id>\d+)/$', views.questionarios, name='questionarios'),
	url(r'^questionario/(?P<questionario_id>\d+)$', views.questoes, name='questoes'),

)
