from django.shortcuts import render
from rest_framework import generics
from .ArticleSerializer import ArticleSerializer,CommentSerializer
from .models import Article,Comment

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        id = self.kwargs['pk']
        return Comment.objects.filter(article_id=id,is_approved=True)

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        article = Article.objects.get(id=id)
        serializer.save(article=article)
# Create your views here.
