from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import *

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'available', 'price']
    list_filter = ['title', 'available', 'price']
    list_editable = ['available']
    search_fields = ['title', 'description']
    ordering = ['title']
    raw_id_fields = ['author']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name']
    search_fields = ['name', 'bio']
    ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['book', 'title', 'created']

@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating','created', 'active']
    list_filter = ['active', ('created', DateFieldListFilter)]
    search_fields = ['rating', 'body']
    list_editable = ['active']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['user', 'created', 'paid']
    list_display = ['user', 'created', 'paid']
    list_editable = ['paid']