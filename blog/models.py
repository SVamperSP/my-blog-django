from django.db import models
from markdownx.models import MarkdownxField

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    article = models.ForeignKey(Article,null=True,on_delete=models.SET_NULL)
    comment = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    url = models.URLField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

class Moment(models.Model):
    content = MarkdownxField()
    create_time = models.DateTimeField(auto_now_add=True)
# Create your models here.
