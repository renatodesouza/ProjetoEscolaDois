from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models.atividade import Atividade
from .models.aluno import Aluno
from .models.coordenador import Coordenador
from .models.curso import Curso
from .models.disciplina import Disciplina
from .models.matricula import Matricula
from .models.professor import Professor
from .models.turma import Turma
from .models.entrega_atividade import EntregaAtividade


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ra', 'usuario', 'data_expiracao', 'imagem')

    fieldsets = [
        ('Informações do Aluno',        {'fields':('ra', 'usuario', 'data_expiracao', 'imagem')})
    ]

    search_fields = ['ra']



@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status', 'atividade',
                    'dt_inicio', 'dt_fim', 'professor', 'disciplina')
    
    fieldsets = [
        ('Atividade',           {'fields':('titulo', 'descricao', 'atividade', 'status')}),
        ('Professor',           {'fields':('professor',)}),
        ('Disciplina',          {'fields':('disciplina',)}),
        ('Turmas',              {'fields':('turma',)}),
        ('Datas',               {'fields':('dt_inicio', 'dt_fim')})
    ]


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        print(request.user)
        return queryset.filter(professor__usuario=request.user)


@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'celular')

    fieldsets = [
        ("Informoções do Coordenador",        {'fields': ('usuario', 'celular')})
    ]

    search_fields = ['usuario']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome', 'descricao', 'periodo', 'modalidade', 'coordenador', 'imagem')

    fieldsets = [
    ('Informações basicas',             {'fields': ('nome', 'descricao')}),
    ('Horarios',                        {'fields': ('periodo', 'modalidade')}),
    ('Coordenador responsavel',         {'fields':('coordenador',)}),
    ('Imagem',                          {'fields':('imagem',)})
    ]
    
    search_fields = ['nome'] 


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

    fieldsets = [
        ('Informações da Disciplina',   {'fields':('nome', 'carga_horaria')}),
        ('Cursos',               {'fields':('curso',)}),
        ('Imagem',                      {'fields':('imagem',)})

    ]

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'turma', 'dt_inicio', 'dt_final', 'status')

    fieldsets = [
        ('Informações da matricula',            {'fields':('aluno', 'curso', 'turma',
                                                           'dt_inicio', 'dt_final', 'status')}),
    ]

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = ('usuario', 'celular')

    fieldsets = [
        ("Informoções do Professor",        {'fields': ('usuario', 'celular')}),
        ("Disciplinas lecionadas",          {'fields':('disciplina',)})
    ]

    search_fields = ['usuario']

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'curso', 'semestre')

    fieldsets = [
        ('Informações da turma',       {'fields':('curso', 'turma', 'semestre', 'disciplina')}),
    ]

@admin.register(EntregaAtividade)
class EntregaAtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resposta', 'status', 'nota', 'aluno', 'atividade', 'professor',
                    'dt_entrega', 'dt_avaliacao', 'observacao', 'file')
    
    fieldsets = [
        ('Titulo',                          {'fields':('titulo',)}),
        ('Professor',                       {'fields':('professor',)}),
        ('Aluno',                           {'fields':('aluno',)}),
        ('Informações da Atividade',        {'fields':('atividade', 'status', 'resposta', 'nota', 'file')}),
        ('Data',                            {'fields':('dt_entrega', 'dt_avaliacao')}),
        ('Observação',                      {'fields':('observacao',)})
    ]

    search_fields = ['titulo', 'aluno']