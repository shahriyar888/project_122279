from django.shortcuts import render
from django.views import generic
from risk.models import Article
from .forms import HomeForm



class Home(generic.ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'articles'
    extra_context = {'home_form':HomeForm()}

