import math
import random

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


ANIMALS = {
    'avestruz': [0, 1, 2, 3], # 1
    'águia': [4, 5, 6, 7], # 2
    'burro': [8, 9, 10, 11], # 3
    'borboleta': [12, 13, 14, 15], # 4
    'cachorro': [16, 17, 18, 19], # 5
    'cabra': [20, 21, 22, 23], # 6
    'carneiro': [24, 25, 26, 27], # 7
    'camelo': [28, 29, 30, 31], # 8
    'cobra': [32, 33, 34, 35], # 9
    'coelho': [36, 37, 38, 39], # 10
    'cavalo': [40, 41, 42, 43], # 11
    'elefante': [44, 45, 46, 47], # 12
    'galo': [48, 49, 50, 51], # 13
    'gato': [52, 53, 54, 55], # 14
    'jacaré': [56, 57, 58, 59], # 15
    'leão': [60, 61, 62, 63], # 16
    'macaco': [64, 65, 66, 67], # 17
    'porco': [68, 69, 70, 71], # 18
    'pavão': [72, 73, 74, 75], # 19
    'peru': [76, 77, 78, 79], # 20
    'touro': [80, 81, 82, 83], # 21
    'tigre': [84, 85, 86, 87], # 22
    'urso': [88, 89, 90, 91], # 23
    'veado': [92, 93, 94, 95], # 24
    'vaca': [96, 97, 98, 99], # 25
}


def get_animal(ten):
    animal = None
    for key, values in ANIMALS.items():
        if ten in values:
            animal = key
            break

    return animal


def make_raffle(request):
    result = []
    places = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}
    for index in range(10):
        places_available = [key for key, value in places.items() if value is None]
        position = random.choice(places_available) 

        first_number = random.randint(0, 9)
        second_number = random.randint(0, 9)
        third_number = random.randint(0, 9)
        fourth_number = random.randint(0, 9)
        thousand = f'{first_number}{second_number}{third_number}{fourth_number}'
        places[position] = thousand
        ten = int(thousand[2:4])
        decimal = math.floor((ten / 4) + 1)

        position_str = f'{position}'
        if position != 10:
            position_str = f'0{position}'

        decimal_str = f'{decimal}'
        if decimal < 10:
            decimal_str = f'0{decimal}'

        result.append({
            'decimal': decimal_str,
            'animal': get_animal(ten),
            'position': position_str,
            'thousand': thousand,
        })

    result_sorted = sorted(result, key=lambda k: k['position'])
    # for r in result_sorted:
    #     print(f'{r["position"]} - {r["thousand"]} - {r["animal"].capitalize()} - {r["decimal"]}')

    return render(request, 'result.html', {'result': result_sorted})
