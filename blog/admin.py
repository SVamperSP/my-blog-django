from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Article,Comment,Moment

class MomentAdmin(MarkdownxModelAdmin):
    class Media:
        js = ("blog/admin_jquery_shim.js",)

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Moment,MomentAdmin)
# Register your models here.
