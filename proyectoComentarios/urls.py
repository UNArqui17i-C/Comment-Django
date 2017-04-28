
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from comentariosApp.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment',CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
