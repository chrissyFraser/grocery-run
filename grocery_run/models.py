from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100, null=True, default=1)
    store_name = models.ForeignKey("Store", related_name="store", on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, default=1)
    bought = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Store(models.Model):
    store_name = models.CharField(max_length=100, null=True, default="Any")

    def __str__(self):
        return self.store_name