from django.conf import settings
import markdown

from .models import Article,Comment,Moment
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content','create_time']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','email','url','create_time']

class MomentSerializer(serializers.ModelSerializer):
    content_html = serializers.SerializerMethodField()

    class Meta:
        model = Moment
        fields = ['id','content','content_html','create_time']

    def get_content_html(self,obj):
        html = markdown.markdown(
            obj.content,
            extensions=['codehilite','fenced_code']
        )

        request = self.context.get('request')
        if request is None :
            return html

        media_url = request.build_absolute_uri(settings.MEDIA_URL)
        return html.replace('src="/media/','src="'+media_url)