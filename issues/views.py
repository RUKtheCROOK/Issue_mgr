from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from accounts.models import Role
from .models import Status, Priority, Issue

class IssueCreateView(LoginRequiredMixin ,CreateView):
    model = Issue
    template_name = 'issues/issue_new.html'
    fields = ['title', 'description', 'priority','assignee']

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        form.instance.status = Status.objects.get(name='to do')
        return super().form_valid(form)
    
class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Issue
    template_name = 'issues/issue_edit.html'
    fields = ['title', 'description', 'priority','status', 'assignee']

    def test_func(self):
        issue = self.get_object()
        product_owner = Role.objects.get('product owner')
        return (issue.reporter == self.request.user or self.request.user.role == product_owner)
    
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = 'issues/issue_delete.html'
    success_url = reverse_lazy('issue_list')

    def test_func(self):
        issue = self.get_object()
        product_owner = Role.objects.get('product owner')
        return (issue.reporter == self.request.user or self.request.user.role == product_owner)

    
class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/issue_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name='to do')
        in_progress = Status.objects.get(name='in progress')
        done = Status.objects.get(name='done')
        context['to_do_list'] = Issue.objects.filter(status=to_do).order_by('priority').reverse()
        context['in_progress_list'] = Issue.objects.filter(status=in_progress).order_by('priority').reverse()
        context['done_list'] = Issue.objects.filter(status=done).order_by('priority').reverse()
        return context
