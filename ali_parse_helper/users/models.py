from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)
    # avatar = models.ImageField(upload_to='users_avatars', blank=True) #install Pillow
    age = models.PositiveIntegerField(verbose_name='возраст', default=5)

    def __str__(self):
        return self.username

