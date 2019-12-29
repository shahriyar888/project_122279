from django.shortcuts import render
from django.views import generic
from risk.models import Article



class Home(generic.ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'articles'
