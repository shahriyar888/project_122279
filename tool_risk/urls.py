from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path,include
from risk import urls as risk_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(risk_urls))
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
