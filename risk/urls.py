from django.urls import path,re_path,include
from .views import Home
urlpatterns=[
    path('',Home.as_view(),name='home')
]