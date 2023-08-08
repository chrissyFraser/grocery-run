from django.contrib import admin
from .models import Item, Store
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(User)