from django.db import models
from risk.models import Base

class Article(models.Model):
    title = models.CharField(max_length=200)
    body  = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='media/article_image',null=True)
