from rest_framework import generics
from .ArticleSerializer import ArticleSerializer,CommentSerializer,MomentSerializer
from .models import Article,Comment,Moment

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-create_time')
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
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

class MomentListView(generics.ListAPIView):
    queryset = Moment.objects.all().order_by('-create_time')
    serializer_class = MomentSerializer

class MomentDetailView(generics.RetrieveAPIView):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer
# Create your views here.