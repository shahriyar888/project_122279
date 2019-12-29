from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True,blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True)


    class Meta:
        abstract=True
