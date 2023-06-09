from django.urls import path
from . import views
from .views import HomeView, CursoView, AlunoView



app_name = 'app'

urlpatterns = [
    # path('home/', views.index, name='index'),
    # path('curso/<int:pk>/', views.curso, name='curso'),
    path('home/', HomeView.as_view(), name='index'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),
]