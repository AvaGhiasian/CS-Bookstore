from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.


def index(request):
    posts = Post.published.all()
    context = {
        'posts':posts,
    }
    return render(request, 'blog/index.html',context)


def post_list(request, category=None):
    if category is not None:
        posts = Post.published.filter(category=category)
    else:
        posts = Post.published.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # shows the last page
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {
        'posts': posts,
        'category': category,
        'page': posts,
    }
    return render(request, "blog/list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, "blog/detail.html", context)


@require_POST
def post_comment(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid:
        # .save() can be used bcs ModelForm is used
        # commit = False: do not apply changes to DB
        # when using ModelForms no cleaned data is needed
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'comment': comment,
        'post': post,
        'form': form,
    }
    return render(request, "blog/comment.html", context)


def post_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_1 = Post.published.annotate(similarity=TrigramSimilarity('title', query)).filter(
                similarity__gte=0.1).order_by('-similarity')
            results_2 = Post.published.annotate(similarity=TrigramSimilarity('description', query)).filter(
                similarity__gte=0.1).order_by('-similarity')
            results = (results_1 | results_2).order_by('-similarity')

    context = {
        'query': query,
        'results': results,
    }
    return render(request, "blog/search.html", context)
