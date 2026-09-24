from django.urls import path
from .views import ArticleListView,ArticleDetailView,CommentListCreateView,MomentListView,MomentDetailView
urlpatterns = [
    path('articles/',ArticleListView.as_view(),name='article-list'),
    path('articles/<int:pk>/',ArticleDetailView.as_view(),name='articles-detail'),
    path('articles/<int:pk>/comments/',CommentListCreateView.as_view(),name='articles-comments'),
    path('moment/',MomentListView.as_view(),name='moment-list-create'),
    path('moment/<int:pk>/',MomentDetailView.as_view(),name='moment-detail'),
]

