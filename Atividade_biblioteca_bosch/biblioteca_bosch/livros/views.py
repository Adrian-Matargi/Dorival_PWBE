from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

# Listar livros
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})

# Cadastrar novo livro
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form': form})

# Atualizar livro
def atualizar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/atualizar_livro.html', {'form': form, 'livro': livro})

# Excluir livro
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/excluir_livro.html', {'livro': livro})