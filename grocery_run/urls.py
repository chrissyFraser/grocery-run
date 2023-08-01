from django.urls import path
from .views import ItemListView

urlpatterns = [
    path("item_list/", ItemListView.as_view(), name="item_list")
]

