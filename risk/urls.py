from django.urls import path,re_path,include
from .views import Home , AiToolsView,UnSuccessView,ArticleView,AboutUsView,ContactUsView,ResultView
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('ai-tools',AiToolsView.as_view(),name='ai-tools'),
    path('unsuccess',UnSuccessView.as_view(),name='unsuccess'),
    path('article',ArticleView.as_view(),name='article'),
    path('result',ResultView.as_view(),name='result'),
    path('about',AboutUsView.as_view(),name='about'),
    path('contact',ContactUsView.as_view(),name='contact'),
]