"""ali_parse_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
<<<<<<< HEAD
import settingapp.views as settingapp
=======
>>>>>>> afa5e21e613f99dbf538812ca0e28e1d24bc3172
from django.conf.urls import include

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('tasks/', include('mainapp.urls', namespace='tasks')),
<<<<<<< HEAD
    path('settings/', include('settingapp.urls', namespace='settings')),
=======
>>>>>>> afa5e21e613f99dbf538812ca0e28e1d24bc3172
    path('admin/', admin.site.urls),
]
