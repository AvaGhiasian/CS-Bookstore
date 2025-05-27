from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from store.forms import ReviewForm, SearchForm
from store.models import Book, Category
from blog.models import Post


# Create your views here.


def index(request):
    books = Book.objects.filter(available=True).order_by('-created')[:4]
    categories = Category.objects.all()
    posts = Post.objects.order_by('-created')[:4]
    context = {
        'books': books,
        'categories': categories,
        'posts': posts,
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
    reviews = book.reviews.filter(active=True).order_by('-created')

    context = {
        'book': book,
        'form': ReviewForm() if request.user.is_authenticated else None,
        'reviews': reviews,
    }
    return render(request, "store/detail.html", context)


def books_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
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


def book_search(request):
    query = None
    results = []
    results_1 = Book.objects.none()
    results_2 = Book.objects.none()

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_1 = Book.objects.annotate(similarity=TrigramSimilarity('title', query)).filter(
                similarity__gte=0.1).order_by('-similarity')
            results_2 = Book.objects.annotate(similarity=TrigramSimilarity('description', query)).filter(
                similarity__gte=0.1).order_by('-similarity')
            results = (results_1 | results_2).order_by('-similarity')

    context = {
        'query': query,
        'results': results,
    }
    return render(request, "store/search.html", context)


@login_required
def review_book(request, pk, slug):
    book = get_object_or_404(Book, id=pk, slug=slug)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect(book.get_absolute_url())

    return redirect(book.get_absolute_url())

