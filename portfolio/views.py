from django.shortcuts import render
from .models import TFC, Tecnologia, UnidadeCurricular, Projeto, Competencia, Formacao, MakingOf, Licenciatura

# Create your views here.
def index_view(request):
    return render(request, "portfolio/index.html")

def tfcs_view(request):
    tfcs = TFC.objects.select_related('orientador').prefetch_related('tecnologias').all()

    return render(request, "portfolio/tfcs.html", {'tfcs': tfcs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, "portfolio/tecnologias.html", {'tecnologias': tecnologias})

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidades_curriculares').all()

    return render(request, "portfolio/licenciaturas.html", {'licenciaturas': licenciaturas})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.prefetch_related('docentes').select_related('licenciatura').all()

    return render(request, "portfolio/ucs.html", {'ucs': ucs})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()

    return render(request, "portfolio/projetos.html", {'projetos': projetos})

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def makingof_view(request):
    entradas = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'entradas': entradas})