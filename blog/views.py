from django.shortcuts import render
from blog.models import Post, Tag, Author

def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)

def tag(request, tag):
    posts = Post.objects.filter(
        tags__name__contains=tag
    ).order_by('-created_on')

    context = {
        "tag": tag,
        "posts": posts
    }
    return render(request, "tag.html", context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, "detail.html", context)

def author(request, author):
    posts = Post.objects.filter(
        author__name__exact=author
    ).order_by('-created_on')

    context = {
        "author": author,        
        "posts": posts
    }
    return render(request, "author.html", context)

def customerror(request, random):
    return render(request, 'customerror.html', context={'random': random})