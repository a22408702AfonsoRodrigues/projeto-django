from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm, RegistoAutorForm

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('likes', 'comentarios').all()
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

@login_required
def artigo_criar(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form})

@login_required
def artigo_editar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form})

@login_required
def artigo_apagar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/artigo_confirmar_apagar.html', {'artigo': artigo})

def artigo_like(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    sessao = request.session.session_key
    if not sessao:
        request.session.create()
        sessao = request.session.session_key
    if not Like.objects.filter(artigo=artigo, sessao=sessao).exists():
        Like.objects.create(artigo=artigo, sessao=sessao)
    return redirect('artigos')

@login_required
def artigo_comentar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()
    return redirect('artigos')

def registo_autor(request):
    form = RegistoAutorForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        grupo = Group.objects.get(name='autores')
        user.groups.add(grupo)
        login(request, user)
        return redirect('artigos')
    return render(request, 'artigos/registo_autor.html', {'form': form})