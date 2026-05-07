from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre', views.about, name='about'),
    path('posts', views.post_list, name='posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/novo/', views.post_create, name="post_create"),
    path('posts/<int:post_id>/editar/', views.post_update, name='post_update'),
]
