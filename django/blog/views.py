from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Post, Writer
from .serializers import PostSer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSer



def index(request):
    writer = Writer.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'writer': writer})


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    return render(request, 'article.html', {'post': post, 'posts': posts})
