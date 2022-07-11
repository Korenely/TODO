from django.shortcuts import get_object_or_404, redirect
from todo_list.forms import TagForm, TaskForm
from todo_list.models import Task, Tag
from django.urls import reverse_lazy
from django.views import generic


def undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.is_done = False
        task.save()
        return redirect(reverse_lazy('todo_list:task-list'))
    return redirect(reverse_lazy('todo_list:task-list'))


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_done = True
        task.save()
        return redirect(reverse_lazy('todo_list:task-list'))
    return redirect(reverse_lazy('todo_list:task-list'))


class TaskList(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDelete(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/task_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TagList(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_list/tag_list.html"


class TagCreate(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDelete(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "todo_list/tag_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")
