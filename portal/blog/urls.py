from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import index, post_detail

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
