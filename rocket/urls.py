from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from rocket.core.views import ItemViewSet


router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
