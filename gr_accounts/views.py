from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User


class SignUp(CreateView):
    model = User
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        authenticated_user = authenticate(username=username, password=password)
        login(self.request, authenticated_user)
        return redirect(self.success_url)