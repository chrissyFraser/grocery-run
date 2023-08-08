from django.urls import path
from .views import ItemListView, ItemCreateView

urlpatterns = [
    path("home/", ItemListView.as_view(), name="home"),
    path("create/", ItemCreateView.as_view(), name="create_item"),
]

