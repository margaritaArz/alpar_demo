from django.urls import path

import exportapp.views as exportapp

app_name = 'settingapp'

urlpatterns = [
    path('', exportapp.ExportHistoryList.as_view(), name='export_history_list'),
    path('create/<int:pk>/', exportapp.CreateExportHistory.as_view(), name='create_export_history'),
]