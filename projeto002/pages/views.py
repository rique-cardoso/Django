from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.http import HttpResponse
# Create your views here.
""" def home(request):
    return HttpResponse('Olá, Django!') """
def about(request):
    return render(
        request,
        'pages/about.html',
        {'descricao': 'Descrição do sobre.'}
    )

def home(request):
    return render(
        request,
        'pages/home.html',
        {'titulo': 'Página Inicial'}
    )

def post_list(request):
    posts = Post.objects.all().order_by('-criada_em')

    return render(
        request,
        'pages/post_list.html',
        {'posts': posts}
    )

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(
        request,
        'pages/post_detail.html',
        {'post': post}
    )
