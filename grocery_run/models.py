from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100, null=True, default=1)
    store_name = models.ForeignKey("Store", related_name="store", on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Store(models.Model):
    store_name = models.CharField(max_length=100, null=True, default="Any")

    def __str__(self):
        return self.store_name