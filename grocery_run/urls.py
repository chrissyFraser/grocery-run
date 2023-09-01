from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path("home/", ItemListView.as_view(), name="home"),
    path("create/", ItemCreateView.as_view(), name="create_item"),
    path("update/<int:pk>/", ItemUpdateView.as_view(), name="update_item"),
    path("delete/<int:pk>/", ItemDeleteView.as_view(), name="delete_item"),
]

