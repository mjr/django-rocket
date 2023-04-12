from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from .models import Item, InstagramAccount


class AllowAnyForPostAuthenticatedForOthers(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class InstagramAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InstagramAccount
        fields = ('username', 'password')


class InstagramAccountViewSet(viewsets.ModelViewSet):
    queryset = InstagramAccount.objects.all()
    serializer_class = InstagramAccountSerializer
    permission_classes = (AllowAnyForPostAuthenticatedForOthers,)


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


def about(request):
    return render(request, 'index.html')
