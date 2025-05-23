from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from store.models import Book, Category


# Create your views here.


def index(request):
    books = Book.objects.filter(available=True).order_by('-created')[:4]
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories,
    }
    return render(request, 'store/index.html', context)


def all_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 12)
    page_num = request.GET.get('page')
    try:
        books = paginator.page(page_num)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'store/all_books.html', {'books': books})


def book_detail(request, pk, slug):
    book = get_object_or_404(Book, id=pk, slug=slug)
    # review = book.review.filter(active=True)
    # form = CommentForm()
    context = {
        'book': book,
    }
    return render(request, "store/detail.html", context)


def books_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category)
    paginator = Paginator(books, 12)
    page_num = request.GET.get('page')
    try:
        books = paginator.page(page_num)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
        'category': category,
    }
    return render(request, 'store/books_by_category.html', context)
