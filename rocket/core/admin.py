from django.contrib import admin

from .models import Item, InstagramAccount


admin.site.register([Item, InstagramAccount])
