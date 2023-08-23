from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagina(request):
    return render(request, '<h1>Ola mundo!</h1>')


def index(request):
    return render(request, 'index.html')


def carrinho(request):
    return render(request, 'carrinho.html')

def produtos(request):
    return render(request, 'produtos.html')