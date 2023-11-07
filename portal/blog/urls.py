from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from blog.views import index, post_detail, SignInView

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<post_slug>/', post_detail, name='post_detail'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': "/"}, name='signout',),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
