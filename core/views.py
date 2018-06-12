from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    texts = ['Testando a parada', 'Muito doido isso véi'];

    context = {
        'title': 'django e-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)
