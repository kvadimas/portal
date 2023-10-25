from django.contrib import admin
from django.urls import include, path

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.csrf_failure'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('api.urls')),
    path('', include('blog.urls')),
    path('martor/', include('martor.urls')),
]
