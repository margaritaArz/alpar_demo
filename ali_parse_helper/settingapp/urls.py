from django.urls import path

import settingapp.views as settingapp

app_name = 'settingapp'

urlpatterns = [
    path('', settingapp.ListSettings.as_view(), name='setting_list'),
    path('user_tasks/edit/<int:pk>/', settingapp.UpdateWorker.as_view(), name='update_worker'),
]