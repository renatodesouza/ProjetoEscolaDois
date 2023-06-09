from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, TemplateView
from .models.curso import Curso
from .models.turma import Turma
from .models.aluno import Aluno
from .models.matricula import Matricula
from .models.atividade import Atividade


def index(request):
    cursos = Curso.objects.all().order_by('?')
    return render(request, 'app/index.html', context={'cursos':cursos})


def curso(request, pk):
    cursos = Curso.objects.all()

    curso = Curso.objects.get(pk=pk)
    
    turmas = Turma.objects.filter(curso__nome=curso).filter(turma='TURMA A')

    disciplinas_por_semestre = []

    for turma in turmas:
        semestre = turma.semestre
        
        disciplinas = turma.disciplina.all()

        disciplinas_por_semestre.append({
            'semestre':semestre,
            'disciplinas':disciplinas
        })
        print('-----------------------------------------------------------------------------------')
        print(curso)
        print(turma)
        print(semestre)
        print(disciplinas_por_semestre)
        print('-----------------------------------------------------------------------------------')

        context = {
            'curso':curso,
            'disciplinas_por_semestre': disciplinas_por_semestre,
            'cursos':cursos
    }
    
        
    return render(request, 'app/curso.html', context)


# ------------------------------------------------------------------


class HomeView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()

        return context
    

class CursoView(DetailView):
    template_name = 'app/curso.html'
    model = Curso
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        curso = self.get_object()
        turmas = Turma.objects.filter(curso__nome=curso, turma='TURMA A')

        disciplinas_por_semestre = [
            {'semestre':turma.semestre,
             'disciplinas':turma.disciplina.all()}
             for turma in turmas
        ]

        context['disciplinas_por_semestre'] = disciplinas_por_semestre

        return context

class AlunoView(DetailView):
    template_name = 'app/aluno.html'
    model = Aluno
    context_object_name = 'aluno'
    
    def get_queryset(self):
        self.nome = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        return Aluno.objects.filter(id=self.nome.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aluno = self.get_object()

        matricula = Matricula.objects.get(aluno=aluno)
        
        context['curso'] = matricula.curso
        context['disciplinas'] = matricula.turma.disciplina.all()
        context['atividades'] = matricula.turma.atividades.all()
        context['atividades_limit'] = matricula.turma.atividades.order_by('?')[:2]
        return context



