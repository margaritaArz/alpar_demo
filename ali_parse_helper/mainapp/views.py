from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ParsingTasks
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404


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

    def get_queryset(self):
        queryset = ParsingTasks.objects.filter(task_user_id=self.request.user.id).all()
        return queryset


class CreateTask(CreateView):
    model = ParsingTasks
    template_name = 'mainapp/create_task.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['title'] = 'Создать задачу для парсинга'
        return context

    # def form_valid(self, form):
    #     phrase_condition = get_object_or_404(PhrasesCondition, id=self.kwargs['pk'])
    #     form.instance.phrase_condition = phrase_condition
    #     return super(PhraseBlockCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mainapp:user_tasks')


class DeleteTask(DeleteView):
    model = ParsingTasks
    template_name = 'mainapp/delete_task.html'

    def get(self, request, *args, **kwargs):
        if self.get_object():
            return super().get(request, *args, **kwargs)
        else:
            raise Http404

    # Продумать позже, чтобы не удалять задания, а деактивировать.
    # Чтобы из таблицы результатов не удалялись записи
    def get_context_data(self, **kwargs):
        context = super(DeleteTask, self).get_context_data(**kwargs)
        context['title'] = 'Удалить задачу для парсинга'
        return context

    def get_success_url(self):
        return reverse_lazy('mainapp:user_tasks')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user.id == obj.task_user_id.id:
            return super().get_object()


class UpdateTask(UpdateView):
    model = ParsingTasks
    template_name = 'mainapp/update_task.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        if self.get_object():
            return super().get(request, *args, **kwargs)
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(UpdateTask, self).get_context_data(**kwargs)
        context['title'] = 'Изменить задачу для парсинга'
        return context

    def get_success_url(self):
        return reverse_lazy('mainapp:user_tasks')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user.id == obj.task_user_id.id:
            return super().get_object()
