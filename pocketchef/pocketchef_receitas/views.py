from django.shortcuts import render
# Create your views here.

def index(request):

    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete',
        4: 'Brownie',
        5: 'Pizza',
        6: 'Suco de laranja'
    }

    dados = { 
        'nome_das_receitas' : receitas 
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')    