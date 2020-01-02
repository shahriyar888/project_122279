from django.shortcuts import render
from django.views import generic
from risk.models import Article
from .forms import HomeForm, AiToolsP1Form,AiToolsP2Form,AiToolsP3Form,AiToolsP4Form


class Home(generic.ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'articles'
    extra_context = {'home_form': HomeForm()}


class AiToolsView(generic.TemplateView):
    template_name = 'ai-tools.html'
    extra_context = {
        'aiformp1': AiToolsP1Form(),
        'aiformp2': AiToolsP2Form(),
        'aiformp3': AiToolsP3Form(),
        'aiformp4': AiToolsP4Form(),
    }


class ArticleView(generic.TemplateView):
    template_name = 'article.html'


class AboutUsView(generic.TemplateView):
    template_name = 'about_us.html'


class ContactUsView(generic.TemplateView):
    template_name = 'contact_us.html'

class ResultView(generic.TemplateView):
    template_name = 'result.html'


class UnSuccessView(generic.TemplateView):
    template_name = 'unsuccess.html'


class SuccessView(generic.TemplateView):
    template_name = ''
