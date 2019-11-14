from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.main, name='index'),
   path('user_tasks', mainapp.ListTasks.as_view(), name='user_tasks'),
   path('user_tasks/create', mainapp.CreateTask.as_view(), name='create_task'),
   path('user_tasks/delete/<int:pk>/', mainapp.DeleteTask.as_view(), name='delete_task'),
   path('user_tasks/edit/<int:pk>/', mainapp.UpdateTask.as_view(), name='update_task'),
]
