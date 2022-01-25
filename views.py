from django.shortcuts import render
from .models import Task, TaskUpdate, TaskNote
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.db import transaction
from . import forms as app_forms
from django.views import generic
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def update(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return HttpResponseRedirect(reverse("kanban:index"))


class IndexView(generic.ListView):
    form = app_forms.CardForm()
    template_name = "kanban/directory.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.all()


class NewTask(CreateView):
    model = Task
    template_name = "Polls/question_create.html"
    form_class = app_forms.TaskForm
    success_url = None

    def form_invalid(self, form):
        print("fail")
        return reverse_lazy('Polls:vote', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            create_recipt = TaskUpdate(task=self.object, old_status=0, new_status=1)
            create_recipt.save()
        return super(NewTask, self).form_valid(form)

    def get_success_url(self):
        print("sucess")
        return reverse_lazy('Polls:details', kwargs={'pk': self.object.pk})


class HistoryView(generic.DetailView):
    model = Task
    template_name = "kanban/history.html"

    def get_queryset(self):
        return Task.objects.all()

def new_card(request):
    if request.method == "POST":
        a = Task(title=request.POST["task_title"])
        a.save()
    return HttpResponseRedirect(reverse("kanban:index"))

def new_card(request, task):
    if request.method == "POST":
        otask = get_object_or_404(Task, pk=task)
        note = TaskNote(status=otask.status, task=otask, note=request.POST["note"])
        note.save()
    print(task)
    return HttpResponseRedirect(reverse("kanban:history", args=(task,)))
