from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<str:category>', views.post_list, name='post_list_category'),
    path('posts/detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('search/', views.post_search, name='post_search'),
]