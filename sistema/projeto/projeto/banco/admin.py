from projeto.banco.models import *
from django.contrib import admin

#class TesteInline(admin.TabularInline):
#	model = Disciplina.participantes.through

#class AlunoAdmin(admin.ModelAdmin):
#	inlines = {
#		TesteInline,
#	}	

class DisciplinaAdmin(admin.ModelAdmin):
#	inlines = {
#		TesteInline,
#	}
#	exclude = ('participantes',)
	filter_horizontal = ('participantes',)

class CursoAdmin(admin.ModelAdmin):
	filter_horizontal = ('professores',)

admin.site.register(Professor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aluno)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Monitor)
admin.site.register(Tema)
admin.site.register(Questionario)
admin.site.register(Questao)
admin.site.register(Forum)
