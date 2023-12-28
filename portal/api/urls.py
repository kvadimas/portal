from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (PostViewSet, TagViewSet)
from portal.settings import VERSION

app_name = "api"

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"tags", TagViewSet, basename="tags")

urlpatterns = [
    path(VERSION + "/", include(router.urls)),
    #path(VERSION + "/auth/", include("djoser.urls.authtoken")),
]