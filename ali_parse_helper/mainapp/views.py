from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ParsingTasks


def main(request):
    context = {'test': 'test'}
    return render(request, 'mainapp/index.html', context)


class ListTasks(ListView):
    model = ParsingTasks
    template_name = 'mainapp/tasks_base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListTasks, self).get_context_data(**kwargs)
        context['title'] = "Задания для парсинга"
        context['table_head'] = ['Ссылка', 'Активность задания', 'Периодичность(часов)']
        return context
