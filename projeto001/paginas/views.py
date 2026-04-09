from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sobre(request):
    return HttpResponse('<h1>Sobre</h1>')

def contato(request):
    return HttpResponse('<h1>Contato</h1>')