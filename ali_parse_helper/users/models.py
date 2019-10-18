from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    #name = input('введите свое имя: ')
    #email = input('Введите свою почту: ')
    #age = input('Введите свой возраст: ')
    #password = input('Введите пароль: ')


