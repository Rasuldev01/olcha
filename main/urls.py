from django.urls import path
from django.conf import settings
from .views import Main
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', Main.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

