from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre', views.about, name='about'),
    path('post', views.post_list, name='post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
