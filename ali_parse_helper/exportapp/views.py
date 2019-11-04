from django.views.generic.list import ListView
from .models import ExportHistory
from mainapp.models import ParsingTasks, ParsingResults
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ExportHistoryList(LoginRequiredMixin, ListView):
    model = ExportHistory
    template_name = 'exportapp/export_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExportHistoryList, self).get_context_data(**kwargs)
        context['title'] = "История экспортов"
        return context

    def get_queryset(self):
        queryset = ExportHistory.objects.filter(user_id=self.request.user.id).order_by('-catch_time').all()
        return queryset


class CreateExportHistory(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, pk=None):
        current_user = CustomUser.objects.filter(id=self.request.user.id).first()

        if pk != 0:
            results = ParsingResults.objects.filter(task_id=pk).all()
        else:
            all_user_tasks = 'select * from mainapp_parsingresults as res'
            'inner join mainapp_parsingtasks as tasks on tasks.id=res.task_id_id'
            f'where tasks.task_user_id_id = {self.request.user.id}'
            results = ParsingResults.objects.raw(all_user_tasks)

        create_exp_history = ExportHistory()
        create_exp_history.user_id = current_user
        create_exp_history.save()
        create_exp_history.results_id.add(*results)

        return reverse_lazy('export:export_history_list')


# def CreateAllExportHistory(LoginRequiredMixin, RedirectView):
#     all_hist = 'select * from mainapp_parsingresults as res'
#                 'inner join mainapp_parsingtasks as tasks on tasks.id=res.task_id_id'
#                 'where tasks.task_user_id_id = {self.request.user.id}'
#
#     def get_redirect_url(self, pk=None):
#         results = ParsingResults.objects.filter(task_id=pk).all()
#         current_user = CustomUser.objects.filter(id=self.request.user.id).first()
#
#         create_exp_history = ExportHistory()
#         create_exp_history.user_id = current_user
#         create_exp_history.save()
#         create_exp_history.results_id.add(*results)
#
#         return reverse_lazy('export:export_history_list')
