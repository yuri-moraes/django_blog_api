from django.urls import path
from . import views

from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:post_id>/post_detail', views.get_post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)