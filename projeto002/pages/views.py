from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Olá, Django!')
def about(request):
    return HttpResponse('Página Sobre')