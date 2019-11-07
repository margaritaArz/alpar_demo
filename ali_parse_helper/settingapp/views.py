from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import ParsingSettings
from django.contrib.auth.mixins import UserPassesTestMixin


class IsSuperUserVies(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ListSettings(IsSuperUserVies, ListView):
    model = ParsingSettings
    template_name = 'settingapp/list_workers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListSettings, self).get_context_data(**kwargs)
        context['title'] = "Страница настроек"
        context['table_head'] = ['Имя воркера', 'Путь до профиля браузера', 'Время между итерациями(минут)',
                                 'Начало итерации', 'Конец итерации', 'Последний выход на связь', ]
        return context


class UpdateWorker(IsSuperUserVies, UpdateView):
    model = ParsingSettings
    template_name = 'mainapp/update_task.html'
    fields = ('worker_name', 'firefox_profile', 'sleeping_time',)

    def get_context_data(self, **kwargs):
        context = super(UpdateWorker, self).get_context_data(**kwargs)
        context['title'] = 'Изменить настройки воркера'
        return context

    def get_success_url(self):
        return reverse_lazy('settingapp:setting_list')
