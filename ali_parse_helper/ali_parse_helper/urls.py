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
import settingapp.views as settingapp
import exportapp.views as exportapp
from django.conf.urls import include
from django.contrib.auth import views as auth_views
# from home.views import e_handler_404, e_handler_500

# handler404 = e_handler_404
# handler500 = e_handler_500

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('tasks/', include('mainapp.urls', namespace='tasks')),
    path('settings/', include('settingapp.urls', namespace='settings')),
    path('export/', include('exportapp.urls', namespace='export')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
]
