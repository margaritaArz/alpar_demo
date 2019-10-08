from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.main, name='index'),
   path('user_tasks', mainapp.ListTasks.as_view(), name='user_tasks'),
]