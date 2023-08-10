from django.contrib import admin

from .models import Item, InstagramAccount, Result


admin.site.register([Item, InstagramAccount, Result])
