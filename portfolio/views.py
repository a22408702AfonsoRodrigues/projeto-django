from django.shortcuts import render
from .models import TFC, Tecnologia, UnidadeCurricular, Projeto, Competencia, Formacao, MakingOf, Licenciatura, TipoTecnologia
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


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

@login_required
def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_form.html', {'form': form})

@login_required
def projeto_editar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')

    return render(request, 'portfolio/projeto_form.html', {'form': form})

@login_required
def projeto_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_confirmar_apagar.html', {'projeto': projeto})

@login_required
def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'form': form})

@login_required
def tecnologia_editar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')

    return render(request, 'portfolio/tecnologia_form.html', {'form': form})

@login_required
def tecnologia_apagar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_confirmar_apagar.html', {'tecnologia': tecnologia})

@login_required
def competencia_criar(request):
    form = CompetenciaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form})

@login_required
def competencia_editar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, request.FILES or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')

    return render(request, 'portfolio/competencia_form.html', {'form': form})

@login_required
def competencia_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_confirmar_apagar.html', {'competencia': competencia})

@login_required
def formacao_criar(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form})

@login_required
def formacao_editar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form})

@login_required
def formacao_apagar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_confirmar_apagar.html', {'formacao': formacao})

def sobre_view(request):
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/sobre.html', {'tipos': tipos})