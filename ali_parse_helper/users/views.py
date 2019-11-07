from django.views.generic import CreateView
from .models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'users/login.html'
    fields = ('name', 'email', 'password')