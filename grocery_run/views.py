from django.urls import reverse_lazy
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "index.html"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["name", "quantity"]
    template_name = "create_item.html"
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    
    
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ["name", "quantity"]
    template_name = "update_item.html"
    success_url = reverse_lazy("home")


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy("home")