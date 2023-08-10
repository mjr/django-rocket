from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from rocket.core.views import ItemViewSet, InstagramAccountViewSet, index, about, make_raffle


router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'instagram-accounts', InstagramAccountViewSet)

urlpatterns = [
    path('', index),
    path('about/', about),
    path('raffle/', make_raffle),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
