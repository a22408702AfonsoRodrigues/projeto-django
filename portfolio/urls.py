from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('unidades-curriculares/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),
]