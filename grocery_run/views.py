from django.shortcuts import render
from .models import Item, Store
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = "item_list.html"

    # def get_queryset(self):
    #     return Item.objects.filter(user=self.request.user)
    
    