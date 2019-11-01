from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ParsingTasks
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


def main(request):
    context = {'test': 'test'}
    return render(request, 'mainapp/index.html', context)


class ListTasks(LoginRequiredMixin, ListView):
    model = ParsingTasks
    template_name = 'mainapp/tasks_base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListTasks, self).get_context_data(**kwargs)
        context['title'] = "Задания для парсинга"
        context['table_head'] = ['Ссылка', 'Активность задания', 'Периодичность(часов)']
        return context

    def get_queryset(self):
        get_tasks_and_imgs = 'SELECT distinct on (tasks.id) tasks.id, main_pars_res.id as parsing_id, ' \
                             'main_pars_res.json::json->\'img_\' as img_, tasks.link, tasks.activate, tasks.update_time ' \
                             'FROM mainapp_parsingtasks as tasks ' \
                             'left join mainapp_parsingresults as main_pars_res ' \
                             'on main_pars_res.task_id_id = tasks.id ' \
                             f'where tasks.task_user_id_id = {self.request.user.id} order by tasks.id, main_pars_res.datetime desc'
        queryset = ParsingTasks.objects.raw(get_tasks_and_imgs)
        return queryset


class CreateTask(LoginRequiredMixin, CreateView):
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


class DeleteTask(LoginRequiredMixin, DeleteView):
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


class UpdateTask(LoginRequiredMixin, UpdateView):
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
