from django.views.generic.list import ListView
from .models import ExportHistory
from mainapp.models import ParsingTasks, ParsingResults
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from users.models import CustomUser


class ExportHistoryList(ListView):
    model = ExportHistory
    template_name = 'exportapp/export_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExportHistoryList, self).get_context_data(**kwargs)
        context['title'] = "История экспортов"
        return context

    def get_queryset(self):
        queryset = ExportHistory.objects.filter(user_id=self.request.user.id).order_by('-catch_time').all()
        return queryset


class CreateExportHistory(RedirectView):
    def get_redirect_url(self, pk=None):
        results = ParsingResults.objects.filter(task_id=pk).all()
        current_user = CustomUser.objects.filter(id=self.request.user.id).first()

        create_exp_history = ExportHistory()
        create_exp_history.user_id = current_user
        create_exp_history.save()
        create_exp_history.results_id.add(*results)

        return reverse_lazy('export:export_history_list')

