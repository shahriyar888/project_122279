from django.contrib import admin
from risk.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   # fields = ['title','body','image']
    fields = []
