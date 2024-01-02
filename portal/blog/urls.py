from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from blog.views import index, post_detail, SignInView, MlPromobotInView

app_name: str = 'blog'

class LogoutViewAndRedirect(LogoutView):
    next_page = '/'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<post_slug>/', post_detail, name='post_detail'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutViewAndRedirect.as_view(), name='signout',),
    path('prototype/ml_promobot/', MlPromobotInView.as_view(), name='ml_promobot'),
]
