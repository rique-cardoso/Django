from django.contrib import admin
from .models import Page, Post

# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'criada_em')
    search_fields = ('titulo',)
    list_filter = ('criada_em'),

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'criada_em')
    search_fields = ('titulo',)
    list_filter = ('criada_em'),