from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.all_books, name='all_books'),
    path('books/<int:pk>/<slug:slug>/', views.book_detail, name='book_detail'),
    path('category/<slug:slug>/', views.books_by_category, name='books_by_category'),
    path('search/', views.book_search, name='search'),
    path('<int:pk>/<slug:slug>/review/', views.review_book, name='review_book'),
]
