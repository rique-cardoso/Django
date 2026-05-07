from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
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

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            form = PostForm()
    
    else:
        form = PostForm()
    
    return render(
        request,
        'pages/post_form.html',
        {'form': form}
    )

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(
        request,
        'pages/post_form.html',
        {'form': form}
    )

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    
    return render(
        request,
        'pages/post_confirm_delete.html',
        {'post': post}
    )