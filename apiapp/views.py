from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import Postserializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer


